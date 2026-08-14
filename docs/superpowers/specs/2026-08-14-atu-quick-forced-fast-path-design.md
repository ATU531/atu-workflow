# `$atu-quick` Forced Fast Path Design

- Date: 2026-08-14
- Status: Approved
- Scope: Add one explicit end-to-end entry to `atu-workflow`

## Problem

The existing risk-adaptive flow reduces routine work, but `$atu-prd` and `$atu-ai` still force authorization, payment, migration, public API, external-service, production-configuration, and similar categories into the standard workflow. That is correct for automatic routing but prevents the user from deliberately choosing a faster path when they already accept the process risk.

The new entry must reduce orchestration time and token use without weakening truthful evidence, inventing missing product decisions, or turning workflow selection into release or production authority.

## Decision

Add an isolated `$atu-quick` Skill. An explicit invocation selects a forced compact workflow and bypasses category-based strict triggers. It creates or resumes one compact specification and immediately executes Q1-Q4 in the same invocation; it does not wait for a second design approval.

Keep `$atu-prd` and its automatic eligibility rules unchanged. Keep `$atu-ai` strict behavior unchanged except for a small routing guard: a file with `Mode: forced-quick` is handed back to `$atu-quick <path>` instead of being reclassified or promoted.

Rejected alternatives:

- Adding an override marker to both `$atu-prd` and `$atu-ai` couples the forced path to two conservative routers and creates more drift risk.
- A global switch would silently weaken ordinary entrypoints and is outside the requested scope.

## Invocation and authority

Supported forms:

```text
$atu-quick <natural-language requirement>
$atu-quick <path/to/specs/quick/file.md>
```

The explicit invocation is the user's choice of workflow and acknowledgement that strict risk categories may be handled in the fast path. It is not, by itself, authority to commit, push, publish, deploy, execute a real payment, run a production migration, delete data, or perform another external write. Those actions are authorized only when the same request or effective project instructions explicitly name the action and target.

Authorization, payment, migration, public API, privacy, audit, external-service, queue, production-configuration, deployment-topology, cross-module, and cross-repository categories never cause automatic escalation. Their concrete design and verification implications still have to be recorded and checked.

## Boundaries

The forced path accepts one coherent user outcome, one authority file, one top-level implementation-and-verification task, and up to five observable acceptance criteria. A coherent outcome may span multiple files, modules, or repositories when the request and ownership remain explicit.

Block only when one of these conditions prevents correct execution:

- a material behavior, business, authorization, payment, migration, data, compatibility, or destructive-operation decision is missing and cannot be established from authoritative repository evidence;
- the request contains unrelated independently deliverable outcomes that cannot be represented as one coherent task;
- a required environment, credential, device, provider, or real-boundary check is unavailable and that check is required for acceptance; or
- the requested external or production action is not explicitly authorized.

Do not translate those blockers into standard-workflow escalation. Report the smallest decision, evidence, or authorization needed and retain `BLOCKED` until it changes. The user may separately choose `$atu-prd` if they want to switch workflows.

## Components

### `skills/atu-quick/SKILL.md`

A lean router with discovery metadata, common invariants, input selection, and one required link to the forced workflow reference. It does not load `$atu-prd` or `$atu-ai` instructions. It loads only the smallest applicable ATU domain Skill during implementation.

### `skills/atu-quick/references/forced-quick-workflow.md`

The single detailed contract for file shape, statuses, Q1-Q4, blocking, recovery, reporting, and action authorization. Keeping the detail in one reference makes the main Skill easy to discover and keeps normal conversations small.

### `skills/atu-quick/agents/openai.yaml`

Generated UI metadata with `display_name`, `short_description`, and a default `$atu-quick` prompt. It contains no optional branding fields.

### Existing routers

`$atu-prd` remains unchanged. `$atu-ai` gains only a forced-mode routing guard and continues to reject attempts to force its own ordinary compact mode past strict triggers.

## Forced quick specification

Write exactly one authority and evidence file:

```text
specs/quick/YYYYMMDD-feature-name.md
```

Use a unique lowercase kebab-case name. The required section order is:

1. title and metadata;
2. goal;
3. scope;
4. risk override and action authorization;
5. reused contracts and evidence;
6. bounded design;
7. acceptance criteria;
8. the single task;
9. execution evidence;
10. open questions; and
11. handoff.

Required metadata:

```text
Status: READY | IN_PROGRESS | DONE | BLOCKED
Mode: forced-quick
Override: explicit $atu-quick invocation
Date: YYYY-MM-DD
Source: request, named files, and repository evidence
```

Use contiguous `AC-Q01` through at most `AC-Q05` and exactly one `T-Q01`. Do not create or update `PLAN.md`, `LESSONS.md`, numbered feature directories, standard authority documents, or a separate `verification.md`.

The initial specification is limited to 575 whitespace-separated English words or about 800 CJK characters. It may be updated with concise execution evidence after implementation.

## Execution flow

### Q1: Establish the contract and boundary

