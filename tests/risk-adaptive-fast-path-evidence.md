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
