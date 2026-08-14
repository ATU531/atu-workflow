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

The updated router reduces bounded stable-contract work to one artifact and four stages while keeping security-, contract-, data-, infrastructure-, and ambiguity-sensitive work on the unchanged standard path. After final strict-trigger and status-routing review fixes, the compact instruction load is 1,307 words (`SKILL.md` plus `quick-execution.md`), below the 1,600-word AI budget.

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

## GREEN-PRD-01 — Stable protected API UI change

Independent task: `/root/green_prd_ui`

The agent received the same bounded UI scenario as RED-PRD-01 and the updated `$atu-prd` Skill.

Observed behavior, verbatim excerpts:

```text
Compact mode is the correct selection.

Documents: 1 authority/evidence document
Acceptance criteria: 4, contiguous `AC-Q01`–`AC-Q04`
Top-level tasks: exactly 1, `T-Q01`
Standard artifacts changed: none

This is proportionate.
```

It produced a complete proposed `specs/quick/20260814-report-video-preview-download.md` covering stable authenticated clients/endpoints, non-autoplay behavior, server filename use, failure paths, late responses, object-URL cleanup, focused component/browser verification, and localized rollback.

Assertions:

| Assertion | Result |
| --- | --- |
| Bounded stable-contract request emits one compact file | PASS |
| Output has one task and no more than five outcomes | PASS |
| No PLAN/LESSONS/numbered/ledger artifact is introduced | PASS |
| Lifecycle, browser, error, and security invariants remain explicit | PASS |

Final result: `PASS — one proportional artifact with complete bounded design`

## GREEN-PRD-02 — Stable backend contract change

Independent task: `/root/green_prd_backend`

The agent received the same bounded backend scenario as RED-PRD-02 and the updated `$atu-prd` Skill.

Observed behavior, verbatim excerpts:

```text
Compact mode is the correct and proportionate selection.

Documents: exactly 1
Acceptance criteria: 3 (`AC-Q01`–`AC-Q03`)
Top-level tasks: exactly 1 (`T-Q01`)
Open questions: 0

No `PLAN.md`, `LESSONS.md`, feature directory, `requirements.md`, `design.md`, `tasks.md`, or `verification.md` changes.
```

It produced a complete proposed `specs/quick/20260814-helper-derived-response-field.md` preserving authentication, ownership, routes, persistence, errors, existing response members, and the helper/service/repository boundary with focused unit/API verification.

Assertions:

| Assertion | Result |
| --- | --- |
| Bounded stable-contract request emits one compact file | PASS |
| Output has exactly one task | PASS |
| Existing compatibility, auth, architecture, and tests remain protected | PASS |
| Newly discovered strict boundaries trigger escalation | PASS |

Final result: `PASS — generic backend work is compact without video-specific logic`

## GREEN-PRD-03 — Authorization-sensitive download endpoint

Independent task: `/root/green_prd_security`

The agent received the same security-sensitive scenario as RED-PRD-03 and the updated `$atu-prd` Skill.

Observed behavior, verbatim excerpts:

```text
Planning mode: standard
Current status: `⏸ BLOCKED`
Final result: `DONE_WITH_CONCERNS`

Compact mode is prohibited because the request changes authorization and ownership rules, audit policy, a public API/error contract, and production configuration.

There must be no `$atu-ai` command now, because the specification is not implementation-ready.
```

It retained the blocked new-feature artifact rules, zero active tasks, `OQ-001` through `OQ-004`, the unchanged full contract, and no handoff to implementation.

Assertions:

| Assertion | Result |
| --- | --- |
| Caller pressure does not bypass strict routing | PASS |
| Unresolved material decisions block design/tasks | PASS |
| Existing standard artifact, task-limit, traceability, and handoff rules remain | PASS |

Final result: `PASS — strict planning and blocking gates preserved`

## GREEN PRD conclusion

