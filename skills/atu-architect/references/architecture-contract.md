# Architecture contract

Use for architecture authoring and for applicable architecture references in planning. Architecture supplies confirmed technical constraints; the PRD remains business authority and feature requirements/design/tasks remain the implementation contract.

## When architecture is needed

Before feature decomposition, examine whether the request creates a new system, materially changes module/dependency boundaries, shared contracts, data ownership/transaction boundaries, deployment units, or requires a consequential tradeoff to satisfy a quality target. An important new domain qualifies when its integration changes these boundaries. Size, task count, payment, authentication, or schema categories alone do not qualify.

An applicable approved baseline closes this step: reuse its relevant decisions. Existing code can establish sufficient architecture for a routine extension without a new document. If material decisions remain, enter architecture design before final feature splitting; unrelated ready scope may continue. Explicit `$atu-quick` retains its own workflow and decision/authorization blockers, not this automatic gate.

## Sources and identity

Discover candidates from user references, relevant existing spec references, repository guidance, and `docs/architecture/`; read only applicable sections and their prerequisite decisions. Existing named architecture files elsewhere may be used without relocation. Verify scope, revision, approval evidence, and conflicts; newest filename/date alone does not establish authority. A label claiming approval without a traceable user/owner confirmation is insufficient.

Default to one `docs/architecture/<scope>.md` per system or substantial change. Follow an established document format when it provides the same facts. Each revision records:

- Revision (`v1`, `v2`, ...), `DRAFT` or `APPROVED`, date, and exact system/change scope.
- Business sources and versions; relevant code/configuration evidence; applicable parent architecture path, revision, and sections when designing a delta.
- Confirmation evidence identifying who approved what and when; for a draft explicitly state that confirmation is pending.
- Supersession scope: which prior decisions change, which remain valid, and affected modules/specs.

Keep an approved revision intact. Append a new draft revision in the same document; never edit approved decisions in place or relabel a changed proposal as approved. After explicit confirmation, update the new revision's approval record. Supersession is limited to its declared scope; approval does not automatically update implementation specifications. If the existing format cannot preserve revisions clearly, use a separate versioned draft and link the prior baseline.

## Useful document content

Adapt section depth to the problem; omit inapplicable detail with a short reason instead of filling a universal template.

1. **Context and constraints:** goals/non-goals, actors, deployment/team/cost constraints, current structure if any, and quality scenarios (condition, expected response, measurable target or explicit unresolved target).
2. **Boundaries:** module responsibilities and exclusions, allowed dependency direction, integration contracts, deployment units only when needed. Separate target design from implemented reality.
3. **Data and flows:** each authoritative writer/owner, tenant/trust boundary, transactions and cross-boundary consistency; key normal path and relevant failure/retry/recovery behavior.
4. **Decisions:** stable document-local `AD-001` identifiers for consequential choices, options, recommendation, rationale/evidence, costs, and acceptance/validation method. Distinguish confirmed constraints, recommendations, and open questions.
5. **Evolution:** a concrete expected extension and its affected versus stable modules; phased delivery, mixed-version compatibility, migration/recovery where applicable, and risks requiring validation before dependent work.
6. **Handoff:** approved path/revision/decision references, affected scope, remaining blocking questions and owners, and original business requirement sources for `$atu-prd`.

Define shared contract semantics, not every endpoint field, database column, class, feature task, or a second feature dependency graph. Detailed feature designs and the delivery DAG belong to `$atu-prd`. A system architecture approval does not approve unspecified product behavior or waive a required UI design review.

Use official documentation for selected external APIs/platform constraints before asserting protocol facts; record applicable version and links. A proposed technical spike is not executed evidence. Unknowns that can overturn a boundary or selection stay open until resolved or explicitly accepted with a bounded validation/fallback plan.

## Planning and execution handoff

Architecture is a supplemental technical source, including when a single PRD was named. Record its path/revision/confirmation in the existing PLAN source ledger; reference relevant decisions in feature `design.md` context. Compact specs use their existing reused-contracts section. Do not import new business scope from architecture or duplicate its full contents.

Conflicting requirements, guidance, code, or architectural revisions require an explicit resolution; proposed target differences from current code are not automatically defects. An affected unapproved architecture decision blocks final design/tasks, not unrelated work. No architecture file is required retroactively for unchanged legacy boundaries.

For a new approved revision, use `$atu-prd --change` to identify affected feature/shared-contract consumers and publish their updates under existing ID/version rules. Preserve completed task text and add new work for changed behavior. A newer unrelated revision does not invalidate all specifications; an unapproved draft does not supersede an approved baseline. Execution checks only applicable approved decisions and stops affected work on a missing, conflicting, or superseded dependency until specifications are reconciled.
