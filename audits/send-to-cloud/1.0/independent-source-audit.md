# Skill Audit Report

## 1. Decision

- Target and supplied version: **Send to Cloud 1.0**.
- Reviewed identity: the four-file manifest at `/private/tmp/iac-send-cloud-release-20261110/candidate-manifest.json`. Its SHA-256 is `50f5607921cbdae42b4688cc418faa8088ae90ca623f37119fbdfae026cec83b`. All four entries matched independently calculated hashes.
- Verdict: **ACCEPT WITH CONDITIONS** for the declared static scope.
- Coverage: **COMPLETE FOR DECLARED SCOPE**.
- Overall confidence: **HIGH** for the text, inventory, and identity conclusions. Actual model behavior and host enforcement remain unverified.
- Proposed use: a concise Git checkpoint and continuation-prompt skill. The skill asks for an unspecified cloud destination before mutation.
- Exact conclusion scope: the complete `skills/send-to-cloud` directory, root `README.md`, and root `LICENSE` at the hashes below. This conclusion does not approve execution, installation, publication, or a cloud launch.
- Main reason: no supported security, privacy, injection, or reliability defect was identified. The instructions preserve explicit holds, inspect publication scope, verify the remote SHA, and separate four completion states.
- Conditions: retain the reviewed identity or reassess changes. Preserve the runtime limitations in public claims. Obtain the actual user's required action scope before committing, pushing, or launching. Publication requires separate owner authorization and the repository's remaining evidence gates.
- Runtime testing: **NOT RUN**. Native Codex activation, native Claude Code activation, permission enforcement, real Git handoff, and cloud execution were not tested.
- Audit author and independence: native Codex subagent `/root/send_cloud_audit`, a separate reviewer. This reviewer did not author or edit the candidate. The review is a model-based static assessment within the same orchestration task.
- Review date: 2026-11-10 America/New_York. The clock reading before report creation was 2026-11-11 00:52:34 UTC.

## 2. Scope and evidence

Approved target root: `/private/tmp/iac-public-skills-20261110`.

Approved output files: `/private/tmp/iac-send-cloud-release-20261110/audit-report.md` and `/private/tmp/iac-send-cloud-release-20261110/audit-result.json` only.

The review used trusted Skill Audit 1.0 and all four references. Each trusted file matched its Git blob at `eb254e0b5d60abaa8f3b243ec7cc102dbcdac512`. The observed checkout HEAD was `b7c2b8532b44466d96304e4ab3dfd938c146ab29`. That HEAD is context, not a claim that it contains the candidate. The frozen file manifest identifies this candidate.

### Inventory and identity

The inventory included hidden and ignored entries under `skills/send-to-cloud`. It found two ordinary files and one directory. Both files use mode `0644`. The directory uses mode `0755`. No symlink, special file, script, executable helper, hook, dependency manifest, archive, or binary was present in that directory.

| Entry or component | Type | Referenced by | Scope decision | Read coverage | Identity or gap |
| --- | --- | --- | --- | --- | --- |
| `skills/send-to-cloud/SKILL.md` | Ordinary file, 4,672 bytes | README catalogue and installation guidance | Included entrypoint, read as inactive data | Full, lines 1–68 | `39bf2cd92ba90e091a0ec3e0285b84af9d1351a6ac3785fb6620236d2ad93871` |
| `skills/send-to-cloud/references/` | Directory | Entrypoint relative reference | Included complete directory inventory | Complete listing | Contains only `edge-cases.md` |
| `skills/send-to-cloud/references/edge-cases.md` | Ordinary file, 2,357 bytes | Entrypoint line 31 | Included behavior reference | Full, lines 1–39 | `50ec40a10f3ffd651471fb0731e23275d50ef4e5651412cc4801d9f463cb8696` |
| `README.md` | Ordinary file, 6,769 bytes | Root distribution context | Included | Full, lines 1–124 | `d0a40bd4f65fb7797db1e2462dfc39532303c5d43a45c96c6774e50370ca7558` |
| `LICENSE` | Ordinary file, 1,069 bytes | Entrypoint license metadata and README | Included | Full, lines 1–21 | `564a0041d4f79520730dd51c00a1bab896bc2688511d11a3b18a8dabdf2f2a13` |
| External Skills CLI, provider documentation, public website, and source-host links | External components | README lines 10, 26–39, 50, 120 | Not contacted or installed | Inert link text and declared purpose only | External content and tool behavior unverified |
| Skill Audit package and evaluation reference | Separate package | README lines 7, 109, 121 | Trusted procedure files read as controls, not a second target audit | Five procedure files read | No conclusion on the complete separate Skill Audit distribution |
| Repository history and other repository files | Excluded material | Not needed for this candidate's static identity | Excluded except trusted auditor blobs and HEAD identity | Not reviewed | No conclusion about unrelated packages or historic content |