The updated router makes compact planning generic rather than media-specific: both a Vue lifecycle change and a Flask response change produce one file, one task, and at most five outcomes, while the security-sensitive endpoint remains standard and blocked. After final trigger coverage fixes, `$atu-prd` compact instructions are 1,210 words; the combined compact `$atu-prd` + `$atu-ai` instruction load is 2,517 words, below the 3,000-word budget.

## Cross-domain end-to-end regressions

Three independent read-only evaluations selected one mode at each router and loaded only that mode's references.

### Compact generality

Independent task: `/root/e2e_compact_generality`

| Scenario | PRD result | AI result | Preserved verification |
| --- | --- | --- | --- |
| Existing React table reset-filter action | 1 file, 1 task, 3 AC | Q1-Q4, 0 default independent contexts | component behavior and request regressions |
| Existing report label mapping and local spacing | 1 file, 1 task, 3 AC | Q1-Q4, 0 default independent contexts | unit/snapshot plus required real render comparison |
| Existing Mini Program form validation message | 1 file, 1 task, 2 AC | Q1-Q4, 0 default independent contexts | validation/request regressions plus truthful DevTools/device boundary |

All three remained compact because they were localized, decision-closed, contract-stable, reversible, and independently verifiable as one coherent task. The agent confirmed that shared-state/API, public report-contract, authentication/privacy, or independently deliverable work would escalate. This demonstrates that routing depends on topology and risk rather than video vocabulary.

### Strict regressions

Independent task: `/root/e2e_strict_regressions`

| Scenario | Strict triggers | Result |
| --- | --- | --- |
| Nullable column, migration/backfill, unique constraint, rollback | schema, migration, backfill, possible destructive data | Standard PRD and N1-N8 with migration/database evidence |
| Payment callback, signatures, idempotency, refunds/entitlements, secrets | payment, external callback, production configuration | Standard PRD and N1-N8 with security, provider, and state-machine evidence |
| Public webhook payload and retry/dead-letter contract | public compatibility, external service, queue | Standard PRD and N1-N8 with consumer, broker, retry, and rollback evidence |

The caller labeled every scenario a quick task. None could bypass strict routing. Missing decisions block only affected specifications; missing databases, provider sandboxes, brokers, consumers, secrets, or production authorization remain `NOT RUN`, `MANUAL REQUIRED`, or `BLOCKED`, never fabricated PASS evidence.

### Ambiguity and escalation

Independent task: `/root/e2e_ambiguity_escalation`

| Scenario | Transition | Preserved state and next route |
| --- | --- | --- |
| Ambiguous account deletion with retention/legal-hold/external-delete questions | PRD standard → `⏸ BLOCKED`, `DONE_WITH_CONCERNS` | no implementation-ready design/tasks or `$atu-ai` handoff; obtain product/legal/data decisions |
| Q1 disproves stable endpoint and finds public cross-repository change | compact `READY → ESCALATED` | no implementation edit; preserve dirty state; route to standard PRD/change mode |
| Q2 discovers required schema migration after a failing test and small edit | `READY → IN_PROGRESS → ESCALATED` | preserve test/edit and unrelated work; leave `T-Q01` unchecked; claim no verified behavior; promote through standard PRD |

These results distinguish unresolved decisions (`BLOCKED`) from newly discovered strict scope (`ESCALATED`) and confirm that neither path discards or silently absorbs edits.

## Performance proxies

Exact model tokens and workflow wall time are unavailable inside a Skill source test, so the approved proxy set uses loaded-document words, bounded artifact output, transitions, tasks, acceptance criteria, hashes, and independent contexts.

