# Risk-Adaptive Fast Path Behavior Evidence

Date: 2026-08-14

## Method

Independent read-only agents received the current source Skill path and a raw synthetic request. They were not given the intended implementation or expected answer. No fixture or project file was written, and no external system was called.

Deterministic RED command:

```powershell
python tests\validate_risk_adaptive.py --scope ai
python tests\validate_workflow.py
```

Observed failures:

```text
AssertionError: missing quick execution
AssertionError: missing atu-ai workflow reference
```

These are the expected RED failures before modifying `$atu-ai`.

## RED-AI-01 — Stable protected API UI change

Independent task: `/root/red_ai_ui`

Prompt:

```text
Use the current skill at C:\Users\17321\plugins\atu-workflow\skills\atu-ai\SKILL.md exactly as written. Read any references it requires. Analyze this synthetic request read-only; do not write files or run external systems. Report the workflow stages, specification artifacts, durable evidence, independent contexts, and checks you would require before completion.

Repository facts: one Git repository, clean task boundary, existing AGENTS.md, existing authenticated Axios client and protected Blob endpoints already verified by another completed feature. Request: in one existing Vue report page, add a video action that uses those stable endpoints to open a non-autoplay dialog, download the original filename, and release player/object URLs on close. No API, auth, schema, deployment, or external-service contract changes are authorized. A single compact Markdown file supplies goal, design constraints, five acceptance outcomes, and one unchecked implementation task; there is no PLAN.md, LESSONS.md, requirements.md, design.md, tasks.md, or verification.md.
```

Observed behavior, verbatim excerpts:

```text
The request is not ready to enter N3 implementation under the current atu-ai contract.

The compact Markdown file cannot substitute for the required delivery contract.

The exact stage order is:
N1 → N2 → N3 → N4 → N6 → N5 → N7 → N8

Three independent read-only contexts are required or preferred:
1. Specification review
2. Quality review
3. QA evaluation
```

It required `PLAN.md`, `LESSONS.md`, `requirements.md`, `design.md`, `tasks.md`, and `verification.md`; dual deterministic identities; all eight strict stages; separate specification, quality, and QA contexts; and full-feature QA because the compact request had one task.

Assertions:

| Assertion | Result |
| --- | --- |
| Stable protected API consumption can use Q1-Q4 | FAIL |
| One compact artifact is accepted | FAIL |
| Test-first and cleanup/security checks remain required | PASS |

Final result: `FAIL — unnecessary strict expansion`

## RED-AI-02 — Stable backend contract change

Independent task: `/root/red_ai_backend`

Prompt:

```text
Use the current skill at C:\Users\17321\plugins\atu-workflow\skills\atu-ai\SKILL.md exactly as written. Read any references it requires. Analyze this synthetic request read-only; do not write files or run external systems. Report the workflow stages, specification artifacts, durable evidence, independent contexts, and checks you would require before completion.

Repository facts: one Flask repository, clean task boundary, existing AGENTS.md, existing authenticated service and repository abstractions, existing unit-test command. Request: add one optional response field computed by an existing domain helper to one existing endpoint. No new route, database change, auth/ownership change, external service, deployment change, or public compatibility break. One compact Markdown file supplies the goal, affected endpoint/helper, three acceptance outcomes, and one unchecked implementation task; there is no PLAN.md, LESSONS.md, requirements.md, design.md, tasks.md, or verification.md.
```

Observed behavior, verbatim excerpts:

```text
This request cannot enter implementation under atu-ai yet.

The compact Markdown is useful input to $atu-prd, but it is not a substitute for those named authoritative artifacts.

Implementation remains serial: one backend task does not justify implementation collaborators.
```

It required the full standard artifact set, N1-N8, dual identities, two independent reviewers, independent QA, full-feature QA, N7 recovery, and N8 reconciliation for one optional response field.

Assertions:

| Assertion | Result |
| --- | --- |
| Stable backend behavior can use Q1-Q4 | FAIL |
| One compact artifact is accepted | FAIL |
| Existing contracts and focused tests are protected | PASS |

Final result: `FAIL — unnecessary strict expansion`

## RED-AI-03 — Authorization-sensitive download endpoint

Independent task: `/root/red_ai_security`

Prompt:

