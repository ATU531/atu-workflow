# S4: Close or recover

Close only from current S3 evidence. Recovery re-establishes current truth without forcing historical work through obsolete audit ceremonies.

## Close

1. Confirm every task is `[x]` or `[DROPPED]`, the feature acceptance matrix passes, required regressions pass, and any triggered independent review or independent QA has no unresolved blocking result.
2. Set the feature to `✅ 完成`. Keep it `🚧 开发中` for an execution or manual-evidence blocker, or set `⏸ BLOCKED` for an unresolved material decision.
3. Append `LESSONS.md` only for a reusable architectural decision, non-obvious failure mode, cross-feature effect, or environment constraint.
4. Use [documentation guidance](documentation.md) only when verified implementation changed affected operator, API, schema, environment, deployment, architecture, or feature documentation. Complete the affected documentation within the authorized scope before final closure.
5. Create or update `verification.md` when the work spans sessions, contains multiple tasks needing durable handoff, or project instructions require it. Write one concise feature-level record with commands, outcomes, acceptance statuses, blockers, and optional reviewed snapshot hash; do not duplicate requirements or raw logs.

Commit only with explicit authorization or an effective repository instruction. Stage only verified scope. Do not push, publish, deploy, migrate, release, or perform another external action without separate authorization.

## Recover

On a later run, re-read effective instructions, current specifications and task states, repository status, current diff, and available verification record. Treat current files and executable checks as truth; chat summaries and old hashes are supporting context only.

- If the specification or code changed, rerun the affected S2 checks and S3 feature verification.
- Do not automatically uncheck completed tasks merely because a ledger or historical hash is missing.
- If a completed marker materially conflicts with current code, tests, or acceptance evidence, report the conflict and either revalidate the affected work or request direction when scope is unclear.
- Preserve unexplained pre-existing or concurrent changes and stop when ownership cannot be determined safely.

After closing one feature, return to S1 for another authorized ready feature. Otherwise report `COMPLETED`, `BLOCKED`, and `NEXT STEP`; use `DONE` only when no blocker remains.
