# Collection measurement method

Run the development tool with the existing private measurement environment:

```sh
/private/tmp/iac-skill-collection-20261111/venv/bin/python scripts/summarize-collection.py --runs-dir /private/tmp/iac-skill-collection-20261111/runs --output /private/tmp/iac-skill-collection-20261111/metrics/collection-admitted-six.json
```

The tool requires the already installed tiktoken and PyYAML packages. It does not install production dependencies, launch models, import target code, or contact a service. Tokenizer vocabulary must already be cached. Its offline cache reader verifies the vocabulary hash without fetching or repairing files.

## Static sizes

The six admitted cores are five collection skills and Skill Creator: Bilingual Business Reply, Agent Permissions Audit, Lead Follow-Up, Review Response, Project Handoff and Skill Creator. AI Readiness Audit is excluded from this cohort. Each complete `SKILL.md` measurement includes its frontmatter. Discovery metadata is serialized as the name value, one newline, and the description value. It excludes YAML keys and delimiters. Character counts use Unicode code points. Word counts use Python whitespace splitting. Byte counts and SHA-256 values use the unchanged UTF-8 bytes. Token counts use the named `o200k_base` encoding and the reported tiktoken version; they are not model-independent usage or billing totals.

Optional reference inventories report package-relative paths, hashes, and independent sizes. Inventory does not mean a reference was loaded in a model run. That runtime field remains unknown.

## Captured runtime scope

Only directories under `runs/<host>/<admitted-skill>/` enter receipt inventory. Other skill directories are pruned before receipt content is read or aggregated. Historical, baseline and control groups are included only within this admitted cohort. Earlier private all-skill reports remain historical artifacts and are not rewritten.

Each admitted run reads only `summary.json`, `launch.json`, `prompt.txt`, `output.txt`, and `events.jsonl`. The output contains relative run IDs, counts, hashes, selected settings and numeric usage. It contains no raw prompt, response, command argument, tool-result text, environment value, or credential. Structured JSON and YAML are inert data. Symlinks and nonordinary files within measured input are rejected.

Limits are 500 runs, 512 KiB per measured input file, and 25 MiB of measured source/receipt input. Directory inventory is also bounded. Installed tokenizer/package data is a trusted development dependency, not a measured receipt. Missing fields become null. Malformed event lines are counted, not silently reported as complete coverage. A limit failure stops without producing a misleading partial total.

Current, historical, baseline and control runs remain separate. A matching source hash is a recorded identity, not proof of body observation or behavior. Manual `-rN` repair labels are recorded separately from automatic retries and do not redefine any defect budget. The supplied fixture protocol has one external user turn, no follow-up replies, and no automatic retries. Internal Skill injection is not clarification. The number of questions an assistant asked remains unknown; completed extra clarification turns are zero under that protocol.

## Aggregate usage

Use the final Claude CLI result usage or the single Codex `turn.completed` usage record as the session aggregate. Summary copies are cross-checked, not added again. Any malformed event line makes aggregate scope incomplete for either host because it could hide another turn or final result. Visible usage counters remain explicitly untrusted metadata and are excluded from complete-session totals. Missing or otherwise ambiguous aggregate scope also remains unknown. Duplicate session identities are counted once; conflicting copies are excluded. Session durations are reported as captured. Their sum is session-seconds, not project wall time.

- Claude ordinary input, cache-creation input and cache-read input are distinct categories. The once-only token total adds those categories and output.
- Codex input already includes cached input. Its once-only total adds input and output. Cached input and reasoning output remain subset counters and are not added again. Cache-write counters remain reported metadata without an assumed additive billing interpretation.
- `modelUsage`, nested cache breakdowns, thinking breakdowns and assistant-message usage do not enter the aggregate again. Any CLI cost is labeled as reported CLI cost, not an invoice.

Claude assistant records are deduplicated by message ID for a diagnostic cross-check. Stream message output usage can be partial. Therefore a mismatch does not replace the final CLI aggregate. Codex has no comparable per-message usage in these captures. Observed tool calls are deduplicated by tool/action ID; lifecycle events are not separate calls. Tool-result and internal injection text counts describe visible text blocks only. They are not added to provider usage.

## Comparisons and limits

Each admitted ordinary baseline session is paired on the same host and observed model. The final six-skill cohort has two such pairs; the Readiness pair is excluded with that skill. A current-source normal run is preferred. If it is not yet captured, use the latest captured historical normal and explicitly report its hash and noncurrent status. If no same-model normal exists, the candidate is null. Settings are shown rather than assumed identical. The comparisons are descriptive: the candidate may add structure, checks or a second output language. Cache state, host context, controller revisions and output workload can differ. A historical comparison is not a measurement of the current source. The tool makes no savings claim and grades no behavior.

Only captured native runtime usage is measured. Authoring, reviewing, orchestration, uncaptured attempts, provider-hidden context and actual billing are unavailable. Do not present these totals as the full development cost or efficiency of the collection.
