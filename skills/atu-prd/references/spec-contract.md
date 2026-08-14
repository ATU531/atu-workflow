# ATU PRD Specification Contract

## Contents

1. [Contract invariants](#contract-invariants)
2. [Output layout](#output-layout)
3. [Authoritative source discovery](#authoritative-source-discovery)
4. [Status, checkbox, version, and ID conventions](#status-checkbox-version-and-id-conventions)
5. [Blocking-question gate](#blocking-question-gate)
6. [PLAN.md structure and example](#planmd-structure-and-example)
7. [LESSONS.md structure and example](#lessonsmd-structure-and-example)
8. [requirements.md structure and example](#requirementsmd-structure-and-example)
9. [design.md structure and example](#designmd-structure-and-example)
10. [tasks.md structure and example](#tasksmd-structure-and-example)
11. [Dependencies and cross-feature impact](#dependencies-and-cross-feature-impact)
12. [Change mode](#change-mode)
13. [Acceptance checklist](#acceptance-checklist)

## Contract invariants

- `specs/` is a sibling of `docs/` under the project root.
- `PLAN.md` contains an append-only source ledger and one current feature index. The ledger grows; the index is updated in place and contains exactly one row per feature.
- `LESSONS.md` is an append-only ledger of confirmed, reusable decisions and supersession records. Never edit or delete an earlier row.
- Every ready feature has exactly three requirement-authority documents: `requirements.md`, `design.md`, and `tasks.md`. A new `⏸ BLOCKED` feature may temporarily contain only `requirements.md` with its open questions. A blocked change to an existing feature preserves all published documents and version history unchanged and does not create the next version.
- After execution starts, `$atu-ai` may create optional `verification.md` as an execution-evidence ledger. It is not requirement, design, or task authority. `$atu-prd` never creates or updates it in any mode and never counts it among the three authority documents or toward the task limit; when it exists, read it only to avoid deletion or overwrite and preserve it unchanged.
- PRD work writes specifications only. It never implements application behavior.
- Every material claim is traceable to an authoritative source or a confirmed answer.
- An assumption remains an open question. A proposed option is not a decision.
- Every feature task list conforms to the canonical active-task checkbox and counting rule below.
- Feature dependencies form a directed acyclic graph and determine the recommended execution order.
- IDs are permanent. Never renumber, recycle, or erase an ID after publication.

## Output layout

```text
project/
  docs/
    product-requirement.md
  specs/
    PLAN.md
    LESSONS.md
    1.account-session/
      requirements.md
      design.md
      tasks.md
      verification.md  # optional execution evidence created by $atu-ai
    2.profile-access/
      requirements.md
      design.md
      tasks.md
```

For an existing project, preserve prior batches and directories. Assign new feature numbers after the highest existing number.

## Authoritative source discovery

- For a project directory or `.`, recursively read only `docs/**/*.md` and `docs/**/*.txt` by default.
- Include a readable `.pdf` or `.docx` only when the user explicitly names that file. Do not discover those formats implicitly.
- Exclude paths or files identified as archive, backup, superseded, or generated output, including anything under `specs/`. Match these labels case-insensitively and record every exclusion in the PLAN source ledger.
- If `docs/` is absent or no eligible source remains, stop and report the condition.
- For one named requirement file, use only that file. Infer the project root from its `docs/` ancestor or repository evidence; ask when `specs/` placement remains ambiguous.
- Record source paths, versions or dates, mode, explicit user confirmations, and exclusions. When eligible sources conflict, report both claims and the affected features; do not silently select one.

## Status, checkbox, version, and ID conventions

### PLAN status values

Use only:

| Value | Meaning |
| --- | --- |
| `待开发` | Specification is ready but implementation has not started. |
| `🚧 开发中` | The implementation workflow has actually started active work. PRD authoring never sets this value. |
| `✅ 完成` | All active tasks and acceptance criteria have verified evidence. |
| `⏸ BLOCKED` | The feature or an upstream contract has an unresolved blocking decision. New features may publish requirements/open questions only; existing features retain their last published version. |

`$atu-prd` creates ready features as `待开发` and unresolved features as `⏸ BLOCKED`. If change mode adds an active task to a `✅ 完成` feature, update that feature's current PLAN index row to `待开发`. Only the implementation workflow may set `🚧 开发中` after work actually starts or return the feature to `✅ 完成` after the new task and acceptance evidence are verified.

### Task checkbox, change tags, and counting

An **active top-level task checkbox** is a non-dropped top-level line in `tasks.md` beginning `- [ ] T-NNN:` or `- [x] T-NNN:`. Count both incomplete and completed active work. A feature may have at most eight such lines. Nested checkboxes are forbidden. Checkboxes or evidence entries in optional `verification.md` do not count.

- `- [ ] T-001: Add request validation ~15min` for active, incomplete work.
- `- [x] T-001: Add request validation ~15min` for verified completed work.
- `- [ ] T-008: [NEW v2] Add organization revocation ~30min` for work added in a change.
- `- [ ] T-003: Retain current-session revocation ~15min [CHANGED v2: organization revocation is now separate]` for an incomplete task revised by a change.
- `- ~~T-004: Add the retired client action ~15min~~ [DROPPED v2: the confirmed flow no longer exposes it]` for an incomplete task ID retired from the prior version. It has no checkbox and does not count toward the limit.

Only a prior-version incomplete `[ ]` task may become a dropped history row. Never change or retire an existing `[x]` task during PRD change processing. If new work is needed because completed behavior must change, add a new task with a new ID and link it to the completed task.

### Versions

- Start each authority document at `v1`.
- In change mode, increment only affected authority documents to the next integer version.
- Append version rows; never rewrite version history.
- Use the current calendar date in `YYYY-MM-DD`.
- Optional `verification.md` is an execution-evidence ledger and does not participate in authority-document version rules.

### Stable IDs

| Entity | Local format | Cross-feature format | Example |
| --- | --- | --- | --- |
| Feature | `N.kebab-case` | same | `2.profile-access` |
| Functional requirement | `F-001` | `N.F-001` | `2.F-001` |
| Non-functional requirement | `NFR-001` | `N.NFR-001` | `2.NFR-001` |
| Acceptance criterion | `AC-001` | `N.AC-001` | `2.AC-001` |
| Technical decision | `D-001` | `N.D-001` | `2.D-001` |
| Open question | `OQ-001` | `N.OQ-001` | `2.OQ-001` |
| Task | `T-001` | `N.T-001` | `2.T-001` |
| Reusable lesson | `L-001` | global; no prefix | `L-001` |

Rules:

1. IDs are local inside one feature document and fully qualified across features.
2. Allocate monotonically. Deletion retires an ID; it does not free it.
3. A renamed feature keeps its numeric prefix.
4. Every functional and non-functional requirement maps to at least one acceptance criterion.
5. Every active task lists the requirement IDs it implements and acceptance IDs it verifies.
6. Acceptance criteria remain observable and atomic. Split criteria joined by unrelated outcomes.

## Blocking-question gate

Block only the affected feature and any downstream consumer when an unanswered question can change:

- pricing, entitlement, payment, refunds, or another business invariant;
- actor authorization, tenant/data ownership, privacy, sensitive operations, or abuse controls;
- data source of truth, retention, deletion, migration, compatibility, or destructive behavior;
- an external service or protocol contract;
- feature boundaries enough to change the dependency graph or push a feature beyond eight tasks.

Use this form:

```text
OQ-001 — Who owns an uploaded record after an organization transfer?
Why it blocks: the answer changes authorization checks and retention behavior.
Affected features: 1.account-session, 2.profile-access.
Options evidenced by the source: organization ownership / creator ownership.
Decision required from: product owner.
```

Do not pick the recommended option. For a new feature, write `requirements.md` with numbered open questions and do not create final `design.md` or `tasks.md`. For a change to an existing feature, preserve all current feature documents and version rows exactly; record the blocker in the PLAN source event and handoff, and do not generate or publish the next document versions. Set the current PLAN index row to `⏸ BLOCKED`, continue independent features, and end the run `DONE_WITH_CONCERNS`. Non-blocking editorial questions may remain in `requirements.md`, clearly labeled with owner and impact.

## PLAN.md structure and example

Use all sections below. The source ledger is append-only; the current feature index, graph, and contract tables represent current state and are updated in place.

```markdown
# Development Plan Index

## Source ledger (append-only)

| Event | Date | Mode | Included authority | Exclusions and conflicts | Resolution |
| --- | --- | --- | --- | --- | --- |
| `SRC-001` | 2026-07-23 | new | `docs/account-access.md`, v1.2 | `docs/archive/account-access-v0.md` excluded as superseded | Product owner confirmed v1.2 |

## Current feature index

| Order | Feature | Delivery scope | Depends on | Status |
| --- | --- | --- | --- | --- |
| 1 | `1.account-session` | Create and revoke authenticated sessions | - | 待开发 |
| 2 | `2.profile-access` | Show the signed-in user's private profile | `1.account-session` | 待开发 |

## Feature dependency graph

`1.account-session` → `2.profile-access`

The graph is acyclic. Recommended execution order: `1` → `2`.

## Cross-feature contracts

| Provider | Consumer | Stable contract | Referenced IDs |
| --- | --- | --- | --- |
| `1.account-session` | `2.profile-access` | Feature 1 creates and returns an opaque session ID for Feature 2 to consume. | `1.F-001`, `1.AC-001`, `2.T-001` |

## ID convention

- IDs are local within a feature.
- Cross-feature references use the numeric feature prefix, such as `2.T-001 depends on 1.T-003`.
- Published IDs are never renumbered or reused.
```

PLAN consistency rules:

- Append one new source-ledger row for every new or change input; never edit or delete earlier source events.
- Maintain exactly one current feature index. Insert a new feature once, then update that row in place for dependency, scope, order, or status changes. Never append another batch table or duplicate a feature.
- Every numbered feature directory appears exactly once in the current feature index.
- Every dependency target exists.
- Table dependencies and the graph say the same thing.
- The recommended order is a valid topological order.
- Independent features may share the same execution stage; do not invent dependencies merely to make a linear list.

## LESSONS.md structure and example

Create this file once as an append-only ledger of confirmed, reusable knowledge. Do not duplicate feature requirements, store open questions, or claim that unimplemented work succeeded.

```markdown
# Specification Lessons

## Lesson ledger (append-only)

| ID | Date | Record type | Subject | Confirmed decision or constraint | Supersedes | Source | Applies to |
| --- | --- | --- | --- | --- | --- | --- | --- |
| L-001 | 2026-07-23 | decision | Session persistence | Use the existing Redis-backed server-side session store; clients hold only opaque tokens. | - | `docs/account-access.md` section 4 | All authenticated features |
| L-002 | 2026-08-02 | supersession | Session persistence | Use the existing database-backed server-side session store while retaining opaque client tokens. | `L-001` | `docs/session-storage-v2.md` section 2 | All authenticated features |
```

Never edit or mark an earlier row. When a confirmed decision replaces one, append a `supersession` row whose `Supersedes` cell points to the earlier ID. Resolve the current rule by following the latest supersession chain.

## requirements.md structure and example

Use every section. Write behavior and outcomes, not implementation instructions.

```markdown
# Account Session — Requirements

## Overview

Allow a registered user to create and revoke a private authenticated session.

## Scope and authoritative sources

- Feature: `1.account-session`
- Project: `example-app`
- Architecture: web client with HTTP API
- Source: `docs/account-access.md`, version 1.2, sections 2-5
- In scope: sign-in, invalid-credential handling, sign-out
- Out of scope: registration, password recovery, profile display

## Requirement version

| Date | Version | Description |
| --- | --- | --- |
| 2026-07-23 | v1 | Initial confirmed requirements |

## Actors and permissions

| Actor | Allowed behavior | Prohibited behavior |
| --- | --- | --- |
| Registered user | Create and revoke their own session | Read or revoke another user's session |
| Anonymous visitor | Submit credentials | Access authenticated resources |

## User stories

- As a registered user, I want to sign in so that I can access my private data.
- As a signed-in user, I want to sign out so that the current client can no longer use my session.

## Functional requirements

1. [F-001] A registered user can create a session with valid credentials.
2. [F-002] Invalid credentials return a generic denial without revealing whether an account exists.
3. [F-003] A signed-in user can revoke the current session.

## Non-functional requirements

1. [NFR-001] Credential and session secrets are never written to application logs.
2. [NFR-002] Authentication failures use the project's documented rate limit.

## Business and data rules

- Session ownership belongs to exactly one user.
- Revocation invalidates the current opaque token.
- The source does not authorize cross-device global sign-out.

## Acceptance criteria

- [ ] [AC-001] Given valid credentials for an active account, when sign-in completes, then one opaque authenticated session ID is returned. Covers: `F-001`.
- [ ] [AC-002] Given an unknown account or incorrect secret, when sign-in is attempted, then both cases return the same public error shape. Covers: `F-002`.
- [ ] [AC-003] Given the current valid session, when sign-out completes, then subsequent use of that token is unauthorized. Covers: `F-003`.
- [ ] [AC-004] Given failures above the configured threshold, when another attempt occurs, then the documented rate-limit response is returned. Covers: `NFR-002`.
- [ ] [AC-005] Given any authentication attempt, when application logs are inspected, then no credential or session secret is present. Covers: `NFR-001`.

## Dependencies

- External: the existing credential verifier and rate-limit configuration.
- Feature: none.

## Constraints

- Preserve the repository's existing authentication error envelope.
- Do not expose account-existence signals.

## Open questions

None. All blocking business, security, and data decisions for this feature are confirmed.
```

Requirements checks:

- Scope exclusions prevent adjacent behavior from leaking into the feature.
- Each actor has an explicit authorization boundary.
- Every `F-*` and `NFR-*` is covered by one or more `AC-*`.
- Acceptance criteria state observable outcomes and do not prescribe internal code.

## design.md structure and example

Use every section. Design choices must follow repository evidence and must reference the requirements they satisfy.

```markdown
# Account Session — Technical Design

## Design version

| Date | Version | Description |
| --- | --- | --- |
| 2026-07-23 | v1 | Initial design for `F-001` through `F-003` |

## Context and constraints

- Feature: `1.account-session`
- Architecture: web client with HTTP API and existing session store
- Governing guidance: repository `AGENTS.md`
- Preserved contract: existing authentication error envelope

## Affected layers and boundaries

| Layer | Responsibility | Requirement IDs |
| --- | --- | --- |
| API | Validate requests and return the public error envelope | `F-001`, `F-002`, `F-003` |
| Domain service | Verify credentials and own create/revoke rules | `F-001`, `F-003` |
| Session store | Persist opaque session state and revocation | `F-001`, `F-003` |
| Client | Submit sign-in and sign-out actions without persisting secrets | `F-001`, `NFR-001` |

## Module design

### Session creation

The API delegates credential checking to the existing verifier. Both unknown-account and incorrect-secret failures pass through one public denial path. Successful verification creates one server-side session associated with the user ID.

### Session revocation

Sign-out resolves the current session, revokes that session only, and returns the existing success envelope. Already-invalid sessions follow the repository's current unauthorized behavior.

## Interface contracts

| Interface | Input | Success | Failure |
| --- | --- | --- | --- |
| `POST /api/session` | Existing credential request shape | Opaque session ID and documented expiry | Generic invalid-credential error or rate-limit response |
| `DELETE /api/session/current` | Current session credential | Existing success envelope | Existing unauthorized envelope |

## Data model and lifecycle

- Reuse the existing session record and store; no new table is authorized.
- Store the user ID, opaque-token digest, expiry, and revocation state.
- Apply the existing retention and expiry jobs; no migration is required.

## Security and privacy

- Compare secrets through the existing verifier.
- Keep credential and token values out of logs, analytics, and public errors.
- Enforce ownership from the resolved current session; never accept a user ID from the client for revocation.
- Apply the configured authentication rate limit.

## Errors, observability, and recovery

- Preserve public error codes and HTTP statuses evidenced in the repository.
- Emit only non-sensitive success/failure counters already permitted by project guidance.
- Session creation failure leaves no partial session record.

## Verification strategy

- Unit verification covers generic denial and current-session revocation.
- API verification covers success, invalid credentials, unauthorized sign-out, and rate limiting.
- Security review verifies that logs and public responses contain no secret or account-existence signal.

## Rollout and rollback

- No schema migration is required.
- Roll back the API and client changes together if the preserved envelope is violated.

## Technical decisions

| ID | Decision | Evidence and reason | Requirement IDs |
| --- | --- | --- | --- |
| D-001 | Reuse the existing server-side session store. | Repository evidence and the source both require opaque client tokens. | `F-001`, `F-003`, `NFR-001` |

## Cross-feature impact

- Provides the session-ID creation contract consumed by `2.profile-access`.
- Contract reference: `1.AC-001` → `2.T-001`.

## Open design questions

None.
```

Design checks:

- Do not introduce a new framework, service, schema, or protocol without source evidence or confirmation.
- Include unhappy paths, authorization, data lifecycle, verification, and rollback where relevant.
- A technical recommendation remains in open questions until confirmed.

## tasks.md structure and example

Use the canonical [task checkbox, change-tag, and counting rules](#task-checkbox-change-tags-and-counting). Each active task represents the smallest independently verifiable `function × layer` slice. Estimates are `~5min`, `~15min`, or `~30min`, and a task over 30 minutes must be split.

```markdown
# Account Session — Task List

## Task version

| Date | Version | Description |
| --- | --- | --- |
| 2026-07-23 | v1 | Initial implementation slices |

## Project information

- Project: `example-app`
- Feature: `1.account-session`
- Specs path: `specs/1.account-session/`
- Top-level task count: 6
- Estimated total: 150 minutes

## Tasks

### Session API and domain

- [ ] T-001: Add session-creation request validation and the preserved response envelope ~30min — Implements: `F-001`, `F-002`; Verifies: `AC-001`, `AC-002`.
- [ ] T-002: Connect session creation to the existing credential verifier and session store ~30min — Implements: `F-001`; Verifies: `AC-001`.
- [ ] T-003: Add current-session revocation in the domain and store boundary ~30min — Implements: `F-003`; Verifies: `AC-003`.

### Client behavior

- [ ] T-004: Connect sign-in and sign-out actions without persisting credentials ~30min — Implements: `F-001`, `F-003`; Verifies: `AC-001`, `AC-003`.

### Verification

- [ ] T-005: Add API tests for success, generic denial, and current-session revocation ~15min — Implements: `F-001`, `F-002`, `F-003`; Verifies: `AC-001`, `AC-002`, `AC-003`.
- [ ] T-006: Add rate-limit and secret-exposure regression checks ~15min — Implements: `NFR-001`, `NFR-002`; Verifies: `AC-004`, `AC-005`.

## Dependency order

- `T-002` depends on `T-001`.
- `T-003` depends on `T-001`.
- `T-004` depends on `T-002` and `T-003`.
- `T-005` depends on `T-002` and `T-003`.
- `T-006` depends on `T-002`.
- Cross-feature: none.

## Traceability matrix

| Requirement | Acceptance | Tasks |
| --- | --- | --- |
| `F-001` | `AC-001` | `T-001`, `T-002`, `T-004`, `T-005` |
| `F-002` | `AC-002` | `T-001`, `T-005` |
| `F-003` | `AC-003` | `T-003`, `T-004`, `T-005` |
| `NFR-001` | `AC-005` | `T-006` |
| `NFR-002` | `AC-004` | `T-006` |

## Risks

- Public error divergence could reveal account existence; retain the shared failure path and verify both cases together.

## Completion definition

- Every active task is `[x]`.
- Every acceptance criterion has recorded verification evidence.
- Required tests, review, and repository checks pass.
- `PLAN.md` may then be updated by the implementation workflow.
```

Task rules:

- Do not write `implement authentication` as one task; split by independently testable layer and behavior.
- Do not combine unrelated work to satisfy the canonical task limit.
- If the active count would exceed the limit, split the feature, allocate a new feature number, and update `PLAN.md`.
- Preserve completed tasks in change mode. New behavior after completed work receives a new task ID.

## Dependencies and cross-feature impact

For each feature, identify:

1. Inputs it requires from another feature.
2. Outputs or stable contracts it provides.
3. Shared interfaces, tables, messages, states, or authorization rules.
4. Downstream acceptance criteria and tasks that consume those contracts.

Write dependencies as full IDs when referring outside the current feature. Cross-feature acceptance references always use `N.AC-NNN`; never use a bare `AC-NNN` outside its owning feature:

```text
2.T-001 depends on 1.T-002 and verifies 1.AC-001 as a consumer.
```

Impact analysis follows both directions:

- Provider change: inspect every consumer listed in `PLAN.md` and every full-ID reference.
- Consumer change: verify whether the provider contract must change or only the consumer behavior.
- Shared data/interface change: inspect all readers, writers, migrations, compatibility behavior, and rollback implications.
- Dependency removal: update the table, graph, task dependencies, design impact sections, and recommended order together.

A dependency cycle is a specification defect. Split shared contracts into a predecessor feature or revise boundaries; do not publish a cyclic plan.

## Change mode

Invocation:

```text
$atu-prd --change 1.account-session replace current-session sign-out with organization-wide sign-out
```

Apply this sequence:

1. Resolve the entry feature from the current PLAN index; a bare number may match exactly one `N.*` directory.
2. Read `PLAN.md`, `LESSONS.md`, all three authority documents, and optional `verification.md` read-only for the entry feature. Inventory any other feature files without deleting or overwriting them.
3. Follow dependency and shared-contract references to enumerate every affected feature before editing.
4. Compare the confirmed change with current IDs and classify each item as added, modified, retired, or unaffected.
5. Run the blocking-question gate per affected feature. Organization-wide sign-out, for example, requires confirmed authorization, ownership, and audit behavior. A new blocked feature receives requirements/open questions only. A blocked change preserves every existing feature document and version row and publishes no next version. Mark either case `⏸ BLOCKED` and continue independent features.
6. Append one event to the PLAN source ledger. Update the single current feature index in place; never append a duplicate feature row.
7. For unblocked features, increment only affected authority documents and record each document's old and new version. Preserve optional `verification.md` and unrecognized files unchanged.
8. Preserve old IDs and history. Retire only requirement/acceptance IDs or incomplete task IDs that exist in the prior version. Never modify or retire a completed `[x]` task; add new task IDs for changed completed behavior:

```markdown
3. [F-003] ~~A signed-in user can revoke the current session.~~ [DROPPED v2: replaced by confirmed organization-scoped revocation]
4. [F-004] Organization administrators can revoke sessions owned by their organization. [NEW v2]

- [AC-003] ~~Given the current valid session, when sign-out completes, then subsequent use of that token is unauthorized.~~ [DROPPED v2: `F-003` retired]
- [ ] [AC-006] Given an authorized organization administrator, when organization sign-out completes, then every session owned by that organization is unauthorized. Covers: `F-004`.

### Preserved completed v1 tasks

- [x] T-003: Add current-session revocation in the domain and store boundary ~30min — Implements: `F-003`; Verifies: `AC-003`.
- [x] T-004: Connect sign-in and sign-out actions without persisting credentials ~30min — Implements: `F-001`, `F-003`; Verifies: `AC-001`, `AC-003`.

### New v2 tasks

- [ ] T-007: [NEW v2] Add organization-scoped revocation authorization ~30min — Implements: `F-004`; Verifies: `AC-006`.
- [ ] T-008: [NEW v2] Replace the completed current-session route and client action with organization-scoped sign-out ~30min — Implements: `F-004`; Verifies: `AC-006`; Depends on: `T-003`, `T-004`.
```

9. Update all affected acceptance mappings, design decisions, cross-feature impacts, task dependencies, and traceability matrices.
10. Update current PLAN dependencies, order, status, and contracts in place. If a `✅ 完成` feature gains an active task, set it to `待开发`. Only the implementation workflow may later set `🚧 开发中` or restore verified `✅ 完成`.
11. Append to `LESSONS.md` only for a confirmed reusable decision or supersession; never edit an earlier row.
12. Apply the canonical active-task counting rule and split a feature when required.

Change summary format:

```text
Affected features: 1.account-session, 2.profile-access

1.account-session
  requirements.md: v1 → v2
  design.md: v1 → v2
  tasks.md: v1 → v2
2.profile-access
  requirements.md: unchanged at v1
  design.md: v1 → v2
  tasks.md: v1 → v2

Added: 1.F-004, 1.AC-006, 1.T-007, 1.T-008
Changed: the 1 → 2 cross-feature contract
Retired existing v1 IDs: 1.F-003, 1.AC-003
Preserved completed tasks unchanged: 1.T-003, 1.T-004
PLAN.md: source event appended; current dependency, contract, and status rows updated in place
Status: 1.account-session `✅ 完成` → `待开发` because new active tasks exist
LESSONS.md: supersession row L-003 appended; prior rows unchanged
```

## Acceptance checklist

### Authority and decision quality

- [ ] Input selection conforms to [authoritative source discovery](#authoritative-source-discovery), and the source ledger records included paths, versions/dates, mode, exclusions, confirmations, and conflicts.
- [ ] Conflicting source claims are reported with affected features and are not silently resolved.
- [ ] Facts, confirmed decisions, open questions, and out-of-scope items are distinguishable.
- [ ] No material decision is assumed; unresolved decisions follow the [blocking-question gate](#blocking-question-gate).
- [ ] No application code or non-specification project file was changed.

### Feature graph and scope

- [ ] Every feature is cohesive and independently verifiable.
- [ ] Existing specifications were checked for duplication or overlap.
- [ ] `PLAN.md` follows its [ledger, current-index, graph, and order rules](#planmd-structure-and-example), with no duplicate feature row.
- [ ] A blocker affects only its dependent feature and downstream consumers; independent ready features continue.
- [ ] Cross-feature providers, consumers, contracts, and full-ID references agree, including qualified `N.AC-NNN` acceptance IDs.

### Document completeness

- [ ] `PLAN.md` exists even for one feature.
- [ ] `LESSONS.md` follows its [append-only supersession contract](#lessonsmd-structure-and-example); no earlier row was edited or deleted.
- [ ] Every ready feature contains exactly the three authority documents; a new `⏸ BLOCKED` feature contains requirements/open questions only, while a blocked change preserves all previously published documents and creates no next version.
- [ ] Optional `verification.md`, when present, is treated only as `$atu-ai` execution evidence: `$atu-prd` never creates or updates it in any mode, reads it only to prevent deletion or overwrite, preserves it unchanged, and does not count it as authority or task work.
- [ ] Every authority document starts at `v1`.
- [ ] Local links resolve and no unfinished authoring marker remains.

### IDs, acceptance, and tasks

- [ ] IDs and cross-feature references conform to the [stable-ID rules](#stable-ids).
- [ ] The traceability matrix has one row per requirement; every active requirement maps to acceptance and active task IDs.
- [ ] Every acceptance criterion is observable and atomic; every cross-feature acceptance reference is fully qualified.
- [ ] Tasks conform to the [checkbox, tag, and active-count rule](#task-checkbox-change-tags-and-counting), and every active task states `Implements` and `Verifies` IDs.
- [ ] Each task follows the [task slice and estimate contract](#tasksmd-structure-and-example).

### Change-mode integrity

- [ ] All affected features were identified before edits.
- [ ] One source event was appended and the single current feature index was updated in place without duplicating a feature.
- [ ] Only affected authority-document versions were incremented, and every affected authority document's old and new version is reported.
- [ ] Optional `verification.md` and unrecognized feature files are preserved unchanged.
- [ ] Completed `[x]` tasks are byte-for-byte preserved.
- [ ] New and changed active tasks retain estimates; each dropped task is a non-checkbox history row for an incomplete `[ ]` ID from the prior version, and no completed `[x]` task is modified or retired.
- [ ] A previously completed feature with new active tasks is `待开发`; only the implementation workflow may set `🚧 开发中` after work starts or restore `✅ 完成` after verification.
- [ ] Dependency, order, traceability, status, and append-only lesson changes are synchronized.

### Handoff

- [ ] The report lists included/excluded sources, mode, changed files, per-authority-document version transitions, dependency order and status, active task counts and estimates, open questions, and checks actually run.
- [ ] Final status is `DONE` only when every feature has final specifications and no blocker; otherwise it is `DONE_WITH_CONCERNS` and distinguishes ready independent features from blocked features.
- [ ] The handoff asks for specification review before `$atu-ai` and does not start implementation.
