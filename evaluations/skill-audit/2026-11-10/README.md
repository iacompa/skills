# Skill Audit text evaluations — 2026-11-10

These artifacts document static report assessments, not execution of target skills.

| Artifact | Purpose |
| --- | --- |
| [cases.redacted.json](cases.redacted.json) | Fifteen inert target packages. The C04 synthetic marker was replaced before publication. |
| [expectations.json](expectations.json) | Case-specific content expectations withheld from fresh evaluators. |
| [baseline.json](baseline.json) | Ten assessments before the candidate skill was authored. |
| [baseline-assessment.md](baseline-assessment.md) | Root interpretation and limits of the control. |
| [forward-one.json](forward-one.json) | Fifteen skill-assisted assessments. |
| [forward-two.json](forward-two.json) | Seven independent repeat assessments. |
| [forward-three.json](forward-three.json) | Seven more independent repeat assessments. |

The twenty-nine skill-assisted assessments met the checked content expectations. Seven cases received three fresh-context assessments each. This is an observed result for these small supplied cases, not a general success rate or certification. The control already met the main behavioral checks; no measured improvement is claimed.

The original C04 input is private because the auditor requires credential-like canaries to stay out of public evidence. Its published placeholder changes the input bytes. Original input hashes in individual reports therefore do not match that redacted fixture. Other fixture text remains unchanged.

The evaluators used inherited `gpt-6.1-sol` in native Codex subagents. They read the auditor manually. No installation, automatic discovery, installed command, host-enforcement, or Claude Code test is established.

[Read the source review and captured-action evidence](../../../audits/skill-audit/1.0/README.md).