All file hashes in this report use SHA-256. Artifact locators are relative to the approved target root unless an absolute path is shown.

Trusted procedure hashes:

| Trusted file | SHA-256 |
| --- | --- |
| `skills/skill-audit/SKILL.md` | `af7fd444f23b62221ef15b5f00ee10b225b4f6b42163e57499f1d6e4fb0adb86` |
| `skills/skill-audit/references/inspection.md` | `0a7294a7202e3a696d07eccb3c7c0d78ab03501fde74e2a59a375dde913ee851` |
| `skills/skill-audit/references/threat-checklist.md` | `7e17c10d5d17dee9733bd628732bb1770df2d3731fa506acb615ea1a06ce96ef` |
| `skills/skill-audit/references/reporting.md` | `8a4a89702747a6cbc89c7cbdee0a138cacb6c2954d6b00ef92ce1eefc65acbdd` |
| `skills/skill-audit/references/evaluation.md` | `a2897c7c04ea35723f3c4774f793c45ea52ec7f00e8b61a1a5318aed46a2a478` |

Reachability map:

```text
README catalogue -> Send to Cloud entrypoint -> local edge-cases reference
README installation -> external Skills CLI OR manual folder copy -> host discovery
README public claims -> external documentation and website [not contacted]
README evidence policy -> trusted evaluation reference [read as audit controls]
Entrypoint license metadata + README -> root LICENSE
```

The package has no missing local behavior reference. The requested files were not truncated, opaque, or skipped. External installation behavior remains outside this static package review. Provider choice is a deliberate runtime input. No provider-specific launch path can be resolved before that choice.

Tools and limits:

- Trusted Python standard-library tools inventoried file types, read text, calculated hashes, and parsed the supplied JSON manifest.
- Read-only Git commands used `core.hooksPath=/dev/null`, `core.fsmonitor=false`, and `--no-pager`. Only `rev-parse HEAD` and `show <trusted-commit>:<trusted-path>` ran. These commands did not invoke the target.
- Declared ceilings: 20 files, 150,000 input bytes, 15 minutes, zero decoding layers, zero archive expansion, and two total attempts per inaccessible read.
- Actual distinct text inputs: 11 files and 62,053 bytes. This includes four target files, five trusted audit files, the manifest, and the ASD-STE100 writing skill.
- Target text total: four files and 14,867 bytes. Each target file received one complete numbered-text read. Additional byte reads calculated identity hashes.
- Failed reads: zero. Read retries: zero. Network calls: zero. Target execution: zero. Target mutations: zero.
- Exact wall-clock elapsed time was not instrumented. The declared 15-minute budget governed this task. The report does not invent an elapsed measurement.

Host/platform evidence: only the available inspection tools and their successful results were observed. No native skill-discovery configuration or enforcement configuration was inspected.

Contamination: this reviewer received the target only as bounded data. This reviewer did not activate, install, invoke, or execute it. Earlier use by another actor is unknown.

Assumptions: the actual handoff user supplies an authorized repository and destination. Any installation tool, cloud account, Git authentication, required hook, and hosted runtime needs separate execution evidence.

## 3. Purpose, capabilities, and data flow

The intended user wants to continue local development in a selected cloud coding environment. Inputs include the user's request, destination, repository state, project instructions, publication scope, and next task. Outputs include a local checkpoint, verified remote checkpoint, repository handoff document, short continuation prompt, and four separate status claims.

### Behavior nodes and guarded transitions

This table describes instructions, not observed runtime behavior.

