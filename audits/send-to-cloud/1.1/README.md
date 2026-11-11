# Send to Cloud 1.1 — reviewed source and native scope

Date: 2026-11-11. Source: `75e25b7a96bb7414b63321ab581ef4de6b3578d6`.

| Review category | Result within the declared scope |
| --- | --- |
| Prompt injection | Passed |
| Security and privacy | Passed |
| Reliability | Passed with warnings |
| Platform verification | Passed with warnings |

Complete static review and the [native supplement](native-verification/README.md) support these reduced-scope results.
Independent review accepted twelve actual behavior sessions: eight Claude Code and four Codex CLI sessions.
Two additional Codex attempts failed during initialization before model telemetry. They remain INCONCLUSIVE, with no activation or behavioral pass inferred.
The owner ended the run before four planned Codex cases started. The original sixteen-case matrix is not complete.

**Reliability warning:** Codex private-history r1–r3 and requested-failed-optional r1 are NOT RUN.
N5-F5 is not fully resolved for these current-source Codex affected paths. The report does not claim full native source conformance or complete repair.
The [Version 1.0 history](../1.0/native-verification/README.md) retains its Medium reliability finding and all five failed optional-count gates.

All four Codex cases and seven default Claude cases executed zero optional validators.
Claude's requested case started one optional validator, retained its explicit exit 2, and ran no later optional validator.
A real baseline mandate separately required `git fsck --no-reflogs`. Native execution succeeded, and the handoff recorded both results.
The omitted Codex paths remain unqualified.

**Platform warning:** manual project installation, restricted hosts, and local bare remotes define the tested scope.
External Skills CLI installation was NOT RUN. Earlier native patch capability failures remain failed. restricted exec-command writes worked.
Claude's hosted-URL placeholders are blocked-recovery templates, not READY consumer prompts. Local checkpoints do not establish hosted Cloud readiness.
The prior [actual Cloud continuation](../../native-verification/2026-11-11/README.md) used a Version 1.0 checkpoint. It is not a fresh 1.1 end-to-end run.

The [structured report](report.json) binds the source and categories. The [native JSON](native-verification/report.json) retains individual results, omissions, and limits.
The entrypoint contains 749 words. Its conditional reference contains 332 words. These whitespace counts are not performance measurements.
The [owner decision](../../native-verification/2026-11-11/owner-decision.json) records publication signoff separately from measured results.
