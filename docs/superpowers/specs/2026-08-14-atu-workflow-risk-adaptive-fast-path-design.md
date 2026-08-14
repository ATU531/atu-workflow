# ATU Workflow Risk-Adaptive Fast Path Design

## Status

- Date: 2026-08-14
- State: approved in conversation; awaiting written-spec review before implementation planning
- Plugin source: `C:\Users\17321\plugins\atu-workflow`
- Scope: `$atu-prd` and `$atu-ai` orchestration only

## Problem

ATU currently applies one high-assurance workflow to every change. `$atu-prd` reads the full specification contract and emits `PLAN.md`, `LESSONS.md`, `requirements.md`, `design.md`, and `tasks.md`. `$atu-ai` then runs every task through N1-N8, repeated durable-ledger synchronization, deterministic application/specification identities, separate specification and quality reviews, independent QA, and context recovery.

Those controls are appropriate for security, payment, schema, migration, external-contract, destructive, and multi-session work. They are disproportionate for a bounded change that reuses stable contracts and can be implemented and verified as one coherent task.

The current mandatory `$atu-prd` and `$atu-ai` workflow text contains about 12,853 English words before repository specifications, source code, test output, or independent-review contexts are loaded. In the `x_insight_projcet` example, the local personal-report play/download request became seven tasks, thirteen acceptance criteria, an estimated 195 minutes, and seven pre-initialized specification hashes before implementation began. This example is evidence and a regression fixture; no video-specific rule belongs in the plugin.

## Goals

1. Automatically select a compact path for bounded, low-risk, contract-stable changes.
2. Preserve the current strict path for high-risk, ambiguous, broad, or hard-to-verify work.
3. Keep test-first implementation, dirty-worktree protection, truthful evidence, scope control, and explicit blockers in both paths.
4. Make the compact path general across frontend, backend, reports, Mini Programs, Android, tests, documentation, and bounded vertical slices.
5. Reduce compact-path orchestration words to at most 3,000 and measured prompt/output volume to at most 35% of the current baseline on matched evaluation scenarios.
6. Allow safe escalation without discarding user work or silently weakening requirements.

## Non-goals

- Do not remove or weaken the existing strict workflow.
- Do not make feature names such as play, download, button, or CRUD automatic proof of low risk.
- Do not bypass testing, validation, authorization boundaries, or required external/manual evidence.
- Do not introduce a separate `$atu-quick` entry in the first version.
- Do not add source-file or function-length limits in this change.
- Do not modify project repositories while evaluating this plugin change; use synthetic or read-only copies.

## Considered approaches

### 1. Risk-adaptive routing inside the existing entries

Add a compact path to `$atu-prd` and `$atu-ai`, selected by evidence-based eligibility rules. Keep current entry names and preserve the strict path.

This is the selected approach because it reduces user decision burden, retains a safe fallback, and does not fragment plugin discovery.

### 2. Add a separate `$atu-quick` skill

This would isolate instructions but require users to classify work before repository inspection. Misclassification and forgotten entry selection would remain common.

### 3. Simplify the strict workflow globally

This would save the most tokens but remove controls needed by security, data, payment, deployment, and recovery work. It is rejected.

## Architecture

### Lean routers

Both main `SKILL.md` files become lean routers containing:

- common authorization, dirty-worktree, evidence-integrity, and no-release-without-authorization boundaries;
- the mode-selection decision;
- links to exactly one selected workflow reference;
- escalation rules.

Strict-only detail moves out of the main files so a compact run does not pay its context cost. Strict mode loads the preserved standard workflow and existing references. Compact mode loads only its compact contract.

### Proposed resources

```text
skills/
  atu-ai/
    SKILL.md                         # lean router and common invariants
    references/
      quick-execution.md             # compact Q1-Q4 workflow
      standard-workflow.md           # strict-only gates moved from the current main skill
      N1-init.md ... N8-finish.md    # preserved strict node contracts
  atu-prd/
    SKILL.md                         # lean router and common invariants
    references/
      quick-spec-contract.md         # classification and one-file format
      standard-workflow.md           # strict-only PRD procedure
      spec-contract.md               # preserved full strict specification contract
```

Moving text must not change strict-mode meaning. Contract tests will pin the required strict gates before refactoring.

## Mode selection

Mode selection is based on the shape and risk of the requested change, not its label.

### Compact eligibility

A change may use compact mode only when all applicable evidence supports these statements:

- it delivers one bounded, independently observable behavior;
- it affects one repository and a localized module or one bounded vertical slice;
- material product decisions and acceptance outcomes are clear;
- existing authentication, authorization, data, API, event, deployment, and external-service contracts remain stable;
- it introduces no schema migration, data backfill, destructive operation, production configuration, or deployment-topology change;
- it introduces no new third-party service, queue protocol, public API contract, or cross-system consistency rule;
- it is reversible and can be verified with focused checks plus a bounded regression set;
- it can be implemented and verified as one coherent task without hiding independent work.

