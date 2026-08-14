# Editor grant viewer

- Status: DONE
- Mode: forced-quick
- Override: explicit $atu-quick invocation
- Date: 2026-08-14
- Source: request, named files, and repository evidence

## Goal
Allow an editor to grant viewer access through the existing `grant_access(actor_role, target_role)` contract while preserving all other authorization behavior.

## Scope
Change only the local authorization matrix and focused regression tests. Preserve the pre-existing untracked `__pycache__/` directory.

## Risk override and action authorization
This is an authorization and public-contract change explicitly routed through forced quick. Local file edits and tests are authorized. Commit, push, deploy, migration, production writes, deletion, external calls, authentication, persistence, audit, dependencies, and schema changes are not authorized.

## Reused contracts and evidence
`grant_access` returns `{"status": 200, "granted_role": target_role}` for allowed grants and `{"status": 403, "error": "forbidden"}` otherwise. Existing tests cover admin-to-editor success and editor-to-editor denial. Baseline `python -m unittest -v` passed 2 tests.

## Bounded design
Add `viewer` to the editor entry in `GRANT_MATRIX`. Add focused tests for editor-to-viewer success and an unknown-role denial; retain existing tests and return envelopes unchanged.

## Acceptance criteria
- AC-Q01: Editor-to-viewer returns exactly `{"status": 200, "granted_role": "viewer"}`.
- AC-Q02: Editor-to-editor and editor-to-unknown return exactly `{"status": 403, "error": "forbidden"}`.
- AC-Q03: Existing admin behavior and all retained tests remain passing.
- AC-Q04: The repository-required `python -m unittest -v` passes without changes outside the authorized local scope.

## Task
- [x] T-Q01: Implement test-first, run focused and repository regression checks, review the complete diff, and verify AC-Q01 through AC-Q04.

## Execution evidence
Environment: isolated local Windows fixture with Python `unittest`; no external systems used.

Changed paths and scope:
- `app.py`: added only `viewer` to the editor grant set.
- `test_app.py`: added editor-to-viewer success and editor-to-unknown denial regressions.
- `specs/quick/20260814-editor-grant-viewer.md`: recorded the forced-quick contract and evidence.

Commands and results:
- Baseline `python -m unittest -v`: exit 0; 2 tests passed.
- Red check `python -m unittest -v test_app.GrantAccessTests.test_editor_can_grant_viewer test_app.GrantAccessTests.test_editor_cannot_grant_unknown_role`: exit 1; editor-to-viewer failed with actual 403 versus expected 200, while unknown denial passed.
- Focused authorization check `python -m unittest -v test_app.GrantAccessTests.test_editor_can_grant_viewer test_app.GrantAccessTests.test_editor_cannot_grant_editor test_app.GrantAccessTests.test_editor_cannot_grant_unknown_role`: exit 0; 3 tests passed.
- Repository check `python -m unittest -v`: exit 0; 4 tests passed.
- `git diff --check`: exit 0; no patch errors.

Acceptance evidence:

| Criterion | Result | Evidence |
|---|---|---|
| AC-Q01 | PASS | Focused and full tests assert the exact editor-to-viewer 200 envelope. |
| AC-Q02 | PASS | Focused and full tests assert exact 403 envelopes for editor and unknown targets. |
| AC-Q03 | PASS | Retained admin test passed in the 4-test repository run; admin matrix entry is unchanged. |
| AC-Q04 | PASS | Required repository command exited 0; diff review found only authorized code, test, and quick-spec paths. |

Combined review found no authentication, persistence, schema, migration, audit, dependency, deployment, data, external-service, concurrency, compatibility, or unrelated behavior changes. The pre-existing untracked `__pycache__/` remained outside the task scope.

## Open questions
None.

## Handoff
Local implementation and verification are complete. No manual or real-boundary evidence is required for this pure function change. Commit, push, deploy, migration, production writes, deletion, and external actions were not performed and remain unauthorized.
