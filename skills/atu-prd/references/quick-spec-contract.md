# Compact ATU PRD Specification Contract

Create one implementation-ready specification for one bounded change. Compact mode reduces planning artifacts, not engineering rigor.

## Eligibility gate

Confirm from the request and repository evidence that the change has one coherent goal, one repository, one localized boundary or bounded vertical slice, one implementation-and-verification task, at most five observable outcomes, closed decisions, stable existing contracts, feasible focused verification, and localized rollback.

Existing authenticated clients and APIs, repositories, components, helpers, and libraries may be consumed when their authentication, authorization, ownership, input/output, error, compatibility, data-lifecycle, and operational contracts remain unchanged.

Use standard mode instead when the change introduces or modifies authentication, authorization, privacy, payment, audit policy, schema, migration, backfill, destructive data behavior, a public API or compatibility contract, an external provider/callback/queue, production configuration, deployment topology, broad shared state, a cross-repository boundary, multiple independently deliverable tasks, or any material uncertainty. A user request for speed cannot waive these triggers.

## File and status contract

Write exactly one authority/evidence file:

```text
specs/quick/YYYYMMDD-feature-name.md
```

Use a lowercase kebab-case name. If the path exists for different work, append `-2`, `-3`, and so on; never overwrite or merge unrelated specifications.

Use only these statuses:

- `READY`: specification is approved and implementation has not started;
- `IN_PROGRESS`: `$atu-ai` began the first test or implementation edit;
- `DONE`: all required implementation, verification, review, and acceptance evidence passes;
- `BLOCKED`: a required decision, environment, or verification boundary prevents completion; or
- `ESCALATED`: evidence requires the standard workflow.

`$atu-prd` creates a complete compact file as `READY`. It does not set `IN_PROGRESS` or `DONE`.

In compact mode, do not create or update `PLAN.md`, `LESSONS.md`, a numbered feature directory, `requirements.md`, `design.md`, `tasks.md`, or `verification.md`. Preserve existing standard specifications unchanged.

## Required document

Use this exact section order:

```markdown
# <Feature name>

- Status: READY
- Mode: compact
- Date: YYYY-MM-DD
- Source: <request, named file, and repository evidence>

## Goal
<One observable outcome and its user value.>

## Scope
- In scope: <bounded behavior and affected boundary>
- Out of scope: <adjacent behavior and forbidden contract changes>

## Reused contracts and evidence
- <existing component/API/helper and repository evidence that makes it stable>

## Compact eligibility and escalation triggers
- Eligible because: <one task, closed decisions, focused verification, localized rollback>
- Escalate if: <concrete strict boundary discovered during implementation>

## Bounded design
- Affected boundary: <module or vertical slice>
- Behavior flow: <short happy and unhappy path>
- Security and compatibility: <preserved auth/ownership/protocol/error contracts>
- Lifecycle and recovery: <cleanup, concurrency, rollback, or not applicable with reason>
- Verification: <focused automated and required real-environment checks>

## Acceptance criteria
- [ ] AC-Q01: <observable atomic result>
- [ ] AC-Q02: <observable atomic result>

## Task
- [ ] T-Q01: Implement and verify the complete bounded change. Covers: AC-Q01, AC-Q02.

## Execution evidence
- Pre-existing changes: pending Q1
- Changed files and diff scope: pending
- Verification commands and results: pending
- Acceptance matrix: pending
- Manual or external boundaries: pending

## Open questions
None.

## Handoff
`$atu-ai specs/quick/YYYYMMDD-feature-name.md`
```

Create between one and five atomic criteria, using the contiguous IDs `AC-Q01` through at most `AC-Q05`. Create exactly one top-level task checkbox and exactly one task ID: `T-Q01`. The task includes implementation, focused tests, relevant regression checks, combined review, and acceptance verification; do not split those activities into orchestration tasks.

The bounded design must be concrete enough to prevent architectural guessing. Record reused boundaries, data flow, unhappy paths, authorization and privacy invariants, compatibility, lifecycle or concurrency cleanup, verification strategy, and rollback only where relevant. Do not add speculative abstractions or boilerplate sections with invented content.

Keep the initial `READY` specification at or below 575 whitespace-separated English words or about 800 CJK characters. Prefer short evidence-backed bullets. If the material contract cannot fit without hiding decisions, risks, or verification boundaries, use standard mode instead of compressing away required detail.

## Questions, promotion, and review

If a material question remains, do not publish a `READY` compact file. Route to standard mode so its blocking-question gate and dependency analysis can preserve the uncertainty.

If a strict trigger is found before writing, use the standard workflow directly. If a previously published compact request expands, preserve its file, set or recommend `ESCALATED` with evidence, and create or update standard artifacts only through the standard workflow. Never copy an unresolved assumption into the promoted design.

Before handoff, verify the path is unique; the status and section order are correct; no standard artifact was changed; every criterion is observable; there are at most five criteria; there is exactly one `T-Q01`; the design covers applicable security, errors, compatibility, lifecycle, tests, and rollback; and no open question or strict trigger remains.

Report selected mode, source/evidence, created file, goal, criterion count, task count, escalation triggers, checks performed, and final status. End with the exact copyable `$atu-ai <compact-path>` command.