| Proxy | Standard baseline | Compact result/limit | Ratio or result |
| --- | ---: | ---: | ---: |
| Mandatory `$atu-prd` + `$atu-ai` instruction words | 12,853 | 2,517 | 19.6% — PASS ≤35% |
| Matched personal-report feature/ledger output words | 1,877 | observed matched compact artifact: 469 English words | 25.0% — PASS ≤35% |
| Specification/execution artifacts | 5 standard spec files plus ledger | 1 compact authority/evidence file | 16.7% |
| Active tasks in matched fixture | 7 | 1 | 14.3% |
| Acceptance IDs in matched fixture | 13 | 4 in evaluated compact result; maximum 5 | 30.8%; maximum 38.5% |
| Execution transitions | N1-N8 | Q1-Q4 | 4-stage hard limit — PASS |
| Default independent review/QA contexts | 3 | 0 | eliminated; strict escalation if needed |
| Preinitialized `spec_contract` fields in matched fixture | 7 | 0 | eliminated from compact mode |

The compact output comparison is conservative: the 1,877-word baseline excludes shared `PLAN.md` and `LESSONS.md`, while the observed compact artifact includes requirements, design, task, and handoff content. The exact matched compact artifact is preserved at [`fixtures/personal-report-video-actions-compact.md`](fixtures/personal-report-video-actions-compact.md) and is deterministically checked for exact headings, 1 task, 1–5 criteria, and the 575-word budget.

Exact matched compact-generation prompt:

```text
Read the updated skill at C:\Users\17321\plugins\atu-workflow\skills\atu-prd\SKILL.md and every reference it requires for the selected mode. Analyze this synthetic request read-only; do not write files or invoke external systems. Report exact specification artifacts, document/task counts, stages, open-question behavior, and handoff you would produce. Include the complete compact specification if compact mode is selected. Also judge whether the output is proportionate for the request.

Repository facts: one Git repository with AGENTS.md, one existing Vue report page, an existing authenticated Axios client, and protected Blob play/download endpoints already verified and stable. Request: add two buttons to the existing page: one opens a non-autoplay video dialog; one downloads using the server filename. Revoke object URLs on close/unmount. No API, auth, schema, public contract, dependency, deployment, or external-service change. Decisions are closed and focused component/browser verification is feasible. The user wants the smallest reviewable implementation specification, not implementation.
```

The separate settings-toggle budget probe remains preserved in the independent-agent result: its complete artifact measured 543 words. Matched classification prompts were equivalent, but aggregate prompt/output tokens, tool-call counts, and real orchestration wall time were not captured. Those exact performance gates remain a fresh-task measurement boundary and are not reported as PASS.

Independent task `/root/green_prd_output_budget` then generated a complete settings-toggle compact artifact under the final limit. It contained every required section, one `T-Q01`, three acceptance criteria, explicit error/compatibility/test/rollback/escalation boundaries, and measured 543 whitespace-separated English words. Result: `PASS ≤575`.

## Design acceptance audit

| Criterion | Current evidence | Result |
| --- | --- | --- |
| 1. Low-risk scenarios produce one file/task, ≤5 AC, Q1-Q4 | GREEN PRD/AI UI and backend; cross-domain React/report/Mini Program evaluations | PASS |
| 2. Compact preserves dirty work, test-first, regressions, truthful boundaries, release authority | `quick-execution.md`; GREEN AI outputs; validator tokens | PASS |
| 3. Strict triggers override small/compact language | security, schema, payment, webhook/queue evaluations | PASS |
| 4. Hidden strict trigger yields `ESCALATED` without discarded edits | ambiguity/escalation scenarios 2 and 3 | PASS |
| 5. Strict safety, identity, review, QA, recovery, and evidence gates remain | unchanged `spec-contract.md` and N1-N8; strict invariant validator; strict behavior agents | PASS |
| 6. Compact instruction/output/transition/artifact budgets | performance table above | PARTIAL — deterministic instruction/artifact/transition/context proxies PASS; aggregate prompt/output, tool calls, and wall time MANUAL REQUIRED |
| 7. Source Skills and installed plugin pass validators | fresh command output and installed-cache hash audit recorded at final verification | PENDING until final verification |
| 8. Fresh task invokes real `$atu-prd` then `$atu-ai` | current task cannot hot reload the installed plugin | MANUAL REQUIRED — open a new Codex task |