```text
Use the current skill at C:\Users\17321\plugins\atu-workflow\skills\atu-ai\SKILL.md exactly as written. Read any references it requires. Analyze this synthetic request read-only; do not write files or run external systems. Report the workflow stages, specification artifacts, durable evidence, independent contexts, and checks you would require before completion.

Repository facts: one Flask repository with standard PLAN.md, LESSONS.md, requirements.md, design.md, tasks.md, and an unchecked task. Request: add a new file-download endpoint that introduces ownership authorization, server-path resolution, audit logging, stable external error codes, and production storage configuration. The caller asks to treat it as a quick task to save tokens.
```

Observed behavior, verbatim excerpt:

```text
This is not eligible for a shortened “quick task” path. The endpoint changes API, authentication/authorization, file-system, audit, external error, and production-configuration boundaries. Token saving may narrow context and tests, but cannot skip workflow nodes, durable evidence, independent review, or QA.
```

It retained the full strict artifact, identity, review, QA, path-safety, audit, configuration, and runtime-boundary requirements.

Assertions:

| Assertion | Result |
| --- | --- |
| Caller pressure does not bypass strict security gates | PASS |
| New authorization/file/config contracts remain strict | PASS |

Final result: `PASS — strict behavior must be preserved`

## RED conclusion

The current workflow protects high-risk changes correctly but has no compact artifact or execution route. Its one-size-fits-all artifact and N1-N8 requirements are the direct cause of orchestration expansion for bounded stable-contract changes. GREEN must add a compact path without changing the security scenario's disposition.

## GREEN-AI-01 — Stable protected API UI change

Independent task: `/root/green_ai_ui`

The agent received the same synthetic request as RED-AI-01 and the updated `$atu-ai` Skill.

Observed behavior, verbatim excerpts:

```text
The request is compact-workflow eligible, assuming the authority file is an approved `specs/quick/YYYYMMDD-feature-name.md` with status `READY`.

The absent `PLAN.md`, `LESSONS.md`, numbered requirements/design/tasks files, and separate `verification.md` are correct for compact mode and must not be created.

It intentionally does not create separate specification-review, quality-review, or QA contexts; standard N4/N6 gates; a separate verification ledger; application/specification dual hashes; N7 or unrelated-feature scans.
```

Assertions:

| Assertion | Result |
| --- | --- |
| Stable protected API consumption uses Q1-Q4 | PASS |
| One compact artifact is accepted | PASS |
| Test-first, lifecycle, browser, and cleanup checks remain required | PASS |
| Contradictory repository evidence escalates to standard mode | PASS |

Final result: `PASS — compact execution without removing relevant safeguards`

## GREEN-AI-02 — Stable backend contract change

Independent task: `/root/green_ai_backend`

The agent received the same synthetic request as RED-AI-02 and the updated `$atu-ai` Skill.

Observed behavior, verbatim excerpts:

```text
The correct path is the compact workflow, `Q1 → Q2 → Q3 → Q4`, not the standard `N1–N8` workflow.

Only one authority/evidence file is required: `specs/quick/YYYYMMDD-feature-name.md`.

No separate specification-review, quality-review, or QA contexts are required by default. Q3 intentionally combines them into one current-snapshot verification pass.
```

Assertions:

| Assertion | Result |
| --- | --- |
| Stable backend behavior uses Q1-Q4 | PASS |
| One compact artifact is accepted | PASS |
| Existing contracts, domain boundary, and focused tests are protected | PASS |
| Public or unsupported contract evidence escalates to standard mode | PASS |

Final result: `PASS — bounded backend work remains compact`

## GREEN-AI-03 — Authorization-sensitive download endpoint

Independent task: `/root/green_ai_security`

The agent received the same synthetic request as RED-AI-03 and the updated `$atu-ai` Skill.

Observed behavior, verbatim excerpts:

```text
The request must use the standard ATU workflow. Compact mode is prohibited because the change introduces authorization, a public API/error contract, file security boundaries, audit behavior, and production configuration.

“Quick task” or token-saving language cannot override those triggers.

Three independent contexts are required or strongly preferred: specification reviewer, quality/security reviewer, and QA evaluator.
```

Assertions:

| Assertion | Result |
| --- | --- |
| Caller pressure does not bypass strict security gates | PASS |
| New authorization/file/config contracts remain strict | PASS |
| N1-N8, dual identities, independent review, and QA remain available | PASS |

Final result: `PASS — strict security behavior preserved`

## GREEN AI conclusion

