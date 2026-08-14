# N3: Execute one task

Work on exactly one active task at a time. An active task is the single task whose implementation is currently allowed to change files; do not start another task until this task completes N4–N7 or is explicitly blocked.

## Start the task

1. Re-read the task description, mapped requirements, design section, acceptance criteria, relevant `LESSONS.md` entries, and effective `AGENTS.md`.
2. Compute the task's deterministic `spec_contract` from the normalized task description, mapped requirements, relevant design contract, and mapped acceptance criteria. Record its hash value, spec hash algorithm, normalization rules, spec hash scope, and exact files/sections/IDs. If it cannot be generated, record `spec_contract=unverifiable`; invalidate older implementation, review, and QA evidence and remain in N3.
3. Inspect the task's target files and current diff. Confirm that the planned edits do not overwrite or absorb unrelated user changes.
4. Announce the task ID, feature, scope, expected files, dependencies, and validation plan.
5. When the first implementation or test edit actually begins, update the feature's PLAN status to `🚧 开发中` if needed and record `in_progress` for the current deterministic application-code snapshot and `spec_contract` in `verification.md` when ledger writing is allowed. Record both hash values, algorithms, and scopes.

## Route domain work

Load the smallest applicable domain skill before editing:

- Browser frontend: `$atu-frontend-engineer`
- Backend/API/service: `$atu-backend-engineer`
- Database, migration, query, or Redis: `$atu-database-engineer`
- Native Android or WebView shell: `$atu-android-engineer`
- Native WeChat Mini Program: `$atu-miniprogram-engineer`
- Test-only work: `$atu-qa-engineer`

Load multiple domain skills only when the one task genuinely crosses those boundaries. Keep code review and documentation synchronization in their designated later nodes.

## Implement test-first

1. Add or tighten the narrowest meaningful automated test for the required behavior and observe it fail for the expected reason. If no safe automated test is feasible, record why and define concrete manual evidence before implementation.
2. Make the smallest implementation change that satisfies the task contract and existing architecture.
3. Run the focused test until it passes, then run the relevant nearby regression checks.
4. Keep credentials, production data, destructive operations, dependency additions, generated files, and external writes within explicit authorization.
5. Inspect the resulting diff and remove only task-introduced noise. Never clean unrelated changes.
6. Before entering N4, recompute `spec_contract` and generate a deterministic commit hash, diff patch hash, or tree/content hash for the exact application/test scope. Record both hash values, hash algorithms, and hash scopes, plus the spec normalization rules. Record `implementation_complete` only when every required implementation and test artifact is present and both identities match the current content; include supporting changed-file/diff evidence, completion timestamp, focused-test result, blockers, and N4 as the next route.
7. If either identity cannot be generated, record `snapshot=unverifiable` or `spec_contract=unverifiable` as applicable. Treat every older implementation, review, and QA result as invalid, keep the task unchecked, record `in_progress` or the blocker, and remain in or route to N3. Never substitute a changed-file list plus timestamp as snapshot identity.

## Collaboration boundary

Implementation collaborators must own mutually exclusive source and mutable artifact write sets, must not share mutable state or ordering dependencies, and must never jointly own or write the same file. Give each implementation collaborator an explicit repository, specification, task slice, exclusive file/write boundary, and authority. Read-only review and QA workers are not implementation collaborators: multiple such workers may inspect the same frozen diff and specifications because they do not write files or share mutable state; pin them to the same exact snapshot and prohibit edits. Collaboration never expands the user's scope or authorizes pushes, deploys, migrations, external messages, destructive actions, or edits outside the assigned slice.

If the write-isolation conditions are not all true, execute writes serially. Regardless of collaboration, keep only one workflow task active and reconcile every returned diff and verification result before N4.

Report files changed, focused and regression evidence, manual checks, dependencies, deviations, residual risks, and blockers. Do not push or deploy.
