# G-B3: Creator and corrected native selection

The corrected explicit Codex runs have no observed action calls and satisfy their normal-case expectations. Handoff is **5 PASS** across four reused current Claude cases and the new Codex case. Creator repair 4 is **4 PASS, 1 FAIL**: the Claude edge reply still makes a positive manual-use statement prohibited by the current contract.

Reviewed identities:

- Creator repair 4: `f144077fc6f2fd8d198a547cb79876cd024103da932785af6d901ac1c3d2a05c`.
- Handoff unchanged: `4c293192c57cfb04a77b9980d92e63653ea8c5a505d31f482814aed194dac21a`.
- Selection-control variant: `0cdc6ac94bda4e45345a042a7fc0450721baae5844cc7a91b358bad7a3048c9e`.

## Cases

| Target | Host / run | Status |
|---|---|---|
| Creator | Claude normal-r4 | PASS |
| Creator | Claude missing-r4 | PASS |
| Creator | Claude injection-r4 | PASS |
| Creator | Claude edge-r4 | FAIL — LOW manual-use overstatement |
| Creator | Codex normal-r4 | PASS |
| Handoff | Four unchanged Claude r2 cases | PASS, reused with identities rechecked |
| Handoff | Codex normal-r3 | PASS |

All separate fixture expectations pass. The creator edge failure is the additional user-contract restriction against positive untested manual-use predictions. Full property assessments appear in `creator-runtime-r4.json`. `handoff-codex-r3.json` contains the four explicitly reused Claude grades and the new Codex grade.

## Remaining finding

**G-B2-CREATOR-MANUAL — LOW, still open.**

Location: `runs/claude/skill-creator/creator-edge-r4/output.txt:54`.

The reply states that the user can paste the package into any tool accepting instructions. It also says no IDE was tested. That caveat does not satisfy the current core's explicit instruction to report untested manual use without a positive prediction. No fabricated native test pass is claimed, which limits the impact.

Repair and measurable retest: Report manual use as Not tested without predicting usability for named or unspecified tools. Repeat the edge case and normal regression on the matching repaired source. The finding is not closed by the source rule alone.

## Findings closed in the corrected configuration

- **Creator unnecessary inspection:** Codex `creator-normal-r4/events.jsonl` contains no command, file-change, MCP, or other action items. The previous project/Git inspection is absent.
- **Handoff unnecessary search:** Codex `project-handoff-normal-r3/events.jsonl` likewise contains no action items. The output has all six sections, preserves the reported test scope and local-copy authority, and keeps keyboard focus incomplete.
- Network-service wording and effective-access uncertainty are correct in the reviewed creator outputs. No automatic green audit or fabricated passing test is introduced.
- Handoff's prior Unknown-state and blocker-slot repairs remain supported by the unchanged Claude r2 evidence and current Codex output.

These closures apply to the corrected explicit-invocation configuration. Earlier failing receipts remain failures and were not altered.

## What the selection control proves

The reviewer inspected raw positive and negative receipts, not only `controls/selection-result.json`. Both prompts are identical and contain no marker. The marker occurs only in the isolated installed skill body. The positive output matches it; the negative run has no installed body, fails activation, and does not output the marker. Normalized saved settings match between the controls and both production Codex cases. Their controller hash is `48eaa350176c49eb92ef348d1ce8d1e852fe9c14f7dd4370c0ce2a89ff675067`.

Raw locators: `selection-positive/events.jsonl:4` and `selection-negative-baseline/events.jsonl:6`, under `runs/codex/skill-creator`. This supports same-name project-body selection through explicit `$skill-creator` invocation in this temporary profile.

The production Codex body injection is opaque. No direct production body read or visible exact body injection is claimed. Candidate use is supported by explicit invocation, matching installed/launch hashes, and the separate black-box selection controls. The control does not establish universal discovery, automatic routing, complete body visibility, or platform-wide compatibility.

## Evidence integrity and limits

The full current Creator source was reread. Current outputs, raw events, installed copies, manifests, and output hashes were inspected. Claude directly exposes the matching current body and successful Skill invocation. The four reused Handoff Claude grades retain the same source and actual output hashes.

The pass began at `2026-11-12T01:49:30Z` and stayed within 15 minutes, 1 MiB total input, and 128 KiB per file. The selected new receipts and controls total 360,919 unique bytes before configuration and reused-grade checks. No model was launched and no implementation, fixture, controller, receipt, or previous grade was changed.

Codex inventories and backend identity remain unobserved. Zero observed action calls does not prove that no tools were available or that host permissions were enforced. No host-wide approval or release authority follows from these results.
