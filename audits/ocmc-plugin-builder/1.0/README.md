# OCMC Plugin Builder 1.0 review

Reviewed on November 18, 2026, by a non-author reviewer using Skill Audit 1.0. The complete eight-file package is bound to source commit `3ff0fb635f45b6fa840907c7962dd0e0c1e0ad17`. The public package uses the collection MIT license.

| Category | Result | Evidence |
| --- | --- | --- |
| Prompt injection | Passed | The written boundary treats retrieved documentation as data. The synthetic case withheld the marker and made zero tool calls. |
| Security and privacy | Passed | Full source review found no personal information, account settings, or credential literals. The package contains Markdown files. Native fixture inventories stayed identical. |
| Reliability | Passed | Independent grading accepted both in-scope Codex outputs. A separate fictional server passed four Inspector checks. |
| Platform verification | Passed with warnings | Codex CLI 0.169.0 discovered the project skill. Two explicit invocations returned exact source text. A same-name control returned different text that matched its own source. The stream omitted a dedicated load event and backend model. |

The verified execution scope is Codex CLI with the complete folder installed in a project. The two cases covered read-only tool planning with a text fallback and the treatment of untrusted documentation during an uncertain write. The same-name control used an identical prompt. Offline inventory also confirmed zero OCMC entries in an absent-skill project. No recorded model tool calls or fixture edits occurred.

The Claude Code 2.1.325 startup listed the package. An expired login stopped activation and inference. The listing provides reference guides for Claude and other integration targets and marks their execution separately. Live OAuth, connector registration, widget rendering, and provider policy enforcement require separate checks.

Codex reported an unrecognized retry-count setting. The controller set a 120-second wall-clock limit and disabled unbounded connection retries. The results support the observed fixture behavior and make no transport retry-count claim.

The Inspector rerun tested stdio and loopback HTTP discovery, one valid call, and one invalid call against a fictional catalogue server. This provides protocol-level evidence for that separate fixture.

- [Independent static review](static-review.md)
- [Redacted native receipts](native-evidence.json)
- [Local Inspector results](inspector-rerun.txt)
- [Exact manifest and bilingual catalogue evidence](report.json)
- [Pinned auditing skill](https://github.com/iacompa/skills/tree/eb254e0b5d60abaa8f3b243ec7cc102dbcdac512/skills/skill-audit)
- [Auditor evaluation](../../skill-audit/1.0/README.md#evaluation-scope)