Consuming an existing authenticated API, persistence abstraction, component, or third-party library does not by itself force strict mode. Creating or changing its security, ownership, protocol, data-lifecycle, or failure contract does.

### Strict-mode triggers

Use strict mode when any of these is present or uncertain:

- new or changed authentication, authorization, privacy, payment, audit, or destructive-data rules;
- schema migration, backfill, retention/lifecycle change, or production configuration;
- new external provider, callback, queue, public API, or compatibility contract;
- cross-repository or broad cross-module state changes;
- unresolved material product, security, scope, or acceptance decisions;
- multiple independently deliverable tasks;
- required verification cannot be made bounded and explicit.

The user may force strict mode. A request to force compact mode cannot override a strict trigger.

## Compact specification

`$atu-prd` writes one file and does not create or update `PLAN.md`, `LESSONS.md`, a numbered feature directory, or `verification.md`:

```text
specs/quick/YYYYMMDD-feature-name.md
```

The filename receives a numeric suffix on collision. The compact file is the complete requirement, design, task, status, and evidence authority for that change.

Required structure:

```markdown
# Feature name

## Status
READY | IN_PROGRESS | DONE | ESCALATED | BLOCKED

## Goal and scope
- Goal
- In scope
- Out of scope
- Reused stable contracts/components

## Compact-mode decision
- Eligibility evidence
- Checked risks
- Escalation triggers

## Design
- Data/interaction flow
- Expected change locations
- Required security, compatibility, error, and lifecycle invariants

## Acceptance criteria
- AC-Q01 ... AC-Q05

## Implementation task
- [ ] T-Q01: one coherent implementation-and-verification task

## Verification result
- Changed files
- Commands and exact outcomes
- Acceptance status
- Manual/external boundaries
```

Rules:

- Use at most five observable acceptance criteria.
- Use exactly one active task.
- Group variants under an observable outcome instead of creating one criterion per status or error code.
- Keep real security, lifecycle, concurrency, compatibility, and error constraints when relevant.
- Do not turn production deployment or optional post-release observation into implementation tasks unless explicitly in scope.

## Compact execution

`$atu-ai` recognizes an explicit compact-spec path, or exactly one `READY` compact spec in the requested project. Multiple candidates require an explicit path.

### Q1: Confirm eligibility

- Read effective `AGENTS.md`, the compact spec, repository status/diff, target code, callers, and nearby tests.
- Protect pre-existing changes.
- Re-check mode eligibility against repository evidence before editing.
- Mark the compact spec `IN_PROGRESS` only when implementation or test editing starts.

### Q2: Implement test-first

- Add or tighten the narrowest meaningful test and observe the expected failure.
- Make the smallest coherent implementation change.
- Run the focused test until it passes.
- Use the smallest applicable domain skill; do not load unrelated roles.

### Q3: Verify once

- Run focused tests and only the relevant supported static/regression checks.
- Inspect the complete task diff once for specification fit, correctness, security, regression risk, readability, and test adequacy.
- Evaluate every compact acceptance criterion against current evidence.
- Use an independent reviewer or QA context only when evidence found during execution raises the task out of compact-mode risk; normally escalate instead of layering strict reviews onto compact mode.

### Q4: Close and report

- Record changed files, exact command outcomes, criterion statuses, and manual/external boundaries in the same compact file.
- Check `T-Q01` and set `DONE` only when required local evidence passes.
- Mark unavailable required evidence truthfully; a required unavailable boundary yields `BLOCKED` rather than a fabricated pass.
- Do not create a separate durable ledger, compute application/specification dual hashes, enter N7, or scan unrelated features.
- Commit, push, deploy, migrate, publish, or perform external writes only under existing explicit authorization rules.

## Escalation and recovery

### Escalation

If a strict trigger appears before or during implementation:

1. Stop compact execution before broadening the change.
2. Preserve user and task changes; do not reset, clean, stash, or discard them.
3. Set the compact spec to `ESCALATED` and record the evidence and affected boundary.
4. Route to `$atu-prd` promotion, which uses the compact file as an authoritative source for standard specifications.
5. Reconcile any already-edited files explicitly in the promoted tasks; do not claim them verified by the compact attempt.

### Interruption recovery

Compact mode uses the compact file plus repository state instead of a separate ledger:

- re-read the compact spec, status, target diff, and nearby tests;
- compare the current diff with the known pre-existing dirty boundary;
- rerun the focused verification rather than trusting chat summaries;
- continue Q2 or Q3 only when ownership and scope remain clear;
- escalate or block on ambiguity.

No specification hash is required. If durable multi-session evidence or complex recovery becomes necessary, promote to strict mode.

## Generality

Compact mode is intended for, but not limited to:

- frontend buttons, forms, filters, field display, local interactions, and styling corrections;
- backend changes that reuse established authentication, service, repository, and API contracts;
- report content, layout, field mapping, and bounded generation behavior;
- Mini Program and Android local UI/state behavior using stable interfaces;
- bounded vertical slices across frontend and backend when contracts remain stable;
- focused tests, documentation synchronization, and local maintainability refactors.

