---
name: atu-prd
description: Use when the user invokes $atu-prd, asks to decompose a PRD or change request into dependency-ordered implementation specifications, or needs requirements, design, tasks, acceptance criteria, and open questions captured before coding.
---

# ATU PRD

Turn authoritative product requirements into reviewable specifications without implementing business code.

Before doing any PRD work, read [the specification contract](references/spec-contract.md) completely. Follow its document structures, IDs, statuses, task checkbox syntax, change annotations, traceability rules, and final acceptance checklist.

## Non-negotiable boundaries

- Work only on specification artifacts under the approved `specs/` directory. Do not edit application code, tests, migrations, manifests, dependencies, deployment state, or production data.
- Treat `requirements.md`, `design.md`, and `tasks.md` as the only requirement-authority documents. `$atu-prd` never creates or updates optional `verification.md` in any mode; `$atu-ai` may add it as an execution-evidence ledger. If it exists, read it only to avoid deletion or overwrite and preserve it unchanged.
- Treat explicit source material and confirmed user answers as facts. Label unresolved items as open questions; never convert an assumption or recommendation into a decision.
- When a material business, security, authorization, data, migration, or external-contract decision is open, block only the feature that depends on it and downstream consumers. For a new feature, record requirements/open questions and do not create final design/tasks. For a change to an existing feature, preserve every published feature document and version unchanged; do not generate or publish the blocked next version. Set its PLAN status to `⏸ BLOCKED`, continue independent features, and report `DONE_WITH_CONCERNS`.
- Keep feature dependencies acyclic and implementation order explicit.
- Limit every feature to at most eight active top-level task checkboxes as defined by the specification contract. Record dropped tasks as non-checkbox history. Split the feature and update the dependency graph instead of hiding work, combining unrelated slices, or lowering estimates.

## Workflow

1. **Select the mode and authoritative source.**
   - **New mode:** `$atu-prd PROJECT_PATH_OR_REQUIREMENT_FILE`.
     - Apply the contract's [authoritative source discovery](references/spec-contract.md#authoritative-source-discovery) rules for recursive formats, explicit files, exclusions, root inference, and conflicts.
   - **Change mode:** `$atu-prd --change FEATURE_NUMBER_OR_KEY CHANGE_TEXT_FILE_OR_URL`. Resolve the project from an explicit path or the current repository, then locate the feature through `specs/PLAN.md` and its numbered directory.
   - Record included and excluded source paths, versions or dates when available, and mode. If eligible sources conflict, report the conflicting claims and affected features instead of choosing silently.

2. **Discover project context without changing it.**
   - Read applicable `AGENTS.md` files, repository guidance, relevant manifests, architecture/configuration evidence, and the existing module outline.
   - Read `specs/PLAN.md`, `specs/LESSONS.md`, and existing feature specifications when present. In new mode, remove already-covered requirements from the candidate set. If a request changes an existing feature's files, interfaces, data model, or behavior, stop and direct it to change mode rather than creating an overlapping feature.

3. **Normalize the requirement.**
   - Identify goals, actors and permissions, user journeys, functional and non-functional requirements, business invariants, data ownership/lifecycle, interfaces, constraints, exclusions, acceptance evidence, and open questions.
   - Separate `confirmed`, `open`, and `out of scope`. Recommendations may be offered as options, but only a confirmed option becomes a decision.
   - Apply the blocking-question gate per feature. A new blocked feature may receive only `requirements.md` with numbered open questions. An existing blocked feature keeps its published documents unchanged and records the blocker in PLAN/the handoff; continue every independent feature that has sufficient decisions.

4. **Build the feature dependency graph.**
   - Split work into cohesive, independently verifiable delivery slices. Estimate task slices before assigning feature numbers.
   - Apply the contract's canonical active-task counting rule before assigning feature numbers; split any feature that would violate it.
   - Give each feature a kebab-case name, list its inputs/outputs and cross-feature contracts, and form a directed acyclic graph. Topologically order the graph; flag and resolve cycles before writing.

5. **Write the specification set.**
   - Keep all output under `PROJECT_ROOT/specs/`:

     ```text
     specs/
       PLAN.md
       LESSONS.md
       N.feature-name/
         requirements.md
         design.md
         tasks.md
         verification.md  # optional; created by $atu-ai after execution
     ```

   - Create `PLAN.md` even for one feature. Append source events to its source ledger, but maintain one current feature index in place with exactly one row per feature.
   - Create `LESSONS.md` when absent. Keep its ledger append-only: append confirmed reusable decisions and explicit supersession records without editing prior rows.
   - For each ready feature, write exactly the three authority documents in the contract. A new blocked feature receives only `requirements.md`; an existing blocked feature retains its current documents without a new version. Never create or update `verification.md` in any mode, and never count it as an authority document or toward the task limit. Use stable IDs and map every active task to requirement and acceptance IDs.

6. **Apply the selected mode.**
   - **New mode:** assign monotonically increasing feature numbers after the current maximum. Never reuse or renumber existing feature, requirement, acceptance, decision, question, or task IDs.
   - **Change mode:** read `PLAN.md` and the existing documents for the entry feature, including optional `verification.md` read-only, then trace downstream and shared-contract impacts and list every affected feature before editing. Apply the blocking gate before versioning; a blocked change preserves all published documents. Otherwise increment only affected authority documents and report each one's old and new version. Keep `verification.md` unchanged and preserve every unrecognized file without deletion or overwrite. Preserve completed `[x]` tasks exactly; express changes to completed work with new task IDs. Mark changed incomplete tasks and new active tasks with contract tags, and keep dropped incomplete IDs as non-checkbox history. If a `✅ 完成` feature gains any active task, update its single PLAN index row to `待开发`; only the implementation workflow may set `🚧 开发中` after work actually starts or restore `✅ 完成` after verification. Update dependencies, execution order, and `LESSONS.md` only where the confirmed change requires it.
   - If a change violates the canonical task limit or creates a distinct delivery slice, add a new numbered feature and update the graph.

7. **Run the consistency review.**
   - Execute every item in the contract's acceptance checklist.
   - Recount active top-level task checkboxes, verify the graph is acyclic, validate all local links, and check bidirectional traceability: source requirement → feature requirement → acceptance criterion → task.
   - Report `DONE` only when every planned feature has final specifications and no blocking decision remains. Otherwise report `DONE_WITH_CONCERNS`, list exact blockers and affected IDs, and distinguish ready independent features from blocked features.

## Required handoff

Report the authoritative sources used, mode, created or changed files, per-authority-document version transitions, feature dependency order and status, per-feature active task counts and estimates, unresolved questions, verification performed, and final status. Invite the user to review the specifications before invoking `$atu-ai`; never start implementation from this skill.
