---
name: atu-doc-syncer
description: Use when completed code or configuration changes require affected README, AGENTS.md, project rules, API, environment, deployment, architecture, or feature changelog documentation to be synchronized with verified repository state.
---

# Documentation Syncer

Synchronize only documentation affected by verified implementation changes. Code, configuration, and executed validation are the source of truth; plans and unchecked task boxes are not evidence of completion.

## Establish the contract

Before editing:

1. Read the repository's `AGENTS.md` and any nested `AGENTS.md` governing the documentation files.
2. Read the current feature's `requirements.md`, `design.md`, `tasks.md`, and `LESSONS.md` when present.
3. Inspect `git status`, the relevant diff, and changed runtime/configuration files. Preserve user-authored documentation and unrelated work.
4. Identify exactly which documented facts changed: commands, modules, paths, APIs, schemas, environment variables, deployment steps, operational behavior, or architectural decisions.

Do not broadly rewrite README files, create new rule files, or reformat unrelated sections. If implementation status is unclear, document the uncertainty or leave the claim unchanged.

## Synchronize affected surfaces

Update only the surfaces whose facts changed:

- **README or operator guide:** project summary, affected architecture/module list, quick-start command, API summary, configuration, or deployment instruction.
- **AGENTS.md or project rules:** only durable repository-wide conventions, commands, paths, or module boundaries. Keep nested scope rules in the correct directory.
- **API/config/deployment docs:** exact methods, paths, fields, error behavior, environment names, defaults, prerequisites, and verified commands.
- **Feature changelog:** record implemented behavior and key files only when the change is actually present. Include verified architectural decisions from `LESSONS.md` when relevant.

Preserve useful existing content. Prefer precise local edits over regenerated "complete" documents. Do not expose secrets or copy live credentials into examples.

## Truthfulness rules

- Do not turn requirements, planned tasks, TODOs, mocks, or proposed designs into past-tense completion claims.
- Do not mark a task, acceptance criterion, deployment, migration, build, test, or release complete without supporting repository or execution evidence.
- Keep planned and implemented behavior visibly distinct.
- Do not document commands that are absent from actual scripts/build files unless clearly labeled as proposed.
- Do not claim environment/configuration parity without comparing the authoritative sample/schema.

## Verify consistency

Check only relevant assertions:

- referenced files and rule paths exist;
- documented commands match package scripts, build files, or operator scripts;
- documented environment variables match the configuration schema and examples;
- API and model descriptions match current code/migrations;
- links, headings, and relative paths resolve;
- changelog statements match the diff and current feature status.

If a check was not run or cannot be established, say so. Never report documentation consistency as passed when verification failed or was skipped.

## Report

- List documentation files changed and the code/config evidence for each change.
- Summarize unaffected documentation deliberately left untouched.
- Report consistency checks and outcomes.
- Identify uncertain implementation status, stale facts outside scope, manual follow-ups, and blockers.
