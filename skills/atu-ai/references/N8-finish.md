# N8: Finish

Finish only after every authorized feature has passed task, review, and QA gates. Enter N8 only when no active task remains and the last required full-feature N6 QA passed on the current snapshot. This terminal node synchronizes truthful documentation and reports the delivery boundary; it does not grant release authority or route to another workflow node.

## Final reconciliation

1. Re-read effective `AGENTS.md`, `PLAN.md`, every feature's `requirements.md`, `design.md`, `tasks.md`, available `verification.md`, relevant `LESSONS.md`, repository status, and the final relevant diffs.
2. For each feature, recompute the deterministic application snapshot and deterministic `spec_contract`. Verify every task is `[x]` or `[DROPPED]`, every required N4 gate passed under both exact current identities, N6 contains criterion-by-criterion task QA evidence under those identities, and the last required full-feature N6 QA plus regressions passed under them.
3. When a ledger is available, verify each entry contains the task ID; dual-identity-matching `implementation_complete` evidence; application snapshot type/value, hash algorithm and hash scope; `spec_contract` value, spec hash algorithm, spec hash scope and normalization; N1 baseline dirty paths; test/static exit codes; specification and quality review outcomes; acceptance-criterion matrix; blockers; and next route. The spec scope must include task description, mapped requirements, relevant design contract, and mapped acceptance criteria. A changed-file list or timestamp is never matching identity. The ledger is execution evidence, never requirements authority.
4. If either task identity or required ledger evidence is missing, incomplete, stale, mismatched, prohibited, `snapshot=unverifiable`, or `spec_contract=unverifiable`, do not trust its checkbox or use a direct N4/N6 fallback. Invalidate all prior implementation, review, and QA evidence and return `BLOCKED` without transitioning to another node in this N8 run. Report `NEXT STEP: 下次 $atu-ai 从 N7 原子 reopen，再 N3 → N4 → N6 → N5`. If authority to reopen `tasks.md` and `PLAN.md` is absent, or the required ledger update is unauthorized, remain `BLOCKED` and identify the required owner/authorization before that future recovery chain. When both identities and all ledger evidence match current content, pass the N8 identity check directly; do not reopen the task.
5. Set a feature to `✅ 完成` only when every completion condition holds. Set unresolved business, security, authorization, destructive-data, external-contract, or scope decisions to `⏸ BLOCKED`. Keep execution blockers such as unavailable environments, tools, services, browsers/devices, or pending manual verification at `🚧 开发中` with the affected task unchecked.
6. Re-read `PLAN.md` after any status correction. Synchronize final ledger evidence using concise sanitized results only; never write secrets or raw sensitive logs. Do not manufacture task, review, test, device, external-service, release, or deployment evidence to make the plan appear complete.

## Synchronize affected documentation

Load and follow `$atu-doc-syncer`. Perform semantic synchronization only for documentation affected by verified implementation:

- README and operator guidance;
- applicable `AGENTS.md` and project rules;
- API, schema, environment, deployment, and architecture documentation;
- current requirements, design, task annotations, changelog, and other affected specs.

Use current code, configuration, migrations, executed checks, and accepted decisions as the source of truth. Preserve unrelated user-authored content. Do not broadly rewrite documents, convert plans into completion claims, or update an unaffected surface merely for consistency of style.

Verify changed commands, paths, links, fields, environment names, API behavior, schema facts, and changelog claims against the repository. Record any assertion that cannot be verified as a boundary rather than presenting it as synchronized.

## Authorization boundary

Workflow completion does not authorize a commit, push, publication, deployment, migration, external message, or production change. Commit only when explicitly requested by the user or expressly required by effective project instructions, and stage only the exact verified implementation and documentation scope. Never push or deploy without explicit authorization for that action and target.

## Final report

Return all three sections even when work is blocked:

```text
COMPLETED
- <features, tasks, review and QA evidence, documentation synchronized>

BLOCKED
- <none, or exact unfinished criterion/check/environment/decision>

NEXT STEP
- <none, or the smallest concrete action and required owner/authorization>
```

Also state relevant files changed, checks run and outcomes, residual end-to-end/device/external-service boundaries, and whether commit, push, and deploy were performed or deliberately not performed. Use `DONE` only when `BLOCKED` is empty; otherwise return `BLOCKED`.

N8 is terminal: do not emit the normal `entering [next node]` transition. `NEXT STEP` may identify an external action, owner, or authorization needed after the workflow, but it is not a next workflow node.
