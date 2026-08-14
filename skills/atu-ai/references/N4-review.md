# N4: Review one task

Review the just-completed task only. Keep the review target explicit: the task ID, its specification mappings, and the exact changed files or diff attributable to it.

## Entry gate

Confirm the task is unchecked and its ledger contains `implementation_complete` evidence matching both the exact current deterministic application-code snapshot and deterministic `spec_contract`. Verify both hash values, algorithms, and scopes, plus spec normalization rules; the spec scope must include the task description, mapped requirements, relevant design contract, and mapped acceptance criteria. If either identity or implementation evidence is missing, incomplete, mismatched, `snapshot=unverifiable`, or `spec_contract=unverifiable`, invalidate all older implementation, review, and QA evidence; do not manufacture it in N4, and return to N3. N4 verifies implementation but does not establish that implementation work was completed.

## Required sequence

Execute these gates in order:

1. **Tests.** Run the task's focused tests and the relevant regression tests. Record exact commands, environment, pass/fail/skip counts, and useful failure output.
2. **Static checks.** Run the repository-supported lint, formatting check, type check, compile check, build check, security scan, or equivalent checks relevant to the changed files. Do not introduce or substitute a tool merely to manufacture a green result.
3. **Self-review.** Compare the diff against requirements, design, acceptance criteria, effective `AGENTS.md`, `LESSONS.md`, existing architecture, user-change boundaries, correctness, security, error paths, compatibility, and test adequacy.
4. **Independent specification review.** In a separate read-only review context, verify that the implementation satisfies every mapped requirement and acceptance criterion without adding unapproved behavior. Supply the exact specification and task diff; do not ask the reviewer to edit files.
5. **Specification hard gate.** Do not start quality review while the specification review has any unresolved blocking finding. Route implementation or test fixes through N3. After every resulting edit, re-run tests, static checks, self-review, and specification review on the new snapshot.
6. **Independent quality review.** Only after the specification hard gate passes, use `$atu-code-reviewer` in a separate read-only review context to inspect correctness, security, regressions, maintainability, and validation gaps for the exact task diff.

Do not begin an independent review until the preceding test, static-check, and self-review gates have no known blocking issue. Multiple read-only reviewers may inspect the same pinned diff/specification snapshot; no reviewer may edit it.

## Failure and re-review rules

- Fix every evidence-backed quality finding within the authorized task scope through N3, then repeat all of N4 from tests through specification review before running quality review again.
- Evaluate warnings against the task contract and risk. Fix material warnings; if a warning is intentionally retained, record concrete evidence and residual impact.
- For an incorrect finding, record the specific code/spec evidence before rejecting it.
- If a fix would change product scope, require a destructive action, cross an authorization boundary, or contradict the specifications, stop and obtain direction rather than expanding the task.
- An unresolved business, security, authorization, destructive-data, external-contract, or scope decision sets the affected feature's PLAN status to `⏸ BLOCKED`.
- A missing runtime, dependency, credential, service, browser, device, external system, supported command, or pending manual verification is `NOT RUN` or `MANUAL REQUIRED` as applicable. It is never a pass: keep the feature `🚧 开发中` and the task unchecked, and do not let successful narrower checks replace the missing gate.
- Pre-existing failures must be reproduced or otherwise evidenced, clearly separated from task-introduced failures, and left unresolved unless the user authorizes that additional scope.

N4 passes only when all required checks for this task have current acceptable evidence, specification review passed before quality review, both independent reviews have no unresolved blocking finding, and every unavailable check is truthfully recorded with its impact. Synchronize the task entry in `verification.md` with its dual-identity-matching `implementation_complete` evidence; application snapshot type/value, hash algorithm and hash scope; `spec_contract` value, spec hash algorithm, spec hash scope and normalization; N1 baseline dirty paths; test/static exit codes; self/specification/quality review results; blockers; and next route. Do not write secrets or raw sensitive logs. If either identity becomes missing, mismatched, `snapshot=unverifiable`, or `spec_contract=unverifiable`, all N4 evidence is invalid and the task returns to N3. If ledger writing is prohibited, say so; the evidence remains non-durable and N7 must recover according to the task checkbox and dual-identity rules.

Report the exact review target, commands and results, findings and dispositions, unavailable evidence, residual risks, and route. N4 PASS enters N6. An implementation/test defect returns to N3; a review/evidence gap remains in N4. Do not push or deploy.
