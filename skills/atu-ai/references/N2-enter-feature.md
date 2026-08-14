# N2: Enter a ready feature

Select the next implementable feature without treating planning as implementation.

1. Read the feature's `requirements.md`, `design.md`, and `tasks.md` completely, then re-read relevant `PLAN.md` dependencies and `LESSONS.md` decisions.
2. Reconcile task states exactly: skip `[x]` and `[DROPPED]`; execute `[CHANGED]` from its current description; treat `[ ]` as active. Do not rewrite history or silently change scope.
3. Check upstream feature, schema, API, environment, and external-system dependencies against repository evidence. A stated dependency is satisfied only when its required contract is present and verified to the degree the current task needs.
4. Extract open questions and conflicts. A material unresolved business rule, security or authorization boundary, destructive data choice, external/interface contract, scope decision, or acceptance criterion blocks the affected feature and downstream dependents. Set its PLAN status to `⏸ BLOCKED` only when editing PLAN is authorized; otherwise report the required status change. Report the exact question and do not choose an answer implicitly.
5. A feature is ready only when its specifications are complete and internally consistent, required dependencies are satisfied, at least one active task is unblocked, and the task is inside the user's authorized scope.
6. Choose the earliest ready feature in dependency order. If the current feature is complete, move to the next ready feature. If it is blocked, continue only with an independent ready feature; otherwise stop with the blocker.
7. Build a dependency-aware task order. Keep tasks serial when they depend on one another, share state, or may edit the same files. Collaboration is optional and must satisfy the stricter rules in N3.
8. Report the selected feature, active/skipped/blocked tasks, dependency evidence, open questions, and intended task order.

Keep the feature's PLAN status unchanged while only reading, analyzing, or planning unless an unresolved decision requires an authorized `⏸ BLOCKED` update. If an environment, tool, credential, service, browser/device, or manual-verification blocker is found before any code or test implementation begins, preserve the current planned status (including `待开发`), keep the task unchecked, and record `execution blocked` only in `verification.md` when ledger writing is allowed and in the node report. Set PLAN to `🚧 开发中` only when actual implementation of the first active task begins; if implementation had already begun, retain `🚧 开发中` while the execution blocker remains. Never replace `✅ 完成` without verified new active work.
