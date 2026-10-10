---
name: atu-architect
description: Use when designing a new system or a substantial module with consequential boundary, data ownership, consistency, deployment, or quality-attribute decisions, or when explicitly invoking $atu-architect.
---

# ATU Architect

Turn requirements and repository evidence into a reviewable system architecture before feature decomposition. Support direct invocation and handoff from `$atu-prd`; architecture approval is separate from PRD approval.

## Scope

- Resolve the project, requirement sources, applicable `AGENTS.md`, and authorized design location. Default to `docs/architecture/<scope>.md`; ask when the target is ambiguous. Read code/configuration and relevant tests, not credential contents.
- Write architecture documents only. Do not implement, create feature tasks, change dependencies, deploy, or infer Git/external-write authority. Preserve existing work and approved architecture revisions.
- Direct invocation may analyze any requested scope. For routine changes with sufficient existing architecture, provide a short reuse assessment instead of manufacturing a new design.

## Design

Read the [architecture contract](references/architecture-contract.md) before authoring. Reuse a current approved baseline; for existing systems describe the evidenced current structure and only the required delta. For a new system establish goals, constraints, owners, boundaries, and quality scenarios before recommending technology.

Read the relevant parts of the [design guide](references/design-guide.md) when choosing boundaries, architecture styles, or patterns. Compare credible alternatives only at consequential forks. Explain the simplest viable option, recommendation, operational/maintenance cost, and verification. A named pattern is not a quality goal.

Produce one readable document for the scope: context, module/dependency view, data ownership and consistency, key success/failure flows, consequential decisions, expected extension scenarios, and incremental delivery/compatibility/recovery. Use small diagrams where they clarify boundaries; use plain language and explain necessary terminology. Record unknown capacity or product rules as questions, not invented facts. An architecture diagram does not replace a required UI design and its approval.

## Confirm and hand off

Self-check for cyclic dependencies, ambiguous data owners, unhandled boundary failures, unsupported assumptions, and speculative abstractions. This is part of authoring, not an additional independent audit pipeline.

Present the proposal and unresolved consequential choices together. Keep its revision `DRAFT` until the user explicitly confirms that revision and scope; existing confirmation is reusable when it clearly applies. Then record `APPROVED` with its confirmation evidence and hand off the original requirement source plus architecture path/revision/sections to `$atu-prd`. If this was a PRD handoff, resume the original planning request after confirmation; otherwise offer the command without starting unrelated work.

Missing decisions block only dependent scope. Report the document, reuse/delta rationale, recommended decisions, questions, and next action. Never turn an unapproved recommendation into an implementation-ready specification.
