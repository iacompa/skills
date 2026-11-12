# R-B: Skill Creator and controller review

Status: Changes requested. This review found two material defects. No source files were changed.

## Revision and scope

- Repository base: `0644690a0e1230f7314ff6469adc6eb76159b819`.
- Candidate: `skills/skill-creator/SKILL.md`, SHA-256 `70775226d276e9ea391f9e532eb0aef84ff122fcc411752daaa470e8aa9d33ff`.
- Controller: `/private/tmp/iac-skill-collection-20261111/evaluate.py`, SHA-256 `61cf630062e70f8ef2aced0b21b65264aa7456f8894fc78550adcdaa4a166d14`.
- Observed run: `/private/tmp/iac-skill-collection-20261111/runs/claude/skill-creator/creator-normal`.
- The candidate and controller hashes match that run's launch manifest.
- Reviewed the applicable collection brief, creator fixtures and expectations, source, controller, controls, output, and relevant raw events.
- This was one review pass. The reviewer did not launch models, edit implementation files, or delegate work.

## Findings

### P2: Generated workflow promises staff actions without supplied approval

Location: `/private/tmp/iac-skill-collection-20261111/runs/claude/skill-creator/creator-normal/output.txt:30` and `:32`.

Evidence: The generated skill instructs replies to say that staff will confirm availability or follow up. The request authorizes FAQ drafts. It supplies no staff follow-up commitment. The generated evaluation plan repeats the unsupported follow-up expectation at line 71. This conflicts with the creator's instruction against invented promises at `skills/skill-creator/SKILL.md:34`.

Impact: A standard missing-information or availability question can produce an unauthorized customer-facing commitment. The generated test plan would reward that defect.

Requested repair: Require generated workflows to preserve the distinction between requesting staff review and promising staff action. Permit a commitment only when supplied approved facts support it. Add an observable expectation for unsupported follow-up promises. Preserve this actual output before repair, then rerun the affected creator case and a relevant regression case.

### P2: Controller omits native Codex activity from its call evidence

Location: `/private/tmp/iac-skill-collection-20261111/evaluate.py:85` through `:87`, with the resulting `calls` field at line 95.

Evidence: The parser inspects only `message.content` blocks of type `tool_use`. Native Codex events place actions under `item`, including `command_execution` and `file_change`. A retained native event sample demonstrates this shape at `/private/tmp/iac-native-platform-20261110/runs/codex/frozen-behavior-receipts-22/receipts/codex-checkpoint-simple-r1-70c7686ff4/native/events.jsonl:4`. Applying the controller's parser to that file returned zero calls despite 42 command-execution events and four file-change events. These counts include lifecycle events, not distinct actions.

Impact: A Codex summary can show an empty call list while the run reads source files, executes commands, or changes files. That field cannot establish source application, unnecessary tool use, or compliance with the intended action scope. Raw events remain available, so the evidence is recoverable.

Requested repair: Parse the native Codex item events and deduplicate lifecycle events by action ID. Record source-use evidence separately from native discovery. Keep unknown or unobserved inventories explicit. Do not interpret an empty call list as proof of no activity. Check the revised parser against retained events before broad Codex runs.

## Native test limits

The observed Claude initialization reports `skills=[]` at `events.jsonl:1`. The Skill invocation fails with `Unknown skill: skill-creator` at line 3. A Read call loads the exact candidate path at lines 8–9. The final output explicitly discloses this fallback.

This run supports explicit file-use evidence for this candidate. It does not establish successful native discovery or native Skill invocation. It does not establish automatic routing, universal compatibility, or any Cursor behavior. The controller's `mode: native` names the requested mode. Its `CAPTURED` status is a capture status, not a behavioral pass.

## Source and telemetry assessment

The creator keeps the standard workflow in one file. It covers portable frontmatter, consequential actions, authority, missing facts, inert source instructions, evaluation separation, and honest compatibility statements. No required sibling skill, reference, or network resource appears in the source.

The observed output provides a complete core file and separate evaluation material. Its generated tests are marked Not run. Its host notes do not invent installation paths or claim native verification. These strengths do not resolve the unsupported commitments finding.

An offline `o200k_base` measurement reports 870 tokens for the complete creator source, including frontmatter. The frontmatter contents contain 34 tokens, excluding delimiters. The complete file contains 686 words and 4,802 characters. No creator-specific numeric target was supplied in the reviewed brief. The source has no optional references to load. These are static measurements, not task usage or billing measurements.

The run reports Claude model `claude-opus-5-5`. The raw provider usage includes 6 input tokens, 5,492 cache-creation input tokens, 7,230 cache-read input tokens, and 2,717 output tokens. The controller preserves those categories and the separate model-usage object. Do not add the overlapping model-usage fields again. These counts cover the observed run, including the failed invocation and subsequent file read. They do not measure only the candidate source.

## Verification and integration notes

- Read the source and raw events directly. The review does not rely on an author's completion claim.
- Compared the current candidate and controller SHA-256 values with the run manifest. Both matched.
- Reproduced the Codex event-parser omission with an existing raw event file. No inference ran.
- Measured static source size with the existing local tokenizer. Network connections were disabled in that measurement process.
- Changed only `evaluations/collection/reviews/creator-and-controller.md`.
- Root integration should preserve this review and failed output. Targeted re-review is required after repairs.