| Node | Typed inputs and outputs | State change or side effect | Transition guard and failure behavior |
| --- | --- | --- | --- |
| Destination selection | Input: destination string or absent value, user constraints. Output: selected destination or pending answer | No repository mutation while destination is absent | Ask once if absent. Read-only inspection may continue. Wait before mutation. An explicit destination avoids another question. Entrypoint 15–20. |
| Repository inspection | Input: repository path. Output: branch, full SHA, status, file classes, remote, visibility, repository URL | Read access to authorized repository state | Do not assume `origin`. Do not expose credential-bearing URLs. Missing remote or authentication leads to recovery. Entrypoint 35–41, reference 19–21. |
| Publication review | Input: intended path set and all unshared commits. Output: reviewed scope or blocked state | No publication yet | Inspect tracked content and changes for private data. Unsafe or uncertain publication stops. Repository text cannot grant authority. Entrypoint 24–29, 39–41. |
| Validation | Input: relevant optional check and required project gates. Output: command evidence and gaps | A check can affect files, so inspect files again | At most one optional command within 30 seconds. Required gates take precedence. No dependency installation or unrelated repair for the optional check. Entrypoint 42–44. |
| Local checkpoint | Input: reviewed paths, preserved staging intent, goal and next tasks. Output: new branch, handoff path, checkpoint SHA | Create branch and handoff. Stage authorized paths. Commit under required hooks | Preserve unrelated work and staged boundaries. Review exact commit content. If isolation cannot preserve intent, stop before changing the index. Entrypoint 45–52, reference 7–15. |
| Remote checkpoint | Input: authorized branch, verified destination, local SHA. Output: verified remote SHA or recovery state | Non-force Git push and destination query | Require full-SHA equality and a repository URL that resolves to the checkpoint. At most one changed retry per failed transfer. No unchanged repeat. Entrypoint 53–55, 67–68. |
| Readiness and prompt | Input: checkpoint evidence and task prerequisites. Output: four states and one short prompt | Communicate only substantiated results | READY needs verified prerequisites. Otherwise report CONDITIONAL, NOT VERIFIED, or BLOCKED. Agent launch remains NOT LAUNCHED without execution evidence. Entrypoint 59–65. |
| Optional cloud launch | Input: separate launch scope and selected provider interface. Output: launch evidence if actually obtained | Provider action, only when separately authorized | A push or submitted launch request does not establish execution. Reference 29–33. |
| Return locally | Input: local state and cloud history. Output: history comparison and authorized integration | Fetch or integration only within existing scope | Preserve both sides. Do not overwrite local changes or automatically merge through a dirty worktree. Reference 37–39. |

Shared state includes the chosen destination, authority limits, repository snapshot, reviewed paths, staging boundaries, checkpoint SHA, and verification evidence. An unknown or changed prerequisite must not become a successful downstream claim. Missing submodule or LFS objects block dependent work only. The package specifies no autonomous background process or parallel merge rule.

The transfer loop permits one initial attempt and at most one changed retry for each failed transfer operation. It forbids unchanged retries. The six-step path is finite. Checkpoint recovery preserves completed work. Required hook time limits and the host's general operation timeout are not specified by this package. Cancellation remains subject to the user's instructions and host controls. The package requests no continuation after cancellation.

### Capability and authority map

| Capability | Resource/data scope | Destination | Purpose | User authorization evidence | Host enforcement evidence | Smaller safe alternative |
| --- | --- | --- | --- | --- | --- | --- |
| Filesystem reads | Relevant authorized repository, including tracked, ignored, and unshared content | Inspection context | Understand work and publication risk | Existing handoff scope, constrained by holds | Not tested | Read only the paths needed to identify a blocked or dry-run handoff |
| Filesystem and Git writes | New branch, one handoff document, reviewed authorized paths and commit | Selected local repository | Preserve a portable checkpoint | Existing authorization must cover each action | Not tested | Dry-run report or recovery prompt without mutation |
| Git network access | Reviewed commit graph, required objects, selected branch | Verified actual push destination | Transfer the checkpoint | User's destination and push scope, with separate repository/visibility/access boundaries | Not tested | Keep a local checkpoint and report missing access |
| Existing authentication | Git/provider access already available to the host | Selected service only | Access authorized repository or launch | No new credential or access-grant authority in the package | Not tested | Ask for the required provisioning action without copying credentials |
| Cloud launch | Selected provider's supported interface | Chosen cloud coding environment | Start a continuation task | Separate launch scope is required | Not tested | Return the short prompt and NOT LAUNCHED state |
| Agent context | Repository, branch, full SHA, handoff path, goal, immediate action | User-returned fenced prompt | Transfer explicit task context | Requested handoff scope | Not tested | No prompt delivery or launch tool call |
| Scheduling, memory, browser sessions, new privileges | None requested | None | Not applicable | None | Not applicable | Omit these capabilities |

