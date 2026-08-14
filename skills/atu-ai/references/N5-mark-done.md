# N5: Mark a verified task done

Mark only the task whose exact current post-fix application snapshot and `spec_contract` both match the identities that passed N4 and N6. Completion bookkeeping is evidence, not optimism.

For a recovery-reopened task, N5 is the only node allowed to change it back from `[ ]` to `[x]`. Do so only after the recovery snapshot completes fresh N4 and N6 PASS; the old checkbox and old ledger evidence have no completion value.

## Completion gate

Before editing a checkbox, `PLAN.md`, or `LESSONS.md`:

1. Recompute and confirm both deterministic identities. Require the application snapshot hash value/algorithm/scope and `spec_contract` hash value/algorithm/scope to match N4 and N6 exactly; require the spec scope to include task description, mapped requirements, relevant design contract, and mapped acceptance criteria.
2. Confirm N4 reviewed the exact current task diff and reports every required test, static check, self-review, independent specification review, and independent quality review.
3. Confirm N6 evaluated every acceptance criterion mapped to this task under those same two identities and returned PASS. When this is the last active task, also confirm the same N6 run returned current full-feature acceptance-criterion and regression PASS. For a recovery-reopened task, confirm the ledger identifies the reopen reason, old/current application snapshots and spec contracts, and N5 as the next route after N6 PASS.
4. Confirm all required checks passed and neither independent review has an unresolved blocking finding.
5. Treat `FAIL`, `BLOCKED`, `NOT RUN`, `MANUAL REQUIRED`, stale evidence, either identity missing/mismatched, `snapshot=unverifiable`, `spec_contract=unverifiable`, or an unreviewed post-review edit as a failed gate. Invalidate old implementation, review, and QA evidence and return to N3 for an identity failure; otherwise return to N3 or N4 as N6 directs.

When the gate is not satisfied, leave the task checkbox unmarked. Report the exact blocker and do not make N5 bookkeeping changes.

## Update the task

1. Locate the exact current task in `tasks.md`.
2. Change only its checkbox from `- [ ]` to `- [x]`. Preserve its ID, wording, metadata, and surrounding content.
3. Re-read `tasks.md` immediately and verify that exactly the intended task is checked.
4. Never batch-mark tasks or mark work completed by another task's evidence.

## Reconcile feature status

Use repository evidence, not the age of the plan:

- Before any active task has actually begun implementation, preserve the existing planned or ready status.
- Once implementation of an active task has begun, the feature is `🚧 开发中`.
- Keep it `🚧 开发中` while any task remains active or has an execution blocker, or while required full-feature QA has not passed.
- Set it to `⏸ BLOCKED` for an unresolved business, security, authorization, destructive-data, external-contract, or scope decision.
- Set it to `✅ 完成` only when every task is `[x]` or `[DROPPED]` and the last required N6 run has current criterion-by-criterion evidence that all required full-feature QA and regressions passed on the current snapshot.

Re-read `PLAN.md` after any permitted status edit. If no `PLAN.md` exists, skip this step.

## Record durable lessons

After the completion gate passes, append to `LESSONS.md` only when the task produced a reusable architectural decision, non-obvious failure mode, cross-feature effect, or environment/dependency constraint. Use:

```text
## YYYY-MM-DD — Feature / Task
```

Do not record routine implementation, repeat existing entries, expose secrets, or rewrite unrelated lessons. Re-read the appended section after editing.

## Commit boundary

A successful N6 PASS followed by N5 is the earliest point at which a local commit is allowed. For a recovery-reopened task, commit is prohibited from the N7 reopen through N4 and N6; eligibility resumes only after N5 re-checks the task. Eligibility does not itself authorize a commit: commit only when the user explicitly requested it or effective project instructions expressly authorize or require it, and include only the exact N4/N6-verified task and bookkeeping files. Inspect the staged diff before committing. Never automatically push, publish, deploy, migrate, or broaden the release scope.

After successful bookkeeping, always enter N7 before selecting more work or finishing. Report the task checkbox evidence, N4/N6 snapshot evidence, PLAN status and reason, LESSONS change or deliberate skip, commit action or skip, and N7 as the next node.