Read effective repository instructions, status and relevant diffs, target code, callers, configuration, nearby tests, and named requirement sources. Record all pre-existing staged, unstaged, and untracked changes without resetting, cleaning, stashing, overwriting, or absorbing them.

Create the forced quick file from natural language, or validate and resume the named forced quick file. Record recognized risk categories and the exact action authorization boundary. Category risk is evidence to design around, never a promotion trigger.

Set `IN_PROGRESS` only when the first test or implementation edit begins.

### Q2: Implement test-first

Load only the smallest applicable domain Skill. Add or tighten the narrowest meaningful automated test and observe the expected failure before editing production behavior. When safe automation is infeasible, record why and identify the concrete manual or real-boundary evidence.

Make the smallest coherent implementation that satisfies the design. Avoid speculative abstractions and unrelated cleanup. Run the focused test to green, run relevant nearby regressions, and preserve unrelated worktree changes.

If a new strict category appears, add it to the risk record and continue within the authorized scope. If it exposes a missing decision or action authority, set `BLOCKED` instead of `ESCALATED`.

### Q3: Verify once

Use one current snapshot for a combined pass:

- run focused tests and repository-supported static, build, security, browser, device, migration, contract, or regression checks required by the changed behavior;
- review the complete task diff against every acceptance criterion, repository rules, architecture, authorization, data lifecycle, payment, errors, concurrency, compatibility, readability, and test adequacy;
- record one evidence row per acceptance criterion; and
- repair defects through Q2, then rerun the complete combined pass.

Unavailable real evidence is `NOT RUN` or `MANUAL REQUIRED`, never a mock-backed pass. Do not create default independent specification-review, quality-review, QA, dual-hash, or durable-ledger contexts.

### Q4: Close truthfully

Update the selected forced quick file with changed files, concise diff scope, exact verification commands and results, acceptance evidence, and manual or external boundaries.

Set `DONE` and check `T-Q01` only when all required acceptance evidence passes. Otherwise keep the task unchecked and set `BLOCKED` with the smallest next action and owner. A later `$atu-quick <path>` re-reads repository state and reruns focused evidence instead of trusting chat history.

## Token and time budget

- `SKILL.md` plus the forced workflow reference must not exceed 1,100 whitespace-separated English words; target about 900.
- The forced entry must not load `$atu-prd` or `$atu-ai` workflow references.
- It loads exactly one most-relevant ATU domain Skill for implementation; crossing modules or repositories does not automatically load additional domain Skills.
- The default path contains one combined verification pass and no automatic independent review or QA contexts.
- The initial authority file observes the 575-word or approximately 800-CJK-character limit.

## Testing strategy

Follow RED-GREEN-REFACTOR for the Skill itself.

### RED

Add a validator that fails because `atu-quick` and its contract do not exist. Run read-only fresh-context behavior scenarios without the new Skill and preserve evidence that the current routers reject forced authorization, payment, migration, and public-API cases or require the standard workflow.

### GREEN

Initialize the new Skill with the supported generator, then write the minimum contract that makes these scenarios pass:

- authorization-sensitive local code change remains forced quick;
- payment or callback contract change remains forced quick;
- schema migration and public API change remain forced quick;
- a newly discovered strict category is recorded and execution continues;
- a missing material decision becomes `BLOCKED`, not guessed or escalated; and
- workflow selection alone does not authorize a production or external action.

All scenarios are read-only and synthetic; they do not call payment providers, production databases, deployment systems, or other external systems.

### Regression and installation

Run the new forced-quick validator, the existing risk-adaptive validator and strict golden checks, `validate_workflow.py`, `quick_validate.py` for every Skill, and plugin validation. Update documentation and plugin example prompts. Refresh the plugin through the supported cachebuster and reinstall flow, then verify the enabled version and source/cache hashes. A fresh Codex task remains the final manual discovery check.

## Planned file impact

Create:

- `skills/atu-quick/SKILL.md`
- `skills/atu-quick/references/forced-quick-workflow.md`
- `skills/atu-quick/agents/openai.yaml`
- `tests/validate_forced_quick.py`
- `tests/forced-quick-evidence.md`

Modify:

- `skills/atu-ai/SKILL.md`
- `tests/validate_workflow.py`
- `tests/README.md`
- `README.md`
- `.codex-plugin/plugin.json`

The implementation must not configure a remote or push. Local commits are allowed. Marketplace configuration is not edited manually; plugin refresh uses the supported update and reinstall tooling.

## Acceptance outcomes

1. Explicit `$atu-quick` creates or resumes one forced quick file and begins Q1-Q4 in the same invocation without a second approval gate.
2. Authorization, payment, migration, public API, and other strict categories do not automatically select or promote to the standard workflow.
3. Missing decisions, required evidence, or action authorization block truthfully without inventing behavior.
4. `$atu-prd` automatic strict routing and `$atu-ai` ordinary compact eligibility remain intact.
5. The forced entry stays within its instruction budget and passes behavioral, structural, regression, plugin, installation, and cache-consistency checks.
