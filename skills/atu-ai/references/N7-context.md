# N7: Manage context

Treat repository files and the written plan as durable workflow state. Conversation memory is only a convenience and must not be the source of truth.

## Re-establish state at every task boundary

After N5 finishes, and before selecting or starting another task, re-read:

1. every effective `AGENTS.md` for the specs and files likely to be touched;
2. `PLAN.md`;
3. the current feature's `requirements.md`, `design.md`, and `tasks.md`;
4. relevant entries in `LESSONS.md`; and
5. each authorized repository's branch, `git status`, and relevant working-tree, staged, and untracked diff; and
6. the current feature's `verification.md`, unless the user prohibited that write.

Compare the current dirty state with the baseline recorded in N1 and the files attributed to the completed task. Preserve unrelated and concurrent changes. If the next task overlaps unexplained changes, stop and resolve ownership instead of guessing.

Reconstruct from those files:

- the authorized repositories and scope;
- completed, active, changed, dropped, and blocked tasks;
- satisfied and unresolved dependencies;
- the latest verified checks and QA boundaries; and
- the next ready task or feature.

Do not infer completion from an earlier chat summary when task boxes, PLAN status, QA evidence, or the current diff disagree.

## Verify the durable ledger

Generate the current deterministic commit hash, diff patch hash, or tree/content hash and compare it with the ledger. Also recompute the current deterministic `spec_contract` from normalized task description, mapped requirements, relevant design contract, and mapped acceptance criteria. Require both identities to match their hash values, algorithms, and scopes; require the spec scope to list exact files/sections/IDs and normalization rules. A file list or timestamp can describe application scope but cannot establish identity. Confirm that the ledger also carries implementation status and evidence, the N1 baseline dirty paths, tests/static exit codes, specification and quality review outcomes, acceptance-criterion matrix, blockers, and next route.

If either deterministic identity cannot be generated, record `snapshot=unverifiable` or `spec_contract=unverifiable` as applicable. If either identity is missing, unverifiable, or mismatched, invalidate all prior implementation, review, and QA evidence and route the task to N3 after any mandatory checked-task reopen. Do not attempt in-place re-proof or reuse evidence.

If ledger writing was prohibited, the ledger is missing, required fields are absent, its application snapshot does not match current code, or its `spec_contract` does not match current specification content, do not trust a checkbox, PLAN status, or chat summary as proof. Handle checked and unchecked tasks separately:

- For an unchecked task with no dual-identity-matching `implementation_complete` evidence because work never started, remains incomplete, or lacks concrete completion evidence, keep it unchecked and route to N3.
- For an unchecked task whose ledger has `implementation_complete` evidence matching both current deterministic identities, but whose review, QA, or downstream ledger evidence is missing or stale, route to N4 and then N6.
- An application snapshot or `spec_contract` mismatch means all prior implementation, review, and QA evidence is invalid. Route to N3 without an N7 re-proof exception.
- For an `[x]` task, perform the mandatory recovery transition below before any review or QA. Never route a stale checked task directly to N4 or N6.

## Atomically reopen an unverified checked task

This recovery bookkeeping is the only safe mutation N7 permits.

1. Before changing anything, confirm authority to update both `tasks.md` and `PLAN.md` for the exact task and feature, and authority to write its `verification.md`. If authority for `tasks.md` or `PLAN.md` is absent, or the required ledger write is prohibited, stop as `BLOCKED`. Do not alter only part of the state, continue to N4/N6, or trust the checkbox.
2. Freeze and hash both identities. Capture the old/current application snapshot type/value, hash algorithm, and hash scope, plus the old/current `spec_contract` value, spec hash algorithm, spec hash scope, and normalization rules, using `<missing>`, `snapshot=unverifiable`, or `spec_contract=unverifiable` where applicable. Treat old `implementation_complete`, review, and QA evidence as invalid when either identity differs or is unverifiable.
3. Apply one atomic recovery state transition without changing source or mutable implementation artifacts:
   - in `tasks.md`, change only its checkbox from `- [x]` to `- [ ]`;
   - in `PLAN.md`, set the feature being recovered to `🚧 开发中`; and
   - in `verification.md`, append the task ID, reopen reason, old/current application snapshot identities, old/current `spec_contract` identities, implementation status/evidence decision, timestamp, and the evidence-selected N3 or N4 next route, plus `COMMIT PROHIBITED DURING RECOVERY`.
4. Re-read all three files and verify every part of the transition. If any write failed or the three records disagree, stop as `BLOCKED`; do not proceed with a partial recovery.
5. Apply the unchecked-task evidence rules after reopening. Without `implementation_complete` evidence matching both current identities, route to N3. With dual-identity-matching implementation completeness and only later evidence missing, route N4 → N6. Keep commit prohibited; N6 PASS routes to N5 to re-check the task, an implementation/test failure returns to N3, and a review/evidence failure returns to N4.

Classify recovered blockers consistently: unresolved business, security, authorization, destructive-data, external-contract, or scope decisions set PLAN to `⏸ BLOCKED`; environment/tool/service/device gaps and pending manual verification keep PLAN `🚧 开发中` and the task unchecked.

## Automatic context compression

Codex may automatically compress a long conversation. Continue safely by performing the same state-recovery reads before any edit or node transition. Do not try to preserve progress through chat-only notes; write only the specification, plan, lesson, and task-state changes authorized by their designated nodes.

## Route after recovery

- Enter N3 when the current feature has another ready task, but only after the just-completed task's current N4/N6 evidence has been recovered.
- Enter N2 when the current feature is complete and another ready feature remains.
- For an unchecked task without `implementation_complete` evidence matching both current identities, enter N3.
- For an unchecked task with dual-identity-matching `implementation_complete` evidence but missing review, QA, or downstream ledger evidence, enter N4 then N6.
- For an application snapshot or `spec_contract` that is missing, mismatched, `snapshot=unverifiable`, or `spec_contract=unverifiable`, invalidate all older implementation, review, and QA evidence and enter N3 without exception.
- For an `[x]` task with unavailable, incomplete, stale, or snapshot-mismatched durable evidence, complete the atomic reopen first, then apply the same unchecked-task N3-or-N4 route. After N4 → N6 PASS enter N5 to re-check it; on failure return to N3 or N4 as classified.
- If the required recovery update to `tasks.md` or `PLAN.md` is unauthorized, stop as `BLOCKED` and do not continue based on the checkbox.
- Enter N8 only when no active task remains anywhere, every checkbox/status gate is satisfied, and the last required full-feature N6 QA and regressions passed under both current deterministic identities.
- If the remaining work is blocked and no independent ready task exists, report the blocker and stop without advancing it.

N7 is read-only workflow recovery except for synchronizing the authorized execution ledger and the single atomic checked-task reopen defined above. Report the recovered state, ledger freshness, reopen evidence when applicable, dirty-state changes, commit prohibition, selected route, and any conflict or blocker.

`$atu-prd` may preserve the ledger unchanged. Always recompute `spec_contract` here; do not assume unchanged ledger content means the specification contract is unchanged.
