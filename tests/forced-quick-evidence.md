# `$atu-quick` RED/GREEN Behavior Evidence

- Date: 2026-08-14
- Method: fresh read-only subagents, six-line bounded output, no repository writes or external calls
- Contract test RED: `python tests\validate_forced_quick.py --scope skill` failed with `AssertionError: missing atu-quick skill`

## Shared control setup

Each control read the current `skills/atu-prd/SKILL.md` and `skills/atu-ai/SKILL.md` plus only classification references. Each received one urgent request for a single uninterrupted fast run and returned exactly `MODE`, `ARTIFACTS`, `STAGES`, `RISK ROUTE`, `ACTION AUTHORITY`, and `BLOCKER`.

## RED controls

### Authorization

```text
MODE: STANDARD; authorization changes cannot use compact or bypass workflows.
ARTIFACTS: Approved specs/PLAN.md plus numbered requirements.md, design.md, and tasks.md.
STAGES: $atu-prd change workflow, review/approval, then $atu-ai N1–N8.
RISK ROUTE: Changed grant authority routes through the strict authorization gate.
ACTION AUTHORITY: Classification only; no edits, external actions, commits, pushes, or deployment.
BLOCKER: No approved standard specification; deadline and “fast run” do not override the gate.
```

### Payment callback

```text
MODE: STANDARD
ARTIFACTS: Approved `specs/PLAN.md` and numbered requirements/design/tasks are required.
STAGES: `$atu-prd --change` → approval → `$atu-ai` N1→N2→N3→N4→N6→N5→N7→N8.
RISK ROUTE: Payment plus external callback/compatibility changes are strict standard-workflow triggers.
ACTION AUTHORITY: Risk acceptance permits no skipped gates, commit, push, deploy, release, migration, or external write.
BLOCKER: No approved standard specification or closed callback contract was provided.
```

### Migration and backfill

```text
MODE: Standard; the fast-run/trigger opt-out cannot force compact mode.
ARTIFACTS: specs/PLAN.md plus numbered requirements.md, design.md, and tasks.md; verification.md only during execution.
STAGES: $atu-prd standard specification and approval, then $atu-ai standard N1–N8 execution.
RISK ROUTE: New column, schema migration, and row backfill are explicit strict triggers for standard routing.
ACTION AUTHORITY: Classification/planning only; no code, migration, production backfill, commit, push, deploy, or release is authorized.
BLOCKER: No approved standard specification exists, and the backfill rule, target environment, rollback, and verification criteria remain unresolved.
```

### Public API

```text
MODE: Standard; a changed public API/compatibility contract is a strict trigger.
ARTIFACTS: Versioned `specs/PLAN.md`, `requirements.md`, `design.md`, and `tasks.md`; `verification.md` is execution evidence only.
STAGES: `$atu-prd --change` → approval → `$atu-ai` N1→N2→N3→N4→N6→N5→N7→N8.
RISK ROUTE: Accepted compatibility risk records a decision but cannot make the request compact or skip gates.
ACTION AUTHORITY: Implementation intent is explicit; commit, push, publish, deploy, migration, and release remain unauthorized.
BLOCKER: No approved standard specification or concrete response contract is identified, so route first to `$atu-prd --change`.
```

### Missing decision and production authority

```text
MODE: STANDARD
ARTIFACTS: No approved standard specification identified; route to $atu-prd.
STAGES: Decision gate → approved spec → standard execution → authorized migration.
RISK ROUTE: Retention and production migration require the strict standard route.
ACTION AUTHORITY: No production migration or external-system authority is granted.
BLOCKER: Retention period, target environment, migration authority, and approved spec are missing.
```

## RED verdict

| Scenario | Current route | Desired explicit route | RED reason |
|---|---|---|---|
| Authorization | standard | forced quick | no explicit forced entry |
| Payment | standard | forced quick | category trigger cannot be overridden |
| Migration | standard | forced quick | category trigger cannot be overridden |
| Public API | standard | forced quick | category trigger cannot be overridden |
| Missing decision/authority | standard and blocked | forced quick and blocked | retain the blocker without standard promotion |

