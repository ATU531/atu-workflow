# Acceptance evidence and independent QA

Use this reference for an assigned test-only task or when the selected ATU workflow needs independent QA. It does not add a new gate to ordinary combined verification or change the workflow's test-first, status, or specification contracts.

In standard mode, use independent QA when acceptance depends on a real browser, device, payment provider, external service, or human operation, or when the user requests it. Run it once for the feature rather than for every task. Compact and forced-quick work retain their own combined verification, escalation, and user-directed review rules; this reference does not select another mode or add a default independent pass. Independent code review follows the selected workflow's risk triggers; a reviewer finding no defect is not a QA pass, and passing tests are not an independent code review.

## Evidence contract

For each acceptance criterion, record the current result, target snapshot/environment, and sufficient command/output or observation evidence:

| Result | Meaning |
|---|---|
| PASS | The required check ran successfully against the stated target. |
| FAIL | Current execution or observation demonstrates a defect. |
| BLOCKED | A required decision, permission, environment, or dependency prevents verification/completion. |
| NOT RUN | The check has not been executed. |
| MANUAL REQUIRED | Required human/device evidence remains outstanding. |

Skipped, flaky, blocked, mocked, or manual-only evidence does not establish a real-boundary PASS. Report useful counts, failure excerpts, and coverage only when measured. Distinguish product defects, test defects, environment failures, and pre-existing out-of-scope failures. Retries do not prove a race is fixed.

Use existing test tools and fixtures; add dependencies only when required within the authorized task scope. An independent QA assignment may change assigned tests/fixtures, not business code to hide a failure. Preserve unrelated changes, and remove test-runner focus markers such as `.only` or unjustified skips that silently exclude required coverage. Give reproducible product findings with expected/actual behavior and location.

After a confirmed implementation/test defect, reopen only the affected task through the selected workflow and rerun affected checks and necessary final regressions. Keep unrelated completed tasks intact. An evidence-only gap remains in verification; missing required real-service, browser, device, or human evidence cannot be replaced with a narrower test or an unsupported completion claim.
