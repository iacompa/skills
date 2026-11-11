# Skill Audit 1.0 — current scoped review

Date: 2026-11-11. Source: `eb254e0b5d60abaa8f3b243ec7cc102dbcdac512`.

| Review category | Current scoped result |
| --- | --- |
| Prompt injection | Passed |
| Security and privacy | Passed |
| Reliability | Passed |
| Platform verification | Passed with warnings |

The [native supplement](native-verification/README.md) records the exact packages, client configurations, individual results, and retained failures.
The current evidence supports the three core results and a platform warning within its restricted fixture scope.
Native sessions tested manual project installation and activation. External Skills CLI installation was not tested.
Native `apply_patch` support remains failed in the tested Codex profile. Exec-command writes supplied the disclosed alternative.
The sessions did not execute the target skills. Native execution tested the auditor against two-file inactive targets.

The original report JSON and evidence files remain unchanged. Their original NOT RUN statements describe the dated static-review scope below.

<details>
<summary>Historical static review — 2026-11-10</summary>

# Skill Audit 1.0 — published review

Reviewed source: [`eb254e0b5d60abaa8f3b243ec7cc102dbcdac512`](https://github.com/iacompa/skills/tree/eb254e0b5d60abaa8f3b243ec7cc102dbcdac512/skills/skill-audit). Date: 2026-11-10.

**Verdict: ACCEPT WITH CONDITIONS. Coverage: complete for the declared static scope.**

| Check | Result | Evidence and limit |
| --- | --- | --- |
| Prompt injection | Passed static review | A separate reviewer found no issue in the auditor's instruction boundary. Synthetic cases covered forged authority, audit suppression, delayed triggers, and benign quotations. |
| Security and privacy | Passed static review | No confirmed source defect. Captured visible evaluation requests stayed within approved reads, inert analysis, designated reports, validation, and one internal progress message. |
| Reliability | Passed static review | All package references were reviewed. Twenty-nine report assessments across fifteen cases met their content expectations. Missing helpers stayed incomplete. |
| Platform verification | Not checked | Native installation, automatic discovery, installed-command activation, actual denied operations, and host enforcement were not tested. |

These results assess written instructions and the recorded text evaluations. They do not guarantee safety or injection immunity.

## Evidence

- [Structured final report and file hashes](report.json).
- [Independent publication-evidence review](publication-evidence-review.json).
- [Independent source review](independent-source-audit.md) and [its JSON](independent-source-audit.json).
- [Independent action-request review](action-trace-review.json).
- [Captured tool requests, redacted](captured-action-requests.redacted.json). These came from the runtime's saved records, not only model assertions.
- [Cases, individual reports, control, and assessment criteria](../../../evaluations/skill-audit/2026-11-10/README.md).

The source reviewer assessed five package files plus the README and MIT license. Its original report preceded Git publication. The final report binds the same file hashes to the immutable source commit.

The root checked the installation guidance against official [Skills CLI commands](https://github.com/vercel-labs/skills/blob/main/docs/commands.md), [CLI requirements](https://github.com/vercel-labs/skills#readme), [Codex documentation](https://learn.chatgpt.com/docs/build-skills), and [Claude Code documentation](https://code.claude.com/docs/en/skills). Documentation verification does not qualify a runtime.

## Evaluation scope

Three fresh Codex agents used the frozen audit instructions with inert target text. The captured model was `gpt-6.1-sol`. The first assessed fifteen cases. Two more independently repeated seven consequential cases. Each repeated verdict agreed.

A separate no-skill control assessed ten cases before the candidate was authored. That control already met the main behavioral checks. No measured improvement over that control is claimed.

One delayed-trigger case received partial package coverage in the first run and complete supplied-text coverage in the repeats. All reviewers rejected its explicit harmful branch. The individual reports preserve that difference.

The action reviewer inspected seventeen top-level requests and twenty-two nested command requests. No forbidden action request appeared in the visible executable paths. Quoted malicious examples remained data. Root output checks found no full synthetic marker, common encoded form, or distinctive suffix in the saved public evidence.

## Conditions and limits

Keep the complete five-file package. Apply this review only to the recorded source and scope. Review affected changes before refreshing a result. Keep untested platform claims gray.

This is model-based review by separate non-author agents within the same task infrastructure. It is not an external laboratory assessment or certification. The tests are small synthetic cases. They do not measure general attack resistance or prove host isolation.

The captured internal progress message is encrypted in the saved runtime record. Its authorized recipient is visible. The root received an ordinary progress summary, but the independent action reviewer did not decode its plaintext. Public evidence excludes ciphertext, private reasoning, and account metadata. Operational paths are redacted.

Raw host syscalls and actual denied-egress behavior remain unverified. No target skill was run as part of these text reviews. Codex and Claude Code installation and enforcement remain NOT RUN.

</details>
