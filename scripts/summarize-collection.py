"""Measure current skill sources and bounded captured CLI receipts without inference."""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
import math
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
from unittest.mock import patch

import tiktoken
import yaml


ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "bilingual-business-reply", "agent-permissions-audit",
    "lead-follow-up", "review-response", "project-handoff", "skill-creator",
)
MAX_RUNS, MAX_FILE, MAX_TOTAL = 500, 512 * 1024, 25 * 1024 * 1024
CLAUDE_FIELDS = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
CODEX_FIELDS = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens", "reasoning_output_tokens")
ACTION_TYPES = {"command_execution", "file_change", "mcp_tool_call", "web_search", "tool_call"}


class InputError(Exception):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def number(value):
    return value if type(value) in (int, float) and math.isfinite(value) and value >= 0 else None


def identifier(value):
    if isinstance(value, str) and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:/() ;=-]{0,159}", value):
        return value
    return None


def source_hash(value):
    return value if isinstance(value, str) and re.fullmatch(r"[a-f0-9]{64}", value) else None


def offline_tokenizer():
    # This replaces the dependency's cache reader, not target code. It never fetches or repairs a cache.
    def cached_only(url, expected_hash=None):
        cache = os.environ.get("TIKTOKEN_CACHE_DIR", os.environ.get("DATA_GYM_CACHE_DIR"))
        directory = Path(cache) if cache else Path(tempfile.gettempdir()) / "data-gym-cache"
        path = directory / hashlib.sha1(url.encode()).hexdigest()
        if not path.is_file():
            raise InputError("offline_tokenizer_cache_unavailable")
        data = path.read_bytes()
        if expected_hash and digest(data) != expected_hash:
            raise InputError("offline_tokenizer_cache_hash_mismatch")
        return data

    with patch("tiktoken.load.read_file_cached", cached_only):
        return tiktoken.get_encoding("o200k_base")


class Reader:
    def __init__(self, roots):
        self.roots = [root.resolve() for root in roots]
        self.bytes_read = 0
        self.cache = {}

    def read(self, path):
        if path.is_symlink():
            raise InputError("symlink_input_rejected")
        resolved = path.resolve()
        if not any(resolved.is_relative_to(root) for root in self.roots):
            raise InputError("input_outside_approved_roots")
        if resolved in self.cache:
            return self.cache[resolved]
        try:
            if not stat.S_ISREG(resolved.lstat().st_mode):
                raise InputError("nonordinary_input_rejected")
            nonblock = getattr(os, "O_NONBLOCK", None)
            if nonblock is None:
                raise InputError("nonblocking_open_unavailable")
            descriptor = os.open(resolved, os.O_RDONLY | nonblock | getattr(os, "O_NOFOLLOW", 0))
        except FileNotFoundError:
            return None
        with os.fdopen(descriptor, "rb") as stream:
            info = os.fstat(stream.fileno())
            if not stat.S_ISREG(info.st_mode):
                raise InputError("nonordinary_input_rejected")
            if info.st_size > MAX_FILE:
                raise InputError("per_file_limit_exceeded")
            if self.bytes_read + info.st_size > MAX_TOTAL:
                raise InputError("total_input_limit_exceeded")
            data = stream.read(info.st_size)
            if len(data) != info.st_size or os.fstat(stream.fileno()).st_size != info.st_size:
                raise InputError("input_changed_during_read")
        self.bytes_read += len(data)
        self.cache[resolved] = data
        return data


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate_key")
        result[key] = value
    return result


def parse_json(data):
    return json.loads(data, object_pairs_hook=unique_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("nonfinite_json")))


def counts(text, encoding):
    return {"o200k_base_tokens": len(encoding.encode(text, disallowed_special=())),
            "characters": len(text), "words": len(text.split()), "utf8_bytes": len(text.encode())}


def inventory(directory, limit=5000, run_slugs=None):
    found, visited = [], 0
    for current, dirs, files in os.walk(directory, followlinks=False):
        if run_slugs is not None:
            depth = len(Path(current).relative_to(directory).parts)
            if depth == 1:
                dirs[:] = [name for name in dirs if name in run_slugs]
            if depth < 2:
                files[:] = []
        visited += 1 + len(dirs) + len(files)
        if visited > limit:
            raise InputError("inventory_limit_exceeded")
        if any((Path(current) / name).is_symlink() for name in dirs + files):
            raise InputError("symlink_inventory_entry_rejected")
        found.extend(Path(current) / name for name in files)
    return sorted(found)


