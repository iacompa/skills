# RR-B: Targeted creator and controller re-review

Status: The controller finding is closed for the observed event types. Creator repair 1 fixes the observed unsupported promises. Creator repair 2 passes source review, but its behavior remains unapproved pending current-source runs.

## Reviewed revisions

- Repository base: `0644690a0e1230f7314ff6469adc6eb76159b819`.
- Current creator source: `skills/skill-creator/SKILL.md`, SHA-256 `77480e44f00d7023ef648e9ffd34a7d893d8c7d6731a00cd466275f7c9673ddd`.
- Creator repair-1 run source: `4f39e4e97f920895152f7c8160f9470427f197fc2a79bcdc719d6ff473237e0f`.
- Current controller: `/private/tmp/iac-skill-collection-20261111/evaluate.py`, SHA-256 `bed42dab06586da775397f8e8b4538db8818c6bfc29f7784fdcabacf666af32e`.
- Current creator frontmatter parses and has only `name` and `description`. The complete file measures 945 tokens with `o200k_base`.

This review inspected source, controls, manifests, installed source copies, actual outputs, and raw events. It did not launch models or edit implementation files.

## Finding disposition

### P2 unsupported downstream promises: fixed in the observed repair-1 output

The original output instructed replies to promise staff confirmation and follow-up at `runs/claude/skill-creator/creator-normal/output.txt:30` and `:32`. Its test plan repeated that expectation at line 71.

The repair-1 output now prohibits promises to confirm, call back, or follow up without a supporting source at `runs/claude/skill-creator/creator-normal-r1/output.txt:64`. The availability test at line 85 requires no callback or confirmation promise. The missing-information behavior uses omissions, placeholders, and internal notes instead. This addresses the observed defect.

The current creator carries the corresponding guard at `skills/skill-creator/SKILL.md:36`. That source change remains present in repair 2. Behavior evidence from repair 1 does not establish a pass for the changed repair-2 source. Repeat the affected case and a relevant regression on the current hash before final acceptance.

Both failed outputs remain preserved:

- Initial output SHA-256: `88fbeae59401aa8052b2d292a31a12e9b23cffea54f3a6e03d270c7cc488860e`.
- Repair-1 output SHA-256: `9a1b0f249e48397187ff309785b6c718f1756b2d7c520787f6caa79ee07b4703`.

### P2 unsupported host and enforcement claims: source repair present; behavior verification open

Location: `runs/claude/skill-creator/creator-normal-r1/output.txt:106`.

Evidence: The repair-1 output claims that manual pasting works in Codex, Claude Code, and Cursor. No tests of those generated-skill workflows support that statement. The same line describes the package as having no network access. A Markdown package does not establish host network enforcement.

Impact: A reader could mistake inferred portability and package contents for verified compatibility or enforced restrictions.

Current source repair: `skills/skill-creator/SKILL.md:50` explicitly prohibits named-host manual-paste claims without an actual test. It requires inferred compatibility to be labeled untested. It also separates package properties from host enforcement. This directly addresses both observed statements without changing the portable standard workflow.

Status: Open for behavior verification. No repair-2 output was used to approve this change. Source review alone cannot close this finding.

### P2 omitted Codex call evidence: closed for tested lifecycle events

The current controller handles native item events at `/private/tmp/iac-skill-collection-20261111/evaluate.py:95` through `:101`. It stores the latest event for each action ID, so a started/completed pair produces one call.

The reviewer extracted and executed that exact parser block against existing raw files. No model process ran.

| Raw event file | Lifecycle events | Distinct actions | Parsed calls | Result |
|---|---:|---:|---:|---|
| Current `runs/codex/project-handoff/project-handoff-normal/events.jsonl` | 4 | 2 | 2 commands | Pass |
| Retained `codex-checkpoint-simple-r1-70c7686ff4/native/events.jsonl` | 46 | 23 | 21 commands and 2 file changes | Pass |

The current captured summary matches the parser output exactly. Its two calls retain the successful source read and the auxiliary search that failed with exit 1. No lifecycle pair is counted twice. Other native item types listed in the parser were not exercised by these samples.

The current controller also writes its frozen launch source to `controller.py` at lines 7 and 44. The current Codex run's snapshot hash matches its launch manifest and the reviewed controller hash. The older Claude repair-1 run predates that snapshot mechanism and has no `controller.py`; its manifest, controls, source copy, and raw events remain available.

## Native activation and configuration evidence

Claude repair 1 now has direct native evidence:

- `runs/claude/skill-creator/creator-normal-r1/events.jsonl:1` lists only Read and Skill tools, the `skill-creator` skill, no plugins, and no MCP servers.
- Line 2 invokes the named Skill. Line 3 returns `Launching skill: skill-creator` without an error.
- Line 4 supplies the skill body, including the downstream-promise guard.
- The installed source copy hashes to the repair-1 manifest's source hash.

Its launch omits `--restricted`, uses project settings, and supplies strict empty MCP configuration. Its controls retain disabled hooks, disabled skill shell execution, denied write/exec/web tools, and restrictions on reads outside the working directories. The only exposed model tools are Read and Skill. Runtime writes remain permitted inside the synthetic temporary directory for the host process. This is not proof of zero host writes or a new adversarial permissions test.

The observed Codex run successfully reads `.agents/skills/project-handoff/SKILL.md` at `events.jsonl:4` through `:5`. The completed command output hashes to the installed candidate and manifest source hash, `6f1728983d3c3a5260dc267800d7a0ee457a99130d61c22f3e64ce7168a5c772`.

Codex controls disable network access for the sandbox, hooks, unrelated skills, apps, plugins, and the configured MCP integrations. Its synthetic workspace permits writes. The launch uses strict config, ignored user config and rules, no daemon, and an ephemeral session. The raw event stream does not emit a complete tool or skill inventory. Summary inventory and native-activation fields therefore remain null. The model identity is correctly labeled requested rather than backend-observed.

These runs establish the specific explicit activation or file-use evidence described above. They do not establish automatic routing, near-miss behavior, Cursor compatibility, or universal host support. A capture status remains separate from a behavioral pass.

## Required next evidence

Run the repaired creator cases on source hash `77480e44f00d7023ef648e9ffd34a7d893d8c7d6731a00cd466275f7c9673ddd`. Verify the absence of unsupported staff commitments, untested host claims, and implied host enforcement. Preserve the actual outputs and classify each case separately. This review authorizes no additional side effects.

Only `evaluations/collection/reviews/creator-and-controller-rereview.md` changed during this pass.
