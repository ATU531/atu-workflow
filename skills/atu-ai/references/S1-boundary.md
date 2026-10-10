# S1: Confirm boundary

Establish the smallest safe execution boundary before editing.

1. Resolve the authorized specs directory and code repositories from the request. Read applicable `AGENTS.md` and any repository guidance that governs likely edits.
2. Read `PLAN.md`, relevant `LESSONS.md`, and the selected feature's `requirements.md`, `design.md`, and `tasks.md`. A legacy single-feature directory is acceptable when its authority is unambiguous.
   Read referenced architecture revisions and applicable decisions. Verify approval evidence and scope; stop only affected work if the reference is missing, unapproved, conflicting, or superseded for this scope, and route specification reconciliation to `$atu-prd`. A newer draft or unrelated revision does not supersede it. Legacy work needs no retroactive architecture document unless current work depends on unresolved architectural decisions. Do not edit an approved baseline to match implementation.
3. Inspect each repository's branch, status, relevant diff, and untracked files. Separate pre-existing work from the intended change; never reset, clean, stash, overwrite, reformat, or absorb unrelated changes.
4. Reconcile dependencies and task states. Skip `[x]` and `[DROPPED]`, treat `[CHANGED]` by its current text, and select the earliest ready `[ ]` task in dependency order.
5. Stop as `BLOCKED` for a material unresolved product, security, authorization, destructive-data, external-contract, or scope decision. Report the exact owner or answer needed.
6. For a missing runtime, credential, service, browser, device, or manual acceptance boundary needed by the current task, report `NOT RUN` or `MANUAL REQUIRED`. Do not label unavailable evidence as a decision failure or a pass.

Keep PLAN unchanged while only reading. Set the selected feature to `🚧 开发中` only when its first test or implementation edit begins. Announce the selected feature/task, intended files, reused contracts, focused checks, and known boundaries, then enter S2.
