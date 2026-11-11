# Send to Cloud 1.0 — published review

Reviewed source: [`eb93857dfe0b9d5132ed3f0b52ea88ca008f87ed`](https://github.com/iacompa/skills/tree/eb93857dfe0b9d5132ed3f0b52ea88ca008f87ed/skills/send-to-cloud). Review date: 2026-11-10.

**Verdict: ACCEPT WITH CONDITIONS. Coverage: complete for the declared static scope.**

| Check | Result | Evidence and limit |
| --- | --- | --- |
| Prompt injection | Passed static review | Repository and tool text cannot authorize new actions or replace the user's cloud choice. Synthetic traces retained this boundary. |
| Security and privacy | Passed static review | No confirmed source defect. Written gates cover private history, tracked secrets, actual push destinations, visibility, and separate action scope. |
| Reliability | Passed static review | Both package files and distribution context were reviewed. Twenty static assessments retained stop/recovery guards. Four nonblocking implementation uncertainties remain recorded. |
| Platform verification | Not checked | Native installation, discovery, host enforcement, real Git handoff, and cloud execution were not tested. |

These results assess written instructions and synthetic predictions. They do not guarantee safety or transfer success.

## Evidence and identity

- [Final report and source binding](report.json).
- [Independent nine-section source audit](independent-source-audit.md) and [JSON](independent-source-audit.json).
- [Frozen four-file manifest](candidate-manifest.json). The root verified every hash against the source commit above.
- [Static cases, twenty assessments, criteria, and retained observations](../../../evaluations/send-to-cloud/2026-11-10/README.md).
- [Captured visible action requests, redacted](captured-action-requests.redacted.json). These came from saved runtime records rather than evaluator assertions alone.

The independent audit preceded Git publication. Its original Markdown and JSON are retained byte-for-byte. Their temporary paths identify the original inspection roots; the manifest and source binding establish the public identity.
The source commit contains two installed Markdown files, the reviewed root README, and the unchanged MIT license. The report is published in a later commit to avoid self-referential identity.

## Auditor evidence and provenance

The trusted Skill Audit 1.0 procedure is unchanged at [`eb254e0b5d60abaa8f3b243ec7cc102dbcdac512`](https://github.com/iacompa/skills/tree/eb254e0b5d60abaa8f3b243ec7cc102dbcdac512/skills/skill-audit).
Its separately reviewed [adversarial evaluation and captured-request evidence](https://github.com/iacompa/skills/blob/b7c2b8532b44466d96304e4ab3dfd938c146ab29/audits/skill-audit/1.0/README.md) remains the auditor-evaluation basis. This release does not claim a new adversarial runtime suite.
This candidate received a separate non-author source audit and three fresh static evaluation sessions. The model recorded for those sessions was `gpt-6.1-sol`.
Visible requests were captured for independent review. Internal progress-message bodies are encrypted in saved records and omitted; recipients remain visible. Host syscalls and actual denied-egress behavior were not captured.

The root checked the README's external installation guidance against official [Skills CLI commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [CLI runtime requirements](https://github.com/vercel-labs/skills#readme), and [Claude Code skill documentation](https://code.claude.com/docs/en/skills). Existing Codex paths retain the previously checked [official guidance](https://learn.chatgpt.com/docs/build-skills). Documentation checks do not establish runtime qualification.

## Concision and conditions

The owner draft contained 6,832 words. The default entrypoint contains 645 words, a 90.6% reduction. Its one conditional reference contains 332 words; the complete installed package is 977 words, an 85.7% reduction. These are whitespace word counts, not measured token counts or timing benchmarks.
Optional validation allows one relevant command within 30 seconds. Required project and host gates take precedence; a complete handoff is not promised within 30 seconds.

Retain this identity and the runtime limits. Reassess affected changes. The mixed-index, platform-prerequisite, concurrent-branch, and recovery-format observations remain visible in the evaluation records. No known blocking defect was waived.
Model-based review within the same task infrastructure is not an external certification. Native Codex and Claude Code activation, actual handoff operations, permission enforcement, and cloud launch remain NOT RUN.