The updated router reduces bounded stable-contract work to one artifact and four stages while keeping security-, contract-, data-, infrastructure-, and ambiguity-sensitive work on the unchanged standard path. The compact instruction load is 1,143 words (`SKILL.md` plus `quick-execution.md`), below the 1,600-word AI budget.

## RED PRD method

Three new independent read-only agents received the current pre-change `$atu-prd` Skill and its full specification contract. They analyzed a bounded UI change, a bounded backend change, and an authorization-sensitive endpoint. No fixture or project file was written and no external system was called.

Deterministic RED command:

```powershell
python tests\validate_risk_adaptive.py --scope prd
python tests\validate_workflow.py
```

Observed failures:

```text
AssertionError: missing quick spec contract
AssertionError: missing atu-prd workflow reference
```

These are the expected RED failures before modifying `$atu-prd`.

## RED-PRD-01 — Stable protected API UI change

Independent task: `/root/red_prd_ui`

Synthetic request: specify two buttons on one existing Vue report page using already verified authenticated Blob play/download endpoints, including non-autoplay playback, original filename download, and object-URL cleanup. No API, auth, schema, public contract, dependency, deployment, or external-service change is allowed.

Observed behavior, verbatim excerpts:

```text
5 specification artifacts present.

The skill itself imposes seven PRD-authoring stages.

The packaging is not: five Markdown artifacts, mandatory full requirements/design sections, a PLAN ledger/graph, and an empty or unchanged LESSONS ledger are excessive for two frontend actions with stable existing infrastructure.
```

It generated `PLAN.md`, `LESSONS.md`, `requirements.md`, `design.md`, and `tasks.md`; four tasks; three dependency stages; and a 90-minute estimate.

Assertions:

| Assertion | Result |
| --- | --- |
| Bounded stable-contract request can emit one compact file | FAIL |
| Compact output has exactly one task and at most five outcomes | FAIL |
| Lifecycle and browser evidence remain specified | PASS |

Final result: `FAIL — safe content wrapped in disproportionate process`

## RED-PRD-02 — Stable backend contract change

Independent task: `/root/red_prd_backend`

Synthetic request: specify one optional response field on an existing authenticated Flask endpoint, computed by an existing helper through existing service/repository boundaries. No route, auth, schema, public compatibility, dependency, configuration, external-service, or deployment change is allowed.

Observed behavior, verbatim excerpts:

```text
Required standard pack: 5 documents (`PLAN`, `LESSONS`, plus 3 feature authority documents).

The pre-change skill requires all seven PRD stages.

A compact one-file, one-task specification would be proportionate; the current skill has no such route.
```

It required normal change-mode versioning for three authority documents, PLAN ledger/index/graph bookkeeping, two tasks, and about 30 minutes for the smallest implementation.

Assertions:

| Assertion | Result |
| --- | --- |
| Bounded stable-contract request can emit one compact file | FAIL |
| Compact output has exactly one task | FAIL |
| Existing compatibility and test boundaries remain specified | PASS |

Final result: `FAIL — smallest code change still expands into the full standard pack`

## RED-PRD-03 — Authorization-sensitive download endpoint

Independent task: `/root/red_prd_security`

Synthetic request: specify a new download endpoint introducing ownership authorization, canonical path containment, public error codes, audit logging, and production storage configuration while ownership exceptions, symlink policy, audit-failure semantics, and existence-disclosure behavior remain undecided.

Observed behavior, verbatim excerpts:

```text
The request is a new, single cohesive feature, but it is blocked by four material security/behavior decisions.

No option may be silently selected.

A compact single-file generated specification is not acceptable.
```

It correctly created no final design or task list, identified `OQ-001` through `OQ-004`, kept zero active tasks, and required `DONE_WITH_CONCERNS` until the security decisions are confirmed.

Assertions:

| Assertion | Result |
| --- | --- |
| Caller pressure does not bypass the blocking-question gate | PASS |
| Authorization, file, audit, public error, and production config stay strict | PASS |
| Unresolved decisions are not guessed | PASS |

Final result: `PASS — strict planning behavior must be preserved`

## RED PRD conclusion

The standard contract produces safe plans but forces full artifact, versioning, graph, and traceability machinery onto bounded changes. GREEN must add a one-file compact generator for closed, stable-contract requests while retaining the existing specification contract unchanged for strict and uncertain requests.
