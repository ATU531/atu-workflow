# S3: Verify the feature once

Verify the complete feature diff after its tasks finish. This is one combined gate, not a specification-review, quality-review, and QA pipeline repeated for every task.

## Combined verification

1. Re-read the feature contract, acceptance criteria, current repository status, complete feature diff, and task-level test evidence.
2. Run the relevant feature tests, regressions, and repository-supported static, type, build, migration, or security checks affected by the diff.
3. Self-review the complete diff against requirements, design, applicable approved architecture decisions (module dependencies, data ownership, shared contracts), correctness, error handling, authorization, compatibility, concurrency or lifecycle behavior, readability, and test adequacy. This adds no separate architecture audit round.
4. Build one feature acceptance matrix with current evidence for every criterion. Mark unavailable required evidence `NOT RUN`, `MANUAL REQUIRED`, or `BLOCKED` rather than substituting mocks or narrower tests.

After a fix, rerun the affected checks and the final regressions needed to establish a coherent current result. Do not restart unrelated gates whose evidence was not invalidated.

## Proportional independent checks

Ordinary standard work uses the combined verification above. Add one independent code review once per feature only when the implemented diff changes one of these critical boundaries:

- authentication or authorization;
- payment, money movement, or entitlement settlement;
- a destructive or irreversible migration or data operation;
- a public API or compatibility contract with real consumers;
- an explicitly authorized production change.

The independent reviewer uses `$atu-code-reviewer`, receives the exact feature contract and current diff, works read-only, and reports only evidence-backed blocking findings. Other reasons for standard mode—multiple tasks, cross-module coordination, additive schema work, external integration, or a broad but reversible change—do not automatically require a separate reviewer.

Use independent QA only when acceptance depends on a real browser, device, payment provider, external service, human operation, or when the user explicitly requests it. Run it once for the feature, not once per task. Give that verifier the [verification guidance](verification.md), selected acceptance criteria, reviewed scope, and available test evidence; code review alone does not establish runtime acceptance.

For a cross-session handoff or independent review, a commit or patch hash may pin the reviewed application snapshot. Do not compute a second specification hash or require hashes for a same-session combined check.

PASS enters S4. When current evidence proves an implementation or test defect, uncheck only the affected task, keep the feature `🚧 开发中`, and return that task to S2; do not disturb unrelated completed tasks. A verification-only gap stays in S3. A missing required real boundary remains truthfully blocked.
