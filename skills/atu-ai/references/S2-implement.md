# S2: Implement one task

Keep one active task and one coherent write boundary. Tasks with ordering, shared-state, or overlapping-file dependencies remain serial.

## Prepare

Re-read the task, mapped requirements, relevant design decisions, acceptance criteria, current target files, effective `AGENTS.md`, and current diff. Read only guidance needed for the changed boundary:

- Web UI and browser acceptance: [Frontend](domains/frontend.md).
- API, service integration, or queue behavior: [Backend](domains/backend.md).
- Schema, migration, transaction, or Redis behavior: [Database](domains/database.md).
- Test-only work or acceptance evidence: [Verification](verification.md).

Use `$atu-android-engineer` or `$atu-miniprogram-engineer` for native platform work. Ordinary edits need no extra role context; a change spanning relevant boundaries may use more than one reference. Reading verification guidance does not create an independent QA pass; S3 decides when one is needed.

## Implement test-first

1. Add or tighten the narrowest meaningful automated test and observe the expected RED failure. If automation is not feasible, state why and define concrete manual evidence before changing behavior.
2. Make the smallest implementation that satisfies the approved contract and its applicable approved architecture baseline; otherwise preserve existing architecture. An approved target may intentionally differ from current code. A new consequential architecture choice returns affected work to `$atu-prd`/`$atu-architect`, not an improvised implementation decision.
3. Run the focused test to GREEN, then run relevant nearby regressions. Use repository-supported commands; do not introduce a tool only to manufacture a pass.
4. Inspect the task diff for correctness, error paths, authorization boundaries, compatibility, readability, test adequacy, and accidental noise.
5. Keep credentials, production data, dependency changes, destructive actions, and external writes within explicit authorization. Do not push, deploy, publish, migrate, or mutate production from this stage.

Record concise commands and outcomes in the stage report. When the task's required local evidence passes, check only that task and keep the feature `🚧 开发中`. Continue S2 for another ready task in the same feature. When all feature tasks are `[x]` or `[DROPPED]`, enter S3.

On an implementation or test failure, stay in S2 and repair only the evidence-backed defect. On a material unresolved decision, keep the task unchecked and return `BLOCKED`.
