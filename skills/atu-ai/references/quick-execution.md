# Compact ATU AI Execution

Execute one approved compact specification through Q1-Q4. Compact mode optimizes orchestration, not engineering evidence. Keep exactly one active task, one compact authority file, and one coherent implementation boundary.

## Entry contract

The selected `specs/quick/YYYYMMDD-feature-name.md` must contain:

- status `READY`, `IN_PROGRESS`, `DONE`, `ESCALATED`, or `BLOCKED`;
- goal, in-scope and out-of-scope boundaries, and reused stable contracts;
- compact-mode evidence and explicit escalation triggers;
- a bounded design with security, compatibility, error, and lifecycle invariants where relevant;
- no more than five observable `AC-Q01` through `AC-Q05` outcomes; and
- exactly one `T-Q01` implementation-and-verification task. It is unchecked in `READY` and `IN_PROGRESS`, checked in `DONE`, and preserved as recorded in `BLOCKED` or `ESCALATED`.

If required content is missing, multiple active tasks exist, or a strict trigger is present or uncertain, do not patch the compact contract in `$atu-ai`. Set or recommend `ESCALATED` with evidence and route to `$atu-prd`.

## Status routing

- `READY or IN_PROGRESS`: enter or resume Q1-Q4 after rechecking repository evidence and the dirty-work boundary.
- `BLOCKED`: report the recorded blocker and required owner/action. Re-evaluate only when the user says the blocking state changed; do not enter Q2.
- `ESCALATED`: preserve the file and route to standard `$atu-prd`; do not continue compact implementation.
- `DONE`: report that the bounded change is closed. A new change requires a new or promoted specification; never reopen `T-Q01` implicitly.

## Q1: Confirm eligibility and boundary

1. Read the compact spec, effective `AGENTS.md`, repository status and relevant diff, target code, callers, configuration, and nearby tests.
2. Record the pre-existing staged, unstaged, and untracked boundary without resetting, cleaning, stashing, overwriting, or absorbing it.
3. Confirm the change is one bounded behavior in one repository and a localized module or bounded vertical slice; its decisions are closed; existing auth, data, API, event, deployment, and external contracts remain stable; and focused verification is feasible.
4. Escalate on any new or changed authentication, authorization, privacy, payment, audit policy, schema, migration, backfill, retention or data-lifecycle rule, destructive operation, production configuration, deployment topology, external provider, callback, queue, public API, compatibility contract, cross-repository boundary, broad shared state, or independent task.
5. Announce the task, expected files, reused contracts, focused checks, and compact eligibility evidence. Do not mark work started while only reading.

When the first test or implementation edit begins, set the compact file to `IN_PROGRESS`. Do not create `PLAN.md`, `LESSONS.md`, numbered feature files, or a separate `verification.md`.

## Q2: Implement test-first

1. Read the task, design, acceptance outcomes, target implementation, and effective project rules again at the edit boundary.
2. Load only the smallest applicable domain skill: `$atu-frontend-engineer`, `$atu-backend-engineer`, `$atu-database-engineer`, `$atu-android-engineer`, `$atu-miniprogram-engineer`, or `$atu-qa-engineer` for test-only work.
3. Add or tighten the narrowest meaningful automated test and observe it fail for the expected missing behavior. If no safe automated test is feasible, record the reason and concrete manual evidence before implementation.
4. Make the smallest coherent change that satisfies the compact contract and existing architecture. Do not introduce speculative abstractions or unrelated cleanup.
5. Run the focused test until it passes, then run the relevant nearby regression checks.
6. Inspect the task diff and remove only task-introduced noise. Preserve unrelated changes.

If implementation reveals a strict trigger, stop before broadening the change. Preserve current edits, set the compact file to `ESCALATED`, record the evidence and affected boundary, and route to `$atu-prd`. Do not claim the partial implementation is verified.

## Q3: Verify once

Use one current task snapshot and one combined verification pass:

1. Run focused tests and only repository-supported static, compile, build, security, browser/device, or regression checks required by the changed behavior.
2. Review the complete task diff against the compact design, every `AC-Q*`, effective `AGENTS.md`, existing architecture, correctness, authorization boundaries, errors, concurrency/lifecycle behavior, compatibility, readability, and test adequacy.
3. Build a compact acceptance matrix with one current evidence row per criterion.
4. Fix implementation or test defects through Q2, then rerun this entire combined pass on the updated diff.
5. Report unavailable real browser, device, credential, external-service, or human evidence as `NOT RUN` or `MANUAL REQUIRED`; never replace a required real boundary with a mock-backed pass.

Do not create default independent specification-review, quality-review, or QA contexts in compact mode. If evidence indicates that independent gates or durable multi-session recovery are necessary, escalate to the standard workflow instead of recreating N4/N6 inside Q3.

## Q4: Close and report

Update only the selected compact file:

- list changed files and concise diff scope;
- record exact commands, environments, exit codes, pass/fail/skip counts, and useful concise outcomes;
- record each `AC-Q*` result and manual/external boundaries;
- check only `T-Q01` and set status `DONE` when all required local evidence passes;
- set `BLOCKED` when a required decision, environment, or verification boundary prevents completion; or
- retain `ESCALATED` when strict promotion is required.

Compact mode does not create a separate ledger, compute application/specification dual hashes, enter N7, scan unrelated features, or reopen historical standard tasks. It also does not authorize a commit or release action.

Return:

```text
COMPLETED
- <behavior and evidence completed>

BLOCKED
- <none or exact unfinished decision/check/boundary>

NEXT STEP
- <none or smallest concrete action and owner>
```

Use `DONE` only when `BLOCKED` is empty.

## Interruption recovery

On a later run, re-read the compact file, repository status, target diff, pre-existing dirty boundary, and nearby tests. Rerun focused verification instead of trusting a chat summary. Continue Q2 or Q3 only when scope and ownership remain clear. If reliable recovery requires durable identities, multiple tasks, or broad context reconstruction, set `ESCALATED` and promote to the standard workflow.
