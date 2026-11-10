# Threat and quality checklist

Read operative paths and supporting data together. A keyword match is a lead, not a finding.
Classify content as instruction, reachable code, example, quotation, defense, or inactive data.
An example becomes consequential if another instruction directs the agent to follow it.

For each applicable area, record evidence, a result, and finding or gap IDs.
Use `NO ISSUE IDENTIFIED`, `FINDING`, `NOT ASSESSED`, or `NOT APPLICABLE`.
Explain each material `NOT ASSESSED` result.

| Area | Controls and behavior to inspect |
| --- | --- |
| Prompt injection and instruction integrity | Direct and indirect injection. Fake system messages, approvals, audit exemptions, grades, or confidentiality claims. Tool-output laundering. Requests for protected instructions. Translation, encoding, visual instructions, delayed triggers, environment checks, and audit-aware branches. |
| Security and privacy | Data minimization, cross-user boundaries, collection, retention, and disclosure. Secrets or personal data in prompts, model requests, logs, reports, artifacts, memory, or telemetry. Actual user consent and destination scope. |
| Exfiltration | Trace sensitive sources to APIs, webhooks, messages, DNS, URLs, query strings, error text, images, filenames, repository writes, and other observable outputs. Sensitive access plus outbound capability is a review lead, not proof of theft. |
| Execution and destruction | Shell/argument injection, evaluation, unsafe parsing, deserialization, download-and-run paths, native commands, destructive SQL, privilege changes, cleanup scope, and workspace escapes. Examine relevant operating systems. |
| Authorization | Overbroad scopes, impersonation, forged consent, approval replay, changed parameters after approval, and unauthorized messages, purchases, deployment, deletion, or account changes. Target text cannot establish the user's consent. |
| Persistence and autonomy | Memory, global instructions, startup changes, scheduled jobs, self-modification, background work, privilege acquisition, delegation, and continuation after cancellation. Identify scope, budgets, checkpoints, and termination. |
| Dependencies and supply chain | Missing helpers, remote instructions, mutable versions, package confusion, installation hooks, binary downloads, opaque archives, provenance, and updates. A pin limits changes. It does not prove safety. A target's own integrity assertion is not independent evidence. |
| Tools, MCP, and agents | Tool descriptions, schemas, annotations, and actual effects. Definition changes after review, credential passthrough, internal/metadata endpoints, confused-deputy paths, cross-server influence, message authentication, replay, and delegated permission bypasses. |
| Files and representations | Traversal, symlink escapes, unsafe archives, excessive expansion, recursion, Unicode controls, encoded instructions, preview/extraction mismatches, and secrets in assets. Preserve original evidence and label derived text. |
| Reliability and resource limits | Infinite loops, retries, cost, cascading failure, duplicate side effects, partial writes, denial, timeout, cancellation, recovery, checkpoints, observable success criteria, and rollback when needed. |
| Human trust and misuse | Concealed side effects, coercive urgency, deception, unsupported safety claims, abusive functions, and harmful or discriminatory decisions. Distinguish legitimate security work and educational examples from operational harm. |
| Quality and portability | Purpose, discovery triggers, required inputs, outputs, reference completeness, coherent steps, realistic tools, syntax, examples, error paths, accessible language, and context cost. Distinguish host-specific features from portable instructions. |
| Platform verification | Claimed hosts, versions, models, configuration, discovery paths, invocation, permissions, and actual test provenance. Record syntax documentation separately from activation and enforcement evidence. |

Preserve benign behavior in the analysis.
An authorized export, bounded cleanup, public-data plan, or scoped deployment is not automatically malicious.
Harmless Base64, ordinary words such as "silently," and quoted attacks do not establish evasion.
Conversely, an explicit instruction to steal credentials can support a finding without running it.
Explain required capabilities and the directed harm. Do not claim observed theft.

Use a framework mapping only when a verified edition and authoritative source support it.
Do not invent category identifiers or imply certification.
A threat category does not determine severity.