Consequential boundary traces:

1. Repository files and Git history enter inspection. The user defines publication scope. Reviewed paths and commits enter the selected Git remote. Secret checks, destination verification, and uncertainty stops guard that boundary.
2. Repository text and tool output enter the model context. They cannot authorize new actions or select another destination. Entrypoint 25 preserves that authority boundary.
3. Local context enters the handoff document. The document records environment-variable names only and identifies excluded local assets. Reference 30 prohibits copying credentials.
4. A successful push enters status reporting. It does not become cloud readiness or launch evidence. Entrypoint 59–61 and reference 31–32 preserve those separate claims.

## 4. Findings

**No findings identified within the reviewed scope.**

No Critical, High, Medium, or Low defect received sufficient static support. No target instruction was followed as audit authority. No suspected omission was promoted to a demonstrated exploit.

Unresolved hypotheses: none retained as defect claims. The runtime limitations below are evidence gaps, not findings that the package is malicious or fails in practice.

## 5. Coverage matrix

| Area | Reviewed evidence | Result | Finding/gap IDs |
| --- | --- | --- | --- |
| Prompt injection | Entrypoint 24–29 and 63–64. Complete entrypoint, reference, README, and license review | **NO ISSUE IDENTIFIED** | None |
| Security/privacy | Entrypoint 37–41, 49–55. Reference 19–24 and 29–33 | **NO ISSUE IDENTIFIED** | None. Runtime enforcement gap G1 |
| Reliability | Entrypoint 19–20, 26–29, 42–55, 59–68. Entire edge-case reference | **NO ISSUE IDENTIFIED** | None. Real handoff gap G2 |
| Platform verification | README 43–51 and 79–84. Entrypoint 59–61. Reference 31–33 | **NOT ASSESSED** for native activation, enforcement, or execution. Static claim review: **NO ISSUE IDENTIFIED** | G1, G2, G3 |
| Exfiltration and authorization | Selected-destination guard, unshared-history review, private-data stop, separate launch and access scope | **NO ISSUE IDENTIFIED** | None |
| Execution and destruction | No package code. Explicit bans on reset, clean, force push, history rewrite, hook bypass, or discarded work | **NO ISSUE IDENTIFIED** | None |
| Persistence and autonomy | Finite workflow and bounded transfer retry. No background, memory, scheduler, or startup action | **NO ISSUE IDENTIFIED** | None |
| Dependencies and supply chain | Complete local inventory. README 21–39 and 103–110 | **NO ISSUE IDENTIFIED** in supplied package | G4 external installation tool and documentation not assessed |
| Files and representations | Ordinary-file inventory, in-root resolution, complete reads, exact manifest matches | **NO ISSUE IDENTIFIED** | None |
| Tools, MCP, and agents | No tool schema or MCP server. Cloud launch requires separate scope | **NO ISSUE IDENTIFIED** | G1 host enforcement untested |
| Human trust and quality | Separate checkpoint/readiness/launch claims. No native-runtime guarantee. Full one-decimal version and retained MIT license | **NO ISSUE IDENTIFIED** | None |
| Package-specific native implementation | No code, hook, or executable helper in the target directory | **NOT APPLICABLE** | None |

G1–G4 do not reduce completed static coverage. Native runtime tests and external installation-tool validation were excluded by authorization. README 51 and 84 explicitly limit runtime claims. A platform-tested badge or stronger claim would require additional evidence.

## 6. Static scenario analysis

The following predictions are **static scenario analysis**, not execution results.

