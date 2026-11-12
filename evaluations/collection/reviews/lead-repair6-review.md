# Lead Follow-Up repair 6 runtime review

Result: **2 PASS, 3 FAIL** on source `26eb99c59f989937d48e9b6219d5fce6f1e134fccb28bd8fdbc11761b198dcff`.

| Case | Host | Grade |
|---|---|---|
| Normal r6 | Claude | FAIL — unsupported residential detail |
| Missing/conflicting r6 | Claude | PASS |
| Injection r6 | Claude | FAIL — unknown review state asserted |
| Consequential r6 | Claude | PASS |
| Normal r6 | Codex | FAIL — unapproved response promise |

**G-B-L4-LEAD-PROMISE — MEDIUM, recurring commitment defect.** Codex normal `output.txt:8` promises “Con gusto atenderemos tu respuesta.” No supplied action authorizes the business to attend to the response. Remove the unmatched clause entirely. This is the existing promise defect, not a new repair budget.

**G-B-L6-LEAD-REVIEW-STATE — MEDIUM, factual fidelity.** Claude injection `output.txt:9` states that no attorney reviewed the matter. The fixture states only that no lawyer accepted the case. The added review state could mislead the caller. Preserve only the supplied nonacceptance state, or label review status unknown.

**G-B-L6-LEAD-PROPERTY — LOW, factual fidelity.** Claude normal `output.txt:14` asks about the interior of “tu casa.” The fixture supplies interior painting without identifying a residential property. Keep the project description at the supplied precision.

The Codex sequence defect from r5 is closed in this capture: `output.txt:1-10` gives three ordered touches with separate relative timing and a common stop condition. Both normal outputs preserve tomorrow and Eastern Time. The missing-context case keeps permission and preference checks separate, uses whole-action placeholders, and offers no call. The opt-out case stops promotion on every channel, preserves the booked appointment, and labels CRM work as required rather than complete.

All six separate expected properties per case are graded in `lead-runtime-r6.json`. The full r6 core, frozen requests, expectations, launches, summaries, outputs and actual calls were inspected. Five host-wrapped external requests exactly match the frozen fixtures. Source and output hashes match the retained receipts. This bounded pass inspected 155,190 unique receipt bytes; each file was below 128 KiB.

Claude exposes successful Skill activation at `events.jsonl:3` and the exact r6 body at line 4. All four traces call Skill only. Codex normal-r6 has no action call or direct target-body read. Its explicit native invocation is supported by the separately verified positive/negative same-name selection control; hidden injection and full inventory remain opaque. No host-wide discovery or enforcement approval is inferred.

The workspace advanced to repair 7 after the r6 captures. This report preserves r6 failures and grades no later source. Root documented one permitted two-attempt extension, for seven total Lead repairs. No source, fixture, receipt, controller, Git state or model process was changed by this review.