def measure_sources(reader, encoding):
    result = []
    for slug in SLUGS:
        package = ROOT / "skills" / slug
        raw = reader.read(package / "SKILL.md")
        if raw is None:
            raise InputError("missing_skill_core")
        text = raw.decode("utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0]:
            raise InputError("invalid_skill_frontmatter")
        metadata = yaml.safe_load(parts[1])
        if not isinstance(metadata, dict) or metadata.get("name") != slug or not isinstance(metadata.get("description"), str):
            raise InputError("invalid_discovery_metadata")
        references = []
        reference_root = package / "references"
        if reference_root.exists():
            for path in inventory(reference_root, 1000):
                data = reader.read(path)
                references.append({"path": path.relative_to(package).as_posix(), "sha256": digest(data),
                                   "size": counts(data.decode("utf-8"), encoding)})
        result.append({"slug": slug, "source_sha256": digest(raw), "skill_md": counts(text, encoding),
                       "discovery_name_description": counts(metadata["name"] + "\n" + metadata["description"], encoding),
                       "optional_reference_inventory": references,
                       "optional_references_loaded_at_runtime": None})
    return result


def text_blocks(content):
    if isinstance(content, str):
        return [content]
    if isinstance(content, list):
        return [block["text"] for block in content if isinstance(block, dict) and isinstance(block.get("text"), str)]
    return []


def numeric_usage(value, host):
    fields = CLAUDE_FIELDS if host == "claude" else CODEX_FIELDS
    return {field: number(value.get(field)) for field in fields} if isinstance(value, dict) else None


def settings(launch):
    argv = launch.get("argv", [])
    result = {"requested_model": None, "requested_effort": None, "max_turns": None, "max_budget_usd": None,
              "timeout_seconds": number(launch.get("timeout_seconds")),
              "automatic_retries": number(launch.get("automatic_retries"))}
    if not isinstance(argv, list):
        return result
    for index, value in enumerate(argv[:-1]):
        following = argv[index + 1]
        if value in ("--model", "-m"):
            result["requested_model"] = identifier(following)
        elif value in ("--max-turns", "--max-budget-usd"):
            try:
                result["max_turns" if value == "--max-turns" else "max_budget_usd"] = number(float(following))
            except (ValueError, TypeError):
                pass
        elif value == "-c" and isinstance(following, str):
            match = re.fullmatch(r'(model|model_reasoning_effort)="([A-Za-z0-9_.-]+)"', following)
            if match:
                result["requested_model" if match[1] == "model" else "requested_effort"] = match[2]
    return result


def measure_run(directory, runs_root, current_hashes, reader, encoding):
    run_id = directory.relative_to(runs_root).as_posix()
    warnings, data = [], {}
    for filename in ("summary.json", "launch.json", "prompt.txt", "output.txt", "events.jsonl"):
        raw = reader.read(directory / filename)
        if raw is None:
            warnings.append("missing_" + filename)
        data[filename] = raw
    parsed = {}
    for filename in ("summary.json", "launch.json"):
        try:
            value = parse_json(data[filename]) if data[filename] is not None else {}
            parsed[filename] = value if isinstance(value, dict) else {}
        except (ValueError, UnicodeError, RecursionError):
            warnings.append("invalid_" + filename)
            parsed[filename] = {}
    summary, launch = parsed["summary.json"], parsed["launch.json"]
    host = summary.get("host") if summary.get("host") in ("claude", "codex") else "unknown"
    slug = summary.get("skill") if summary.get("skill") in SLUGS else None
    events = []
    malformed = 0
    for line in (data["events.jsonl"] or b"").splitlines():
        try:
            event = parse_json(line)
            if not isinstance(event, dict):
                raise ValueError("nonobject_event")
            events.append(event)
        except (ValueError, UnicodeError, RecursionError):
            malformed += 1
    if malformed:
        warnings.append("malformed_event_lines")
    init = next((event for event in events if event.get("type") == "system" and event.get("subtype") == "init"), {})
    final = next((event for event in reversed(events) if event.get("type") == "result"), {})
    turns = [event for event in events if event.get("type") == "turn.completed"]
    raw_usage = final.get("usage") if host == "claude" else turns[0].get("usage") if len(turns) == 1 else None
    aggregate = numeric_usage(raw_usage, host) if host in ("claude", "codex") else None
    summary_usage = numeric_usage(summary.get("usage"), host) if host in ("claude", "codex") else None
    required = CLAUDE_FIELDS if host == "claude" else ("input_tokens", "output_tokens")
    complete = malformed == 0 and aggregate is not None and all(aggregate.get(key) is not None for key in required)
    if host == "codex" and len(turns) != 1:
        warnings.append("codex_session_aggregate_scope_unknown")
    messages, calls, results, items, injections = {}, {}, {}, {}, []
    missing_message_ids = 0
    for index, event in enumerate(events):
        message = event.get("message", {})
        if not isinstance(message, dict):
            message = {}
        if event.get("type") == "assistant" and isinstance(message.get("usage"), dict):
            if message.get("id"):
                messages[message["id"]] = message["usage"]
            else:
                missing_message_ids += 1
        for block in message.get("content", []) if isinstance(message.get("content"), list) else []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                calls[block.get("id") or "event-" + str(index)] = identifier(block.get("name")) or "unknown"
            elif block.get("type") == "tool_result":
                results[block.get("tool_use_id") or "event-" + str(index)] = "\n".join(text_blocks(block.get("content")))
        if event.get("type") == "user":
            injections.extend(text for text in text_blocks(message.get("content")) if text.startswith("Base directory for this skill:"))
        item = event.get("item", {})
        if isinstance(item, dict) and item.get("type") in ACTION_TYPES and item.get("id"):
            items[item["id"]] = item
    tool_texts = list(results.values())
    if host == "codex":
        calls = {key: item["type"] for key, item in items.items()}
        tool_texts = [item["aggregated_output"] for item in items.values() if isinstance(item.get("aggregated_output"), str)]
    message_sum = {field: sum(value[field] for value in messages.values()) if not missing_message_ids and all(number(value.get(field)) is not None for value in messages.values()) else None for field in CLAUDE_FIELDS} if messages else None
    crosscheck = {"deduplicated_message_count": len(messages), "messages_without_ids": missing_message_ids,
                  "message_usage_sum_not_added_to_totals": message_sum,
                  "aggregate_minus_message_sum": {field: aggregate[field] - message_sum[field] if aggregate and aggregate.get(field) is not None and message_sum[field] is not None else None for field in CLAUDE_FIELDS} if message_sum else None,
                  "limit": "Stream message usage can be partial, especially output. Only final CLI aggregate usage enters totals." if host == "claude" else "Codex does not emit comparable per-message usage here."}
    summary_hash, launch_hash = source_hash(summary.get("source_sha256")), source_hash(launch.get("source_sha256"))
    recorded_hash = summary_hash if summary_hash == launch_hash else None
    case = identifier(summary.get("case"))
    group = "control" if "selection" in directory.name or (case or "").startswith("selection") else "baseline" if summary.get("mode") == "baseline" else "current" if slug and recorded_hash == current_hashes[slug] else "history" if slug and recorded_hash else "unknown"
    repair = re.search(r"-r(\d+)$", directory.name)
    session_id = init.get("session_id") if host == "claude" else next((event.get("thread_id") for event in events if event.get("type") == "thread.started"), None)
    session_key = digest((host + ":" + str(session_id)).encode()) if session_id else digest((data["events.jsonl"] or b"") + (data["launch.json"] or b""))
    text_counts = {}
    for filename in ("prompt.txt", "output.txt"):
        try:
            text_counts[filename] = {**counts(data[filename].decode("utf-8"), encoding), "sha256": digest(data[filename])} if data[filename] is not None else None
        except UnicodeError:
            text_counts[filename] = None
            warnings.append("invalid_utf8_" + filename)
    aggregate_total = (sum(aggregate[key] for key in CLAUDE_FIELDS) if host == "claude" else aggregate["input_tokens"] + aggregate["output_tokens"]) if complete else None
    observed_model = identifier(init.get("model")) if host == "claude" else None
    model_usage = final.get("modelUsage")
    return {"run_id": run_id, "group": group, "host": host, "skill": slug, "case": case,
            "source_sha256": recorded_hash, "source_hashes_agree": summary_hash == launch_hash if summary_hash and launch_hash else None,
            "source_hash_is_recorded_identity_not_body_observation": True,
            "manual_repair_rerun": repair is not None, "manual_repair_label": int(repair[1]) if repair else None,
            "observed_model": observed_model, "reported_model_label": identifier(summary.get("model")),
            "cli_version": identifier(init.get("claude_code_version")),
            "controller_sha256": source_hash(launch.get("controller_sha256")),
            "settings": settings(launch), "started_at": launch.get("started_at") if isinstance(launch.get("started_at"), str) and re.fullmatch(r"[0-9TZ:+.-]+", launch["started_at"]) else None,
            "elapsed_seconds": number(summary.get("elapsed_seconds")),
            "prompt": text_counts["prompt.txt"], "final_output": text_counts["output.txt"],
            "observed_calls": {"count": len(calls), "by_name": dict(sorted(Counter(calls.values()).items())), "event_stream_complete": data["events.jsonl"] is not None and malformed == 0},
            "observed_tool_result_text": {"blocks": len(tool_texts), "sum_separate_blocks": {key: sum(counts(text, encoding)[key] for text in tool_texts) for key in ("o200k_base_tokens", "characters", "words", "utf8_bytes")}},
            "observed_internal_skill_injection_text": {"blocks": len(injections), "o200k_base_tokens_sum": sum(counts(text, encoding)["o200k_base_tokens"] for text in injections)},
            "external_user_turns": 1, "external_followup_replies": 0, "completed_clarification_turns": 0,
            "assistant_clarification_questions": None,
            "turn_protocol_basis": "Supplied fixture protocol; internal Skill injection is not an external clarification.",
            "provider_aggregate": aggregate, "summary_reported_usage": summary_usage,
            "provider_usage_evidence_status": "untrusted_incomplete_event_stream" if malformed else "complete_session_aggregate" if complete else "unknown_aggregate_scope",
            "summary_usage_matches_raw_aggregate": aggregate == summary_usage if aggregate is not None and summary_usage is not None else None,
            "complete_session_aggregate_observed": complete, "provider_token_total_once": aggregate_total,
            "reported_cli_cost_usd_not_invoice": number(final.get("total_cost_usd")),
            "model_usage_entries_not_added": len(model_usage) if isinstance(model_usage, dict) else None,
            "models_reported_in_cli_aggregate": [model for model in (identifier(key) for key in model_usage) if model] if isinstance(model_usage, dict) else None,
            "usage_crosscheck": crosscheck, "session_key_sha256": session_key,
            "session_id_observed": session_id is not None, "malformed_event_lines": malformed, "warnings": warnings}


def aggregate_runs(rows):
    sessions = defaultdict(list)
    for row in rows:
        sessions[row["session_key_sha256"]].append(row)
    for copies in sessions.values():
        signatures = {json.dumps([row["provider_aggregate"], row["complete_session_aggregate_observed"]], sort_keys=True) for row in copies}
        for index, row in enumerate(copies):
            row["usage_counting"] = "excluded_conflicting_session_receipts" if len(signatures) > 1 else "excluded_duplicate_session" if index else "counted" if row["complete_session_aggregate_observed"] else "unknown_incomplete_aggregate"
    buckets = defaultdict(list)
    for row in rows:
        buckets[(row["group"], row["host"])].append(row)
    result = []
    for (group, host), members in sorted(buckets.items()):
        included = [row for row in members if row["usage_counting"] == "counted"]
        fields = CLAUDE_FIELDS if host == "claude" else CODEX_FIELDS
        result.append({"group": group, "host": host, "receipt_count": len(members), "sessions_counted_once": len(included),
                       "excluded_or_unknown_receipts": len(members) - len(included),
                       "provider_usage_sums": {key: sum(row["provider_aggregate"][key] for row in included if row["provider_aggregate"].get(key) is not None) if any(row["provider_aggregate"].get(key) is not None for row in included) else None for key in fields},
                       "provider_token_total_once": sum(row["provider_token_total_once"] for row in included) if included else None,
                       "session_elapsed_seconds_sum_not_project_wall_time": sum(row["elapsed_seconds"] for row in included if row["elapsed_seconds"] is not None) if included else None})
    return result


def comparisons(rows):
    result = []
    for baseline in [row for row in rows if row["group"] == "baseline"]:
        candidates = [row for row in rows if row["group"] in ("current", "history") and row["host"] == baseline["host"] and row["skill"] == baseline["skill"] and row["case"] == baseline["case"] and row["observed_model"] is not None and row["observed_model"] == baseline["observed_model"]]
        candidate = max(candidates, key=lambda row: (row["group"] == "current", row["started_at"] or "", row["run_id"])) if candidates else None
        result.append({"baseline_run_id": baseline["run_id"], "candidate_run_id": candidate["run_id"] if candidate else None,
                       "same_observed_model": candidate is not None, "observed_model": baseline["observed_model"],
                       "candidate_matches_current_source": candidate["group"] == "current" if candidate else None,
                       "candidate_source_sha256": candidate["source_sha256"] if candidate else None,
                       "selection_basis": "Prefer current source; otherwise latest captured same-model normal, explicitly historical.",
                       "baseline": {key: baseline[key] for key in ("provider_aggregate", "provider_token_total_once", "prompt", "final_output", "elapsed_seconds", "settings", "cli_version", "controller_sha256")},
                       "candidate": {key: candidate[key] for key in ("provider_aggregate", "provider_token_total_once", "prompt", "final_output", "elapsed_seconds", "settings", "cli_version", "controller_sha256")} if candidate else None,
                       "interpretation": "Descriptive only. Skills add default structure and, for bilingual replies, a second output language. Workloads, caches and hidden host context need not be equivalent. No savings or behavior grade is inferred."})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        runs_root = args.runs_dir.resolve(strict=True)
        if not runs_root.is_dir():
            raise InputError("runs_root_not_directory")
        encoding = offline_tokenizer()
        reader = Reader([ROOT, runs_root])
        sources = measure_sources(reader, encoding)
        hashes = {item["slug"]: item["source_sha256"] for item in sources}
        summaries = [path for path in inventory(runs_root, 10000, SLUGS) if path.name == "summary.json"]
        if len(summaries) > MAX_RUNS:
            raise InputError("run_limit_exceeded")
        if args.output.resolve() in {path.parent / filename for path in summaries for filename in ("summary.json", "launch.json", "prompt.txt", "output.txt", "events.jsonl")}:
            raise InputError("output_would_overwrite_receipt")
        rows = [measure_run(path.parent, runs_root, hashes, reader, encoding) for path in summaries]
        totals = aggregate_runs(rows)
        result = {"schema_version": "1.0", "measured_at_utc": datetime.now(timezone.utc).isoformat(),
                  "measurement_method": {"tokenizer": "tiktoken", "tokenizer_version": version("tiktoken"), "encoding": "o200k_base", "yaml_version": version("PyYAML"),
                                         "discovery_serialization": "name + newline + description, without YAML keys or delimiters",
                                         "word_method": "Python str.split whitespace words", "characters": "Unicode code points", "network": "No network; cached tokenizer data only",
                                         "usage_scope": "Captured native CLI runtime only. Author and reviewer usage is unavailable.",
                                         "admitted_cohort": list(SLUGS),
                                         "cohort_scope": "Only admitted skill cores and host/admitted-skill receipt directories are measured. Excluded skill directories are pruned before receipt reads and aggregation.",
                                         "usage_rules": "Claude input/cache-write/cache-read are distinct. Codex cached input and reasoning output are subsets, not additions. ModelUsage and per-message usage are not added to CLI aggregate totals.",
                                         "unknowns": "null means unobserved or unavailable, never assumed zero",
                                         "observed_text_scope": "Prompt/final-output files and visible tool/injection text only. Hidden host context and separately supplied material were not instrumented. Text counts are not provider billing counts."},
                  "limits": {"max_runs": MAX_RUNS, "max_input_file_bytes": MAX_FILE, "max_total_input_bytes": MAX_TOTAL, "actual_input_bytes": reader.bytes_read},
                  "sources": sources, "runs": rows, "totals_by_group_and_host": totals,
                  "same_model_baseline_comparisons": comparisons(rows)}
        if args.output.resolve() in reader.cache or args.output.resolve() == Path(__file__).resolve():
            raise InputError("output_would_overwrite_measurement_input")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
        print(json.dumps({"sources": len(sources), "runs": len(rows), "groups": dict(Counter(row["group"] for row in rows)), "baseline_pairs": len(result["same_model_baseline_comparisons"]), "input_bytes": reader.bytes_read}))
    except (InputError, OSError, ValueError, UnicodeError, RecursionError, yaml.YAMLError) as error:
        print("Measurement stopped: " + (str(error) if isinstance(error, InputError) else type(error).__name__), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