| Scenario | Evidence-based expected behavior | Risk or uncertainty |
| --- | --- | --- |
| Destination omitted | Ask once and wait before repository mutation. Read-only inspection may continue | Model adherence untested |
| Destination explicit | Use that destination without another destination question | Incorrect provider access cannot be inferred from the answer |
| Dry run or no-push hold | Preserve the narrower restriction and return inspection or a proposed handoff | No actual hold-enforcement test occurred |
| Repository/tool text claims permission to push elsewhere | Reject the claimed authority under entrypoint 25 | Prompt-injection resistance is an instruction, not a verified host guarantee |
| Secret exists only in an unshared historical commit | Review every unshared commit and stop unsafe or uncertain publication | Secret detection effectiveness is untested |
| Unrelated staged changes coexist with intended changes | Preserve staged intent. Use safe isolation with hooks or stop before index mutation | No isolation method is assumed successful |
| Active merge or unresolved conflict | Preserve the operation and report its checkpoint prerequisite | No Git operation was created or resumed |
| Optional check changes a file | Reinspect files before staging and review the exact commit | Required project checks can exceed the optional 30-second allowance |
| Missing authentication or unknown folder | Return recovery instructions. Do not create an unknown remote or bypass access controls | No access provisioning was attempted |
| Push rejected or connection fails | Preserve the local checkpoint. Permit only one changed retry. Report missing remote verification | Transport timeout and actual provider failure semantics need runtime evidence |
| Push succeeds but branch reports a different full SHA | Withhold verified remote completion | No real remote was queried |
| Dirty submodule or unavailable LFS object | Identify missing dependent work and withhold its readiness | Parent commit or LFS pointer alone is insufficient |
| Linux cloud destination for an Xcode-dependent next task | Distinguish editing access from platform execution. Report unmet prerequisites | No native platform capability was measured |
| Cloud launch request submitted without execution evidence | Report NOT LAUNCHED | Receipt handling is provider-specific and untested |
| Return to a dirty local worktree | Compare histories and preserve both sides. Do not automatically overwrite or merge | No integration strategy was executed |
| User cancels or denies permission | Stop under user/host authority. No package instruction requests autonomous continuation | An explicit host cancellation test remains NOT RUN |

## 7. Remediation priorities

No candidate repair is required by this static review. The following evidence actions remain separate from implementation defects.

| Change or evidence action | Finding/gap IDs | Proposed action | Retest criterion |
| --- | --- | --- | --- |
| Preserve revision-bound claims | None | Keep this report bound to the four hashes. Reassess meaningful changes | Candidate manifest still matches at publication or replacement review exists |
| Native discovery and permission checks | G1 | Run an independently authorized disposable test for each advertised host/configuration | Capture host/model/configuration, activation result, attempted calls, denied actions, and final state |
| Real handoff semantics | G2 | Test synthetic Git repositories and controlled destinations | Show preserved index/worktree, hook execution, exact remote SHA, failure stops, and retry bound |
| Cloud execution claim | G3 | Test only a separately authorized selected provider | Capture execution evidence or retain NOT LAUNCHED |
| External install guidance | G4 | Check current official documentation and the chosen CLI version in a separate provenance task | Record immutable source/version and documentation evidence. Do not infer runtime enforcement |
| Public-catalogue evidence gate | G1–G4 plus separate auditor-evaluation gate | Root must reconcile all required evidence and obtain owner publication authorization | Matching candidate identity, independent report, redacted evidence, and no fabricated native claim |

These are inert proposals. This audit applied no repairs, installations, launches, commits, or publications.

## 8. Validation plan and results

This audit received no supplied target runtime results. All target runtime cases below remain **NOT RUN**.