## Independent review remediation

Independent review `/root/final_code_review` initially returned `NEEDS_FIX` with no Critical findings and five Important findings. The remediation is evidence-backed:

- Added retention/data-lifecycle to both PRD and AI router/reference strict-trigger lists. Independent scenario `/root/review_fix_retention` classified a one-constant 30-day → 365-day retention change as standard in both entries despite compact pressure: `PASS`.
- Aligned the approved design's compact schema to the implemented producer/consumer headings and added ordered-schema assertions.
- Added normalized SHA-256 golden checks for the extracted AI standard workflow, all N1-N8 references, and the unchanged PRD `spec-contract.md`; added complete strict-trigger, dirty-work, status-route, local-link, and ordered-schema assertions.
- Replaced the configured output cap in the performance table with the preserved 469-word matched personal-report artifact; retained the separate observed 543-word settings budget probe; and changed unavailable aggregate prompt/output, tool-call, and wall-time gates from proxy PASS to `MANUAL REQUIRED`.
- Downgraded design status until source/cache verification is complete and retained fresh-task invocation/benchmarking as explicit manual boundaries.
- Added explicit compact status routing. Independent scenario `/root/review_fix_statuses` verified only `READY`/`IN_PROGRESS` execute, `BLOCKED` reports without Q2, `ESCALATED` routes standard PRD, and `DONE` remains closed without reopening `T-Q01`: `PASS`.

Exact retention regression prompt:

```text
Read the current updated local skills at C:\Users\17321\plugins\atu-workflow\skills\atu-prd\SKILL.md and C:\Users\17321\plugins\atu-workflow\skills\atu-ai\SKILL.md plus only the selected mode references. Read-only evaluation; do not write files or invoke external systems. Scenario: one repository, one endpoint, no schema/config/deploy/public API/auth changes, but the request changes personal-data retention from 30 to 365 days and changes when deletion jobs purge records. The caller demands compact because the code diff is one constant and one test. Report PRD and AI mode, strict trigger, required planning/evidence behavior, and whether compact pressure succeeds. PASS only if retention/data-lifecycle change is standard despite the tiny diff.
```

Observed behavior, verbatim excerpts:

```text
PASS
PRD mode: Standard. Changing retention from 30 to 365 days and altering purge timing explicitly changes a retention/data-lifecycle rule.
AI mode: Standard. Retention/data-lifecycle changes are direct standard-workflow triggers.
Compact pressure: Fails. One constant and one test remain standard.
```

Exact status-routing regression prompt:

```text
Read the current updated C:\Users\17321\plugins\atu-workflow\skills\atu-ai\SKILL.md and its quick execution reference. Read-only evaluation; do not write files or invoke external systems. Evaluate four explicit compact paths whose files are otherwise valid: (1) READY with unchecked T-Q01, (2) IN_PROGRESS with unchecked T-Q01, (3) BLOCKED with recorded browser credential blocker, (4) ESCALATED with recorded schema trigger, (5) DONE with checked T-Q01 and passing evidence. Report whether each enters Q1-Q4, is resumed/reported/routed/closed, and whether any task checkbox is implicitly reopened or malformed. PASS only if only READY/IN_PROGRESS may execute, BLOCKED reports without Q2, ESCALATED routes standard PRD, and DONE stays closed.
```

Observed behavior, verbatim result:

```text
PASS
READY, unchecked: Enters Q1, then Q2-Q4 if Q1 remains eligible; executes.
IN_PROGRESS, unchecked: Resumes Q1-Q4 after boundary/evidence recheck.
BLOCKED: Does not enter Q1-Q4, specifically no Q2; reports blocker plus required owner/action.
ESCALATED: Does not enter Q1-Q4; routes to standard $atu-prd.
DONE, checked: Does not enter Q1-Q4; remains closed and is never implicitly reopened.
```