Feature vocabulary never determines mode. A simple-sounding download endpoint may be strict if it introduces authorization or file-access rules; a private-video UI may remain compact when it only consumes an already verified protected API and preserves its contract.

## Evaluation strategy

### RED baselines

Run current skills in independent contexts against the exact prompts and preserve compact prompt/output evidence:

1. Existing protected API plus bounded play/download UI: current expansion is the regression baseline.
2. Simple CRUD or button behavior: detect needless full-spec and full-state-machine work.
3. Local report field/layout change: detect cross-domain overplanning.
4. Bounded backend behavior using existing auth and repository contracts: detect unnecessary architecture expansion.
5. New authorized download endpoint: confirm strict classification.
6. Schema migration, payment callback, or production configuration: confirm strict classification.
7. Material ambiguity or an implementation-time hidden risk: confirm block or escalation.

### GREEN and regression

After each skill change, rerun the same scenarios with the changed skill path. Verify artifacts and behavior, not a summary of intended rules.

Deterministic tests must verify:

- compact and standard resources exist and links resolve;
- the compact schema, maximum five criteria, and exactly one active task;
- compact mode does not require `verification.md`, dual hashes, or N1-N8;
- strict mode retains dirty-worktree protection, dual identities, reviews, QA, recovery, and evidence integrity;
- strict triggers cannot be overridden by a compact request;
- router and compact-reference word budgets;
- existing plugin, skill, metadata, and invocation validation.

### Performance acceptance

For matched behavior scenarios:

- mandatory compact-path instruction text is at most 3,000 English words;
- prompt plus output word count is at most 35% of the current baseline;
- orchestration has at most four transitions and one active task;
- no independent review/QA context is created by default;
- one compact spec replaces the standard specification set and ledger;
- orchestration wall time, excluding actual build/browser/network duration, is at most 50% of baseline;
- when exact token usage is unavailable, record loaded-document words, output words, tool calls, independent contexts, transitions, and artifacts as proxies.

No performance target may be met by skipping a required test, concealing a blocker, or misclassifying a strict scenario.

## Delivery sequence

Skill changes are delivered and tested one at a time:

1. Establish and verify the local Git baseline without a remote.
2. Commit this approved design document.
3. Pin strict-mode invariants and capture RED behavior evidence.
4. Add compact-spec execution to `$atu-ai`; `$atu-prd` still emits only standard specs during this intermediate compatible state.
5. Validate the changed skill, full plugin, compact executor, and strict regressions; update the cachebuster and reinstall.
6. Add compact classification and generation to `$atu-prd`.
7. Validate the changed skill, full plugin, compact generator, strict regressions, and end-to-end handoff; update the cachebuster and reinstall.
8. Run a fresh-task plugin smoke because the active Codex task cannot dynamically reload an updated plugin.

The intermediate plugin remains usable because executor support lands before the generator can emit compact specs.

## Rollback

- Keep each skill change in its own local commit.
- On regression, revert the affected commit, generate a new cachebuster, and reinstall `atu-workflow@personal`.
- Never hand-edit Marketplace during the update loop.
- Keep the strict workflow selectable throughout rollout.
- Do not modify or delete prior cache versions as part of rollback.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Unsafe work is misclassified as compact | Conservative evidence-based triggers, strict-on-uncertainty, negative behavior tests |
| Compact rules become another large workflow | Enforced word budgets and one-file/one-task/four-transition limits |
| Strict semantics regress during extraction | Pin invariant tests before moving text and run strict behavior regressions |
| Compact work expands after editing begins | Explicit escalation that preserves changes and invalidates unverified claims |
| Manual checks block every local delivery | Separate required local completion from explicitly scoped external/release evidence without calling unrun checks passed |
| The implementation becomes video-specific | Use video only as one fixture; require CRUD, report, backend, ambiguity, migration, and payment scenarios |

## Acceptance criteria

1. Low-risk, contract-stable scenarios produce one compact spec, one task, at most five acceptance criteria, and a Q1-Q4 execution trace.
2. Compact runs preserve dirty work, test first, verify relevant regressions, report unavailable evidence, and never infer release authority.
3. Strict-trigger scenarios select the existing full workflow even when the user calls them small or requests compact mode.
4. An execution-time strict trigger produces `ESCALATED` without discarding or silently absorbing edits.
5. Strict-mode behavior retains all current safety, identity, review, QA, recovery, and evidence gates.
6. Compact-path instruction, output, transition, artifact, and orchestration-time budgets pass matched RED/GREEN evaluation.
7. The source plugin, every Skill, and the installed plugin pass their existing validators after each rollout stage.
8. A fresh Codex task can invoke `$atu-prd` to create a compact spec and `$atu-ai` to execute or correctly escalate it.
