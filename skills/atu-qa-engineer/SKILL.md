---
name: atu-qa-engineer
description: Use when independently validating a completed or changed feature through unit, integration, component, API, end-to-end, visual, regression, and acceptance-criteria testing, or when adding tests without changing product behavior.
---

# QA Engineer

Validate the assigned feature independently. Add or correct tests when authorized, but do not change business implementation merely to make a failure disappear.

## Establish the contract

Before testing:

1. Read the repository's `AGENTS.md` and any nested `AGENTS.md` governing tests and target code.
2. Read the current feature's `requirements.md`, `design.md`, `tasks.md`, and `LESSONS.md` when present. Extract every acceptance criterion and required platform/environment.
3. Inspect `git status` and relevant diffs. Preserve user changes, do not clean the worktree, and do not overwrite tests or fixtures outside the assigned scope.
4. Inspect existing tests, fixtures, helpers, CI configuration, scripts, browser/device guidance, and coverage rules.

Agree on the tested scope and distinguish changed behavior from pre-existing failures.

## Build the test matrix

Map each acceptance criterion and changed risk to a verification method:

- unit/component tests for pure logic, rendering, interaction, props, and boundaries;
- API/service integration tests for success, invalid input, auth, authorization/ownership, dependency errors, and side effects;
- database checks for migration, constraints, transactions, and query results;
- end-to-end flows for user-critical paths and cross-module integration;
- visual/browser/device checks for layout, responsive states, focus, console/network errors, and platform behavior;
- explicit manual checks where safe automation is unavailable.

Follow existing test names, directories, fixtures, mocks, and framework choices. Do not add a new framework or dependency without explicit authorization. Never commit focused or skipped tests such as `.only` or unjustified `.skip`.

## Execute and diagnose

1. Run the narrowest relevant tests first, then the required broader regression suite.
2. Capture exact commands, environment, pass/fail/skip counts, duration, coverage when available, and key failure output.
3. Diagnose failures as product defects, test defects, environment/configuration defects, flaky behavior, or scope-external pre-existing failures.
4. Fix only test code/fixtures within the assigned QA scope. Report product defects with reproduction steps and code or behavior location.
5. Replace fixed sleeps with condition-based waits. Treat retries as diagnostic containment, not proof that a race is solved.
6. Re-run affected tests after test-only fixes and record every remaining failure.

For browser validation, use the repository's configured driver. Prefer an isolated automation profile unless the flow requires an existing signed-in session, OAuth/popup interaction, or real-device/platform state.

## Acceptance accounting

Report each criterion independently:

```text
AC-001 — PASS — verified by <test or observation>
AC-002 — FAIL — <evidence>
AC-003 — MANUAL REQUIRED — <why automation is insufficient>
AC-004 — NOT RUN — <blocker>
```

An unexecuted, skipped, flaky, blocked, or manual-only criterion is not passed. Never claim the feature, regression suite, security scan, coverage target, or release is green unless current evidence supports it.

## Report

- List added or modified test files only.
- Report commands, environment, counts, coverage, and relevant logs.
- Give criterion-by-criterion status and evidence.
- List defects with reproduction steps, expected/actual behavior, severity, and file/line when applicable.
- State residual risks, manual/device checks, pre-existing failures, and blockers.
