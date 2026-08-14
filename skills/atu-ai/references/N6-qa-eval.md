# N6: Evaluate QA

Evaluate QA after N4 and before N5 against the exact N4-passed deterministic application snapshot, deterministic `spec_contract`, and matching `implementation_complete` evidence. Confirm both hash values, algorithms, and scopes, including spec normalization and coverage of task description, mapped requirements, relevant design contract, and mapped acceptance criteria. N6 always maps and verifies the acceptance criteria assigned to the current task. N6 cannot create missing implementation evidence. If either identity is missing, mismatched, `snapshot=unverifiable`, or `spec_contract=unverifiable`, invalidate all older implementation, review, and QA evidence and route to N3. A score may decide when extra QA is useful; it can never turn missing or failed evidence into a pass.

If N7 recovery-reopened an already checked task, verify the current recovery snapshot rather than the old checkbox or ledger snapshot. Commit is prohibited during this N6 run.

## Decide the QA scope

Always run task-level QA for the current task's mapped acceptance criteria and relevant regressions.

When the current task is the feature's last active task (all other tasks are `[x]` or `[DROPPED]`), the same N6 run must also execute a full-feature acceptance-criterion matrix and all required feature regressions. Only this current full-feature PASS may qualify the feature for completion after N5.

Run additional feature-level QA earlier when:

- an API, schema, migration, authentication, authorization, payment, privacy, or external callback contract changed;
- the change crosses modules or repositories;
- five tasks have completed since the last feature-level QA; or
- specifications or project instructions require a particular QA gate.

For other changes, score change breadth, risk, accumulated work since QA, and user-visible boundary from 1 to 5 each. A total of 8 or more triggers additional QA. Pure documentation, comment, formatting, or unimplemented type-only changes may skip extra execution only when no acceptance criterion or required gate depends on them.

Record the inputs and reason. A known blocker, failed N4 gate, missing required environment, or unresolved acceptance criterion takes precedence over scoring and must be reported; scoring cannot bypass it.

## Validate criterion by criterion

Use `$atu-qa-engineer` in a separate independent QA context when practical; otherwise apply that skill's contract directly. Supply the specs path, repository path, exact feature/task scope, changed snapshot, and known boundaries.

1. Re-read effective `AGENTS.md`, `PLAN.md`, current `requirements.md`, `design.md`, `tasks.md`, `LESSONS.md`, repository status, the task's N4 evidence, and the exact N4-passed task diff.
2. Extract every acceptance criterion mapped to the current task and build a matrix with one row per criterion. If this is the last active task, also build the complete feature matrix rather than assuming earlier task checks still prove it.
3. Map each row to the strongest relevant evidence: unit/component, API or service integration, database, regression, end-to-end, visual/browser, real-device, or external-service verification.
4. Run the narrowest checks first and then required broader regressions. Record exact commands, environment, pass/fail/skip counts, duration when available, and useful failure output.
5. For every criterion, report one status and its evidence:

```text
AC-001 — PASS — <current test or observation>
AC-002 — FAIL — <reproduction and evidence>
AC-003 — MANUAL REQUIRED — <missing human, browser, or device evidence>
AC-004 — NOT RUN — <environment or dependency blocker>
AC-005 — BLOCKED — <external contract or service blocker>
```

Explicitly account for required end-to-end flows, browser or visual checks, real-device or mini-program checks, credentials, payment providers, callbacks, and other external services. An unavailable, skipped, flaky, manual-only, simulated, or mocked boundary is not a pass for the real boundary.

## Route the result

- **PASS:** Every task-mapped acceptance criterion and required regression has current passing evidence, with no unresolved blocker. For the last active task, the full-feature matrix and regressions must also PASS. Enter N5; for a recovery-reopened task, N5 re-checks it. Do not check or commit before N5.
- **FAIL requiring implementation or test changes:** Keep the affected task unchecked, keep commit prohibited, and return to N3. After fixes, repeat N4 and N6 on the updated snapshot before N5.
- **Review or evidence gap without an implementation change:** Keep the task unchecked and commit prohibited, return to N4, then repeat N6 only after N4 passes on the current snapshot.
- **Unresolved business, security, authorization, destructive-data, external-contract, or scope decision:** Set the affected feature's PLAN status to `⏸ BLOCKED`, keep the task unchecked, report the exact decision owner/input needed, and stop if no independent ready work remains.
- **Environment or manual execution blocker:** For a required criterion that is `NOT RUN` or `MANUAL REQUIRED` because a runtime, dependency, credential, service, browser/device, external system, or human check is unavailable, keep PLAN at `🚧 开发中` and the task unchecked. Report the exact evidence needed and stop if no independent ready work remains.

Limit repair loops to evidence-backed, authorized changes. Never weaken an acceptance criterion, replace a required end-to-end or real-device check with a narrower test, or raise a score to conceal a blocker.

Synchronize `verification.md` with the task ID; dual-identity-matching `implementation_complete` evidence; application snapshot type/value, algorithm and scope; `spec_contract` value, spec hash algorithm, spec hash scope and normalization; N1 baseline dirty paths; test/static exit evidence inherited from N4; specification/quality review results; task acceptance-criterion matrix; any full-feature matrix and regressions; blockers; and next route. Store concise sanitized evidence only; never secrets or raw sensitive logs. Never use a file list or timestamp as matching identity. If ledger writing is prohibited, report that fact and require N7 to recover according to the task checkbox and dual-identity rules.

Report the trigger decision and score, task criterion matrix, full-feature matrix when required, commands and outcomes, end-to-end/device/external-service boundaries, defects, PLAN reconciliation, residual risks, and N5 or the return node.
