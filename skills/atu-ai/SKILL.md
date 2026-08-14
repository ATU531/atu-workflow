---
name: atu-ai
description: Use when the user invokes $atu-ai or asks to continue specification-driven development from an existing specs/PLAN.md through implementation, review, QA, completion tracking, and documentation synchronization.
---

# ATU AI

Continue an approved specification set through implementation. Treat `specs/PLAN.md`, each feature's `requirements.md`, `design.md`, and `tasks.md`, plus `specs/LESSONS.md`, as the delivery contract. Use `specs/<feature>/verification.md` only as a durable execution-evidence ledger; it never overrides requirements, design, tasks, or acceptance criteria.

## Hard gates

- Read the current node reference completely every time before executing that node. Never skip, merge, reorder, or claim a node completed early.
- Keep work within the user's authorized repositories, features, tasks, and environments. A node transition never expands authorization.
- Preserve pre-existing and concurrent user changes. Never clean, reset, discard, overwrite, or hide unrelated work.
- Stop for unresolved business, security, authorization, destructive-data, external-contract, or scope decisions. N1 records and routes the decision without editing PLAN; N2 sets the affected feature's PLAN status to `⏸ BLOCKED` only when that specification write is authorized. Do not invent a decision to keep the workflow moving.
- Treat missing environments, tools, credentials, services, browsers/devices, and pending manual verification as execution blockers. Before any code or test implementation has begun, preserve the existing planned status (including `待开发`) and record the blocker only in `verification.md` and the node report. After implementation has begun, keep the feature `🚧 开发中`. In both cases keep the affected task unchecked; never misclassify the blocker as a pass or a PLAN decision block.
- Treat tests, static checks, reviews, migrations, browser/device checks, releases, and deployments as passed only when current evidence proves they passed. Record unavailable or blocked checks truthfully.
- Identify every application-code snapshot deterministically with a commit hash, diff patch hash, or tree/content hash. Record the hash algorithm and hash scope. A changed-file list or timestamp is metadata only and can never identify a matching snapshot. If no deterministic hash can be generated, record `snapshot=unverifiable`, invalidate all prior implementation, review, and QA evidence, and route to N3.
- Bind every task to a deterministic `spec_contract` identity. Record its hash value, hash algorithm, normalization rules, and hash scope covering at least the normalized task description, mapped requirements, relevant design contract, and mapped acceptance criteria. If it cannot be hashed, record `spec_contract=unverifiable`.
- Synchronize current evidence to `verification.md` at N1, N3, N4, N6, N7, and N8 unless the user prohibits that write. Record `implementation_complete`, review, or QA evidence only when both the deterministic application snapshot and `spec_contract` match current content. If either identity is missing, unverifiable, or mismatched, invalidate all prior implementation, review, and QA evidence and route to N3. Never record secrets or raw sensitive logs.
- N7 routes an unchecked task to N4 → N6 only when its ledger has `implementation_complete` evidence matching both current identities and only later review/QA evidence is missing. Without both identities and implementation evidence, route to N3; there is no in-place re-proof exception for an identity mismatch.
- When N7 finds an already `[x]` task whose ledger is missing, stale, incomplete, or identity-mismatched, never validate it in place. With authority for all required bookkeeping writes, atomically reopen it to `[ ]`, set its feature to `🚧 开发中`, and record the reopen reason, old/current application snapshots and spec contracts, implementation-evidence decision, and N3 or N4 next route in the ledger. Prohibit commits throughout recovery; only the dual-identity-matching implementation-complete path may enter N4 → N6, and only N6 PASS followed by N5 may re-check the task and restore commit eligibility. Without authority to update `tasks.md` and `PLAN.md`, stop as `BLOCKED` and do not trust the checkbox.
- `$atu-prd` may preserve an existing verification ledger unchanged. On the next `$atu-ai` run, recompute `spec_contract`; changed requirements, design, task text, or acceptance criteria invalidate old evidence automatically.
- Never push, publish, deploy, migrate production data, or perform another release action automatically. Do so only after an explicit user request and the applicable project workflow.

## State machine

Execute this state machine exactly:

```text
N1 Initialize
  -> N2 Enter ready feature
  -> N3 Execute one task
  -> N4 Review that task
       -> N3 for an implementation/test fix
       -> N4 to close a review/evidence gap
       -> N6 only after N4 PASS
  -> N6 QA mapped acceptance criteria on the current task snapshot
       -> N3 for an implementation/test fix
       -> N4 to close a review/evidence gap
       -> N5 only after N6 PASS
  -> N5 Mark the N6-verified task complete; optionally make an authorized local commit
  -> N7 Manage context
       -> N3 when the feature has another ready task
       -> N2 when another ready feature remains
       -> N3 without dual-identity-matching implementation_complete evidence
       -> N4 then N6 with dual-identity-matching implementation_complete but missing later evidence
       -> atomically reopen an unverified [x] task, then apply the same N3-or-N4 evidence route
       -> N5 to re-check a recovery task only after N6 PASS
       -> N8 only when no active task remains and the last required full-feature QA passed
N8 Finish (terminal)
```

A blocked feature may yield to an independent ready feature. If no authorized ready work remains, report the exact blocker and stop without advancing the blocked node.

After each completed node except N8, report:

```text
✓ [node name] complete; entering [next node name]
```

N8 is terminal. Use its final-report contract and do not claim that it is entering a next node.

## Node routing

Read the mapped reference before every node execution:

- N1: [Initialize](references/N1-init.md)
- N2: [Enter feature](references/N2-enter-feature.md)
- N3: [Execute task](references/N3-execute-task.md)
- N4: [Review](references/N4-review.md)
- N5: [Mark done](references/N5-mark-done.md)
- N6: [QA evaluation](references/N6-qa-eval.md)
- N7: [Context management](references/N7-context.md)
- N8: [Finish](references/N8-finish.md)
