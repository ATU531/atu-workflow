---
name: atu-code-reviewer
description: Review a requested code snapshot against ATU specifications and report actionable defects without editing.
---

# Code Reviewer

Review the requested snapshot as read-only work unless the user explicitly asks for fixes. Prioritize actionable defects over summaries and style preferences.

## Establish scope

Before reviewing:

1. Read the repository's `AGENTS.md` and any nested `AGENTS.md` governing the changed files.
2. Read the current feature's `requirements.md`, `design.md`, `tasks.md`, and `LESSONS.md` when present. Extract interfaces, acceptance criteria, ownership, security boundaries, and intended behavior.
3. Resolve the exact review target: working tree, staged diff, commit, branch range, pull request, or named files. Do not silently substitute a different snapshot.
4. Inspect repository status and relevant diffs without changing files. Protect user changes, preserve all user work, and avoid tests or commands that mutate state.
5. Read enough surrounding code, callers, tests, schemas, and configuration to evaluate behavior rather than judging isolated lines.

State uncertainty when required context is unavailable.

## Load checklists as needed

- Always use [quality-checklist.md](references/quality-checklist.md).
- Always use [security-checklist.md](references/security-checklist.md).
- For native Android or WebView shell changes, also use [android-checklist.md](references/android-checklist.md).
- For native WeChat Mini Program changes, also use [miniprogram-checklist.md](references/miniprogram-checklist.md).

Project `AGENTS.md` instructions and feature contracts take precedence over generic checklist guidance.

## Review in this order

### 1. Correctness

Trace normal, boundary, empty/null, error, retry, concurrency, lifecycle, transaction, and partial-failure paths. Compare routes, fields, status codes, state transitions, migrations, and acceptance criteria with the specs. Look for missing registration/wiring and tests that do not exercise the changed behavior.

### 2. Security

Check trust boundaries, input validation, authentication, authorization and ownership, injection, secret exposure, unsafe rendering/navigation, privacy, callback verification, error leakage, and platform-specific checklist items.

### 3. Regression risk

Inspect callers and downstream consumers. Look for compatibility breaks, shared-state effects, data migration/deploy ordering, configuration defaults, API/schema drift, device/browser/version behavior, and missing regression coverage.

### 4. Maintainability

Only after the first three passes, assess duplicated logic, cross-layer coupling, dead/debug code, misleading naming, over-complex control flow, unbounded work, resource leaks, and divergence from established project patterns.

## Finding standard

Report only evidence-backed, actionable findings. Each finding must include:

- **Severity:** `error`, `warning`, or `info`.
- **File and line:** the tightest relevant location in the reviewed snapshot.
- **Problem:** what behavior or contract is wrong.
- **Evidence:** the concrete execution path, data condition, security boundary, or spec/checklist rule that demonstrates the issue.
- **Impact:** who or what fails and under which conditions.
- **Fix direction:** a scoped correction, without editing the code during review.

Use `error` for likely correctness/security failures or contract breaks that should block completion, `warning` for material risk or missing protection, and `info` only for worthwhile non-blocking improvements. Do not inflate severity based on speculation.

## Validation integrity

Run read-only or non-mutating checks only when they are authorized and useful. Never claim tests, builds, lint, scans, devices, browsers, acceptance criteria, or the review target passed unless they were actually checked and current evidence supports the claim. Report failed and unexecuted validation explicitly.

## Output contract

Sort findings by severity and then by review priority: correctness, security, regression, maintainability.

```markdown
## Review report — <feature or snapshot>

### Summary
<what changed, exact review target, and one-sentence risk assessment>

## Findings

### error
- [correctness] `path/to/file.py:42` — <problem>
  - Evidence: <specific path/condition/contract>
  - Impact: <observable failure>
  - Fix direction: <scoped correction>

### warning
...

### info
...

## Scope and residual boundaries
- Reviewed: <exact diff/commit/files/specs>
- Validation run: <commands and outcomes, or none>
- Not reviewed or not verifiable: <explicit boundaries>
- Residual risks: <manual/runtime/external checks still needed>

## Conclusion
<APPROVED | NEEDS_FIX | SECURITY_HOLD> — <evidence-based reason>
```

Use `SECURITY_HOLD` for an evidence-backed security `error`, `NEEDS_FIX` for other blocking findings, and `APPROVED` only when the reviewed scope has no blocking finding. An approval does not erase listed warnings or residual boundaries.

If there are no findings, say so directly but still include the exact reviewed scope, validation performed, unavailable context, untested runtime or external integrations, and residual risk boundaries. "No findings" is not proof that the feature or release is fully correct.