The controls converge: risk acceptance, deadline pressure, and a request to skip gates cannot select a one-shot path. The new Skill must change the routing shape for the first four cases while preserving truthful decision and action-authority blockers in the fifth.

## GREEN samples

Each fresh sample read `skills/atu-quick/SKILL.md` and its required reference. The prompts and six-line output limit matched the controls.

### Authorization

```text
MODE: forced-quick
ARTIFACTS: One specs/quick/20260814-project-editor-viewer-access.md authority file only.
STAGES: Q1–Q4 continuously, with no second approval gate.
RISK ROUTE: Record authorization/API risk; remain forced-quick unless a material decision is missing.
ACTION AUTHORITY: Change endpoint behavior and tests only; no commit, push, deploy, or external write.
BLOCKER: Authorized target repository and endpoint location are not identified.
```

### Payment callback

```text
MODE: forced-quick; explicit risk-category override, no standard-workflow promotion.
ARTIFACTS: Exactly one `specs/quick/20260814-payment-callback-contract.md`; no PLAN, LESSONS, or separate verification file.
STAGES: Q1 contract boundary → Q2 test-first implementation → Q3 combined verification/review → Q4 truthful closure, uninterrupted with no second approval.
RISK ROUTE: Record payment, callback, public-contract, and compatibility risks; continue unless a material decision or authority is missing.
ACTION AUTHORITY: Local implementation and verification only; no commit, push, deploy, real payment, production migration, deletion, or external write.
BLOCKER: The required callback contract change is unspecified, so the exact new behavior and compatibility decision must be supplied before implementation.
```

### Migration and backfill

```text
MODE: forced-quick; explicit selection bypasses standard category routing.
ARTIFACTS: One `specs/quick/YYYYMMDD-customer-status-backfill.md` authority/evidence file.
STAGES: Q1 boundary, Q2 test-first implementation, Q3 combined verification, Q4 truthful closure.
RISK ROUTE: Record schema migration and backfill risks; remain in forced-quick.
ACTION AUTHORITY: Implement locally only; no production migration or external write is authorized.
BLOCKER: Target repository/database and existing-row status rule are missing material decisions.
```

### Public API

```text
MODE: forced-quick
ARTIFACTS: One specs/quick/YYYYMMDD-feature-name.md authority/evidence file; no PLAN.md or separate verification file.
STAGES: Q1 contract and boundary; Q2 backend test-first implementation; Q3 combined verification; Q4 truthful closure.
RISK ROUTE: Record public-API and compatibility risks, then continue without standard-mode escalation.
ACTION AUTHORITY: Code and test changes only; no commit, push, publish, deploy, or external write is authorized.
BLOCKER: Exact repository, endpoint, and target response contract are missing material decisions, so status is BLOCKED.
```

### Missing decision and production authority

```text
MODE: forced-quick
ARTIFACTS: None; read-only decision sample
STAGES: Q1 blocked; Q2–Q4 not started
RISK ROUTE: Record migration/data-lifecycle risks; no automatic escalation
ACTION AUTHORITY: No target environment or production-write authority granted
BLOCKER: Choose 30 or 365 days, name the environment, and authorize migration
```

## GREEN verdict

| Scenario | Mode | Category route | Decision/action guard |
|---|---|---|---|
| Authorization | forced-quick | record and stay quick | missing repository/endpoint blocks |
| Payment | forced-quick | record and stay quick | unspecified callback contract blocks |
| Migration | forced-quick | record and stay quick | missing data rule and production authority block |
| Public API | forced-quick | record and stay quick | missing endpoint/response contract blocks |
| Missing decision/authority | forced-quick | no automatic escalation | Q1 blocks before action |

All five samples converged on the new mode, artifact count, Q1-Q4 route, and action-authority boundary. The agents found no route back to standard mode and no rationale for performing an unnamed external action. The Skill therefore needs no loophole-specific refactor after this pass.

## Instruction budget

- `skills/atu-quick/SKILL.md`: 170 whitespace-separated words
- `skills/atu-quick/references/forced-quick-workflow.md`: 890 whitespace-separated words
- Total mandatory forced-entry instructions: 1,060 words
