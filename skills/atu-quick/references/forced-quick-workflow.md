# Forced Quick Workflow

## Entry and authority

Accept `$atu-quick <requirement>` or `$atu-quick <specs/quick/file.md>`. Explicit invocation chooses this workflow and acknowledges its risk-category override. It does not authorize an unnamed commit, push, publish, deploy, real payment, production migration, deletion, or external write. The request or effective project instructions must name each such action and target.

Authorization, payment, migration, backfill, public API, compatibility, privacy, audit, external-service, callback, queue, production-configuration, deployment-topology, cross-module, cross-repository, broad-state, and unbounded-verification categories never cause automatic escalation. Record applicable categories and design around them. A newly discovered category is added to the record and execution continues unless it exposes a missing decision or unnamed action authority; then use `BLOCKED`, never automatic promotion.

## Specification contract

Write or resume exactly one authority/evidence file:

```text
specs/quick/YYYYMMDD-feature-name.md
```

Use a unique lowercase kebab-case name; add `-2`, `-3`, and so on for collisions. Use this exact order:

```markdown
# Feature name

- Status: READY | IN_PROGRESS | DONE | BLOCKED
- Mode: forced-quick
- Override: explicit $atu-quick invocation
- Date: YYYY-MM-DD
- Source: request, named files, and repository evidence

## Goal
## Scope
## Risk override and action authorization
## Reused contracts and evidence
## Bounded design
## Acceptance criteria
## Task
## Execution evidence
## Open questions
## Handoff
```

Create contiguous `AC-Q01` through at most `AC-Q05` and exactly one `T-Q01`. The one `T-Q01` covers implementation, focused tests, relevant regression, combined review, and acceptance verification. Keep the initial file within 575 English words or about 800 CJK characters. Do not create or update `PLAN.md`, `LESSONS.md`, numbered feature files, standard authority documents, or a separate `verification.md`.

Natural-language input produces the complete file and immediately continues below; no second approval is required. Before resuming a named file, validate its path under `specs/quick/`, required metadata, exact section order, one to five contiguous `AC-Q*`, exactly one `T-Q01`, and initial size limit; otherwise set `BLOCKED` before Q2. `READY` or `IN_PROGRESS` executes, `BLOCKED` resumes only after its recorded condition changes, and `DONE` stays closed.

## Q1: Establish contract and boundary

Read repository instructions, status and relevant diffs, requirement sources, target code, callers, configuration, and nearby tests. Record pre-existing staged, unstaged, and untracked changes. Confirm one coherent outcome, source decisions, recognized risks, requested repositories, and exact action authority. Related cross-module or cross-repository work may stay in one task.

Write `READY`, then set `IN_PROGRESS` only when the first test or implementation edit starts. If unrelated deliverables cannot form one outcome, or a material behavior, business, security, payment, migration, data, compatibility, or destructive-operation decision is missing, set `BLOCKED` and ask only for that decision.

## Q2: Implement test-first

Read only guidance needed for the changed boundary: [frontend](../../atu-ai/references/domains/frontend.md), [backend](../../atu-ai/references/domains/backend.md), [database](../../atu-ai/references/domains/database.md), or [verification](../../atu-ai/references/verification.md) for test-only work. Use `$atu-android-engineer` or `$atu-miniprogram-engineer` for native platform work. Ordinary edits need no extra role context; use multiple references when the change needs them. These references do not override forced-quick routing or add independent QA.

Add or tighten the narrowest meaningful automated test and observe its expected failure before changing behavior. If safe automation is infeasible, record why and the concrete manual evidence required. Make the smallest coherent implementation, avoid speculative abstractions and unrelated cleanup, run focused tests to green, run nearby regressions, and preserve unrelated work.

## Q3: Verify once

On one current snapshot:

1. Run focused tests and only repository-supported static, build, security, browser, device, migration, contract, or regression checks required by the change.
2. Review the complete diff against every `AC-Q*`, repository rules, architecture, authorization, data lifecycle, payment, errors, concurrency, compatibility, readability, and test adequacy.
3. Record one evidence row per criterion.
4. Repair defects through Q2 and rerun the entire combined pass.

Record unavailable required real evidence as `NOT RUN` or `MANUAL REQUIRED`; mocks do not prove a real boundary. Do not create default independent review, QA, dual-hash, or durable-ledger contexts.

## Q4: Close truthfully

Record workflow status and execution evidence only in the forced file: changed paths, concise diff scope, exact commands, environments, exit codes, useful results, acceptance rows, and manual/external boundaries. When verified behavior changes require project documentation updates, use [documentation guidance](../../atu-ai/references/documentation.md) and update only affected docs within the authorized scope. Check `T-Q01` and set `DONE` only when every required acceptance result passes and required documentation is current. Otherwise leave it unchecked and set `BLOCKED` with the smallest missing decision, evidence, or authorization and its owner.

## Blocking and recovery

Category risk, broad verification, or a changed shared contract does not block by itself. Block only for a missing material decision, unrelated outcomes, unavailable required acceptance evidence, or an unauthorized requested action. Do not convert a blocker to standard mode; the user may separately choose `$atu-prd`.

On a later `$atu-quick <file>` run, re-read the file, repository instructions, status, relevant diff, pre-existing dirty boundary, and nearby tests. Rerun current evidence instead of trusting chat history.

Quick reference:

| Evidence | Route |
|---|---|
| Strict category with closed decisions | Record and continue Q1-Q4 |
| New strict category during implementation | Append and continue |
| Missing material decision | `BLOCKED` |
| Required real check unavailable | `BLOCKED` with `NOT RUN` or `MANUAL REQUIRED` |
| External or production action unnamed | Do not perform it; block only if acceptance requires it |

## Output

```text
COMPLETED
- List implemented behavior and current evidence.

BLOCKED
- Write none, or the exact unfinished decision, evidence, or authorization.

NEXT STEP
- Write none, or the smallest concrete action and owner.
```