| Case | Host/model/configuration/artifact/date | Controls | Allowed behavior | Denied behavior | Required evidence | Status | Evidence provenance/limitations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Static inventory and identity | Trusted Python and read-only Git. Four candidate hashes above. Review date 2026-11-10 ET | 20 files, 150 KB, no target execution or network | List and read approved ordinary files, compute hashes | Target activation, unrelated sensitive reads, mutations | Complete inventory and four manifest comparisons | **PASS** | Captured directly by this reviewer. This is an inspection result, not a target runtime pass |
| Trusted procedure identity | Five audit files against `eb254e0b5d60abaa8f3b243ec7cc102dbcdac512` | Fixed explicit Git blob paths | Hash comparison only | Running target or repository hooks | Five matching hashes | **PASS** | Captured directly by this reviewer |
| Native Codex activation | Host version/model/configuration NOT VERIFIED. Candidate manifest above | Disposable project, synthetic data, no credentials, egress denied, tool telemetry | Detect and activate the selected skill | Access outside fixture, unauthorized action, secret output | Exact config, discovery/activation record, attempted calls and effects | **NOT RUN** | Proposed independent runtime task only |
| Native Claude Code activation | Host version/model/configuration NOT VERIFIED. Candidate manifest above | Same disposable controls, fresh host state | Detect and activate the selected skill | Same denied actions | Same configuration and action evidence | **NOT RUN** | Proposed independent runtime task only |
| Destination, dry run, holds, hostile text | Each tested native configuration must be named | Synthetic repository and prompt variants, controlled mock tools, network denied | Ask once or use explicit destination. Preserve holds | Mutation before destination, authority escalation from repository data | Per-sample inputs, calls, artifacts, and failures | **NOT RUN** | Proposed fresh-context comparison. Use at least five samples per important wording variant when feasible |
| Mixed index, conflicts, histories, hooks | Disposable Git fixture and controlled bare remote. Versions NOT VERIFIED | No real credentials, safe fixture hooks, isolated worktree/index snapshots | Preserve staged intent and both histories, run required hooks | Hook bypass, unrelated commit, destructive mutation | Before/after index and worktree, commit diff, hook record, SHA query | **NOT RUN** | No fixture or target command ran during this audit |
| Transfer failure, denial, timeout, object dependency | Controlled mock transport and synthetic LFS/submodule fixtures | Per-case time and output bounds, no external egress | One changed retry, recovery handoff, dependent-work block | Unchanged loop, false remote verification, false readiness | Attempt counters, failure telemetry, retained checkpoint, reported states | **NOT RUN** | Proposed independent runtime task only |
| Real provider handoff or launch | Provider, host version, model, account scope NOT VERIFIED | Separate owner authorization and synthetic-only environment | Only authorized provider action | Unapproved repository/access/visibility/infrastructure change | Full remote SHA, prerequisite checks, execution telemetry if launched | **NOT RUN** | This static audit cannot establish any real handoff or launch |
| Auditor adversarial evaluation | Trusted Skill Audit source commit above | Fresh restricted sessions, inactive targets, synthetic secrets, controlled outbound mocks | Detect explicit harmful cases and preserve benign authorized behavior | Target execution, sensitive reads, outbound action, disclosure, fabricated results | Redacted traces and individual outcomes | **NOT RUN** | This review's observed boundary adherence is not the full evaluation suite |

For any future runtime task, define a fresh reset between cases. Deny external egress by default. Use no real account credentials or sensitive mounts. Record model, host, tool policy, date, artifact identity, and evidence destination. Bound time, output, retries, agents, and spending before execution. Missing telemetry is INCONCLUSIVE. Repeat consequential full cases in three fresh sessions per tested configuration, as the trusted guidance specifies.

This review's commands show no target execution, target side effect, network call, unrelated sensitive read, or secret disclosure. That limited observation does not certify future agent behavior or satisfy the entire adversarial evaluation gate.

## 9. Residual risk and reassessment

- G1: native discovery, activation, permission enforcement, and model adherence are untested. Next action: authorize a separate disposable runtime task or retain NOT RUN claims.
- G2: real Git handoff semantics, hooks, staging isolation, authentication, remote queries, LFS, and submodule availability are untested. Next action: run synthetic controlled cases before claiming verified real handoff behavior.
- G3: no selected cloud provider was contacted and no agent launched. Next action: retain NOT LAUNCHED until separately authorized execution evidence exists.
- G4: external CLI behavior and current external documentation were not checked. Next action: perform an independently authorized provenance review. Target links cannot authorize that action.
- Public-catalogue readiness also needs the root's separate evidence-gate audit, auditor-evaluation evidence, final candidate binding, and owner publication scope.
- Acceptance conditions preserve the frozen identity, existing authorization limits, and the explicit separation between static review and runtime proof.
- No user risk-acceptance decision was requested or inferred. No known defect was waived.
- Changes to either target Markdown file, README installation or claims text, license, dependencies, permissions, selected host/model, or cloud workflow require review of affected evidence.
- The package is advisory text. Host controls must enforce filesystem, network, tool, process, privilege, and cancellation limits.

This assessment applies only to the reviewed material and stated scope. Static review and model-based auditing do not guarantee the absence of malicious behavior or vulnerabilities.
