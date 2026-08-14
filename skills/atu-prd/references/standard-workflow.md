# Standard ATU PRD Workflow

Use this workflow for multi-feature or multi-task work, change-mode versioning, strict risk boundaries, material uncertainty, or a user-forced standard run.

Before doing standard PRD work, read [the specification contract](spec-contract.md) completely. Follow its document structures, IDs, statuses, task checkbox syntax, change annotations, traceability rules, blocking-question gate, and final acceptance checklist.

## Non-negotiable boundaries

- Treat `requirements.md`, `design.md`, and `tasks.md` as the only requirement-authority documents. `$atu-prd` never creates or updates optional `verification.md`; `$atu-ai` may add it as an execution-evidence ledger. If it exists, read it only to avoid deletion or overwrite and preserve it unchanged.
- When a material business, security, authorization, data, migration, or external-contract decision is open, block only the feature that depends on it and downstream consumers. For a new feature, record requirements/open questions and do not create final design/tasks. For a change to an existing feature, preserve every published feature document and version unchanged; do not publish the blocked next version. Set its PLAN status to `⏸ BLOCKED`, continue independent features, and report `DONE_WITH_CONCERNS`.
- Keep feature dependencies acyclic and implementation order explicit.
- Limit every feature to at most eight active top-level task checkboxes under the canonical counting rule. Split the feature and update the dependency graph instead of combining unrelated slices or lowering estimates.

## Workflow

1. **Select the mode and authoritative source.**
   - New mode: `$atu-prd PROJECT_PATH_OR_REQUIREMENT_FILE`. Apply the contract's authoritative-source discovery rules.
   - Change mode: `$atu-prd --change FEATURE_NUMBER_OR_KEY CHANGE_TEXT_FILE_OR_URL`. Resolve the repository and locate the feature through `specs/PLAN.md`.
   - Record included and excluded sources, versions/dates, mode, and conflicts. Never silently choose between conflicting claims.

2. **Discover project context without changing it.**
   - Read applicable repository guidance, architecture/configuration evidence, manifests, and the relevant module outline.
   - Read `specs/PLAN.md`, `specs/LESSONS.md`, and relevant existing feature specifications. Remove already-covered requirements. Route a request that changes existing specified files, interfaces, data, or behavior to change mode rather than creating an overlapping feature.

3. **Normalize the requirement.**
   - Identify goals, actors/permissions, journeys, functional and non-functional requirements, business invariants, data ownership/lifecycle, interfaces, constraints, exclusions, acceptance evidence, and questions.
   - Separate confirmed, open, and out-of-scope items. Apply the blocking-question gate per feature; continue independent features with closed decisions.

4. **Build the feature dependency graph.**
   - Split cohesive, independently verifiable delivery slices and estimate tasks before numbering features.
   - Apply the active-task counting rule. Give each feature a kebab-case name, inputs/outputs, and cross-feature contracts. Form a directed acyclic graph and topologically order it before writing.

5. **Write the standard specification set.**

   ```text
   specs/
     PLAN.md
     LESSONS.md
     N.feature-name/
       requirements.md
       design.md
       tasks.md
       verification.md  # optional; created by $atu-ai
   ```

   Create `PLAN.md` even for one feature. Maintain its append-only source ledger and one current feature index. Create `LESSONS.md` when absent and keep confirmed reusable decisions/supersessions append-only. Write exactly the three authority documents for each ready feature. A new blocked feature receives only `requirements.md`; a blocked existing feature retains its published documents. Never create or update `verification.md`. Use stable permanent IDs and map every active task to requirement and acceptance IDs.

6. **Apply new or change rules.**
   - New: allocate feature numbers after the current maximum; never reuse or renumber published IDs.
   - Change: inspect the entry feature and every downstream/shared-contract impact before editing. Preserve completed `[x]` tasks byte-for-byte; use new task IDs for changes to completed behavior. Version only affected authority documents, retain dropped incomplete work as non-checkbox history, keep optional ledgers and unrecognized files unchanged, and synchronize PLAN dependencies/order/contracts/status. If a completed feature gains active work, set it to `待开发`; only implementation may set `🚧 开发中` or restore `✅ 完成`.
   - Add another numbered feature when the canonical task limit or a distinct delivery slice requires it.

7. **Run the consistency review.**
   - Execute the contract's complete acceptance checklist.
   - Recount active tasks, prove the graph is acyclic, resolve local links, and validate bidirectional source → requirement → acceptance → task traceability.
   - Report `DONE` only when every planned feature has final specifications and no blocking decision remains. Otherwise report `DONE_WITH_CONCERNS` with exact blockers and ready versus blocked features.

## Required handoff

Report authoritative sources, mode, created/changed files, authority-document version transitions, feature dependency order/status, active task counts/estimates, unresolved questions, verification performed, and final status. Invite review before a copyable `$atu-ai` command; never start implementation from this Skill.
