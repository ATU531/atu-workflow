# N1: Initialize

Establish the workflow boundary without changing application source or requirement-authority files. N1 may create or synchronize the execution ledger described below, but N1 does not edit `PLAN.md`.

1. Resolve the `specs/` directory and every authorized code repository from the user's request. If the request points to `specs/PLAN.md`, use its parent as the specs directory. Do not guess an unresolved path.
2. For the specs tree and each code repository, find and read the root `AGENTS.md` plus every more-specific `AGENTS.md` that governs files likely to be touched. Apply the most specific instruction where scopes overlap.
3. When present, read `.claude/CLAUDE.md` and every applicable `.claude/rules/*.md` file. Treat them as compatible repository guidance only: user instructions and the effective `AGENTS.md` files have higher priority. Project guidance supplements the specifications but cannot silently override confirmed product requirements; report a material conflict.
4. Read `specs/PLAN.md` and `specs/LESSONS.md`. Treat reusable decisions and explicit supersession records in `LESSONS.md` as required context. If `PLAN.md` is absent, allow a legacy single-feature specs directory only when it has an unambiguous feature contract.
5. Discover numbered feature directories in plan/dependency order. Verify each ready feature has `requirements.md`, `design.md`, and `tasks.md`; record missing or inconsistent artifacts as blockers instead of fabricating them.
6. Verify every authorized repository path exists and inspect its current branch, `git status`, and relevant working-tree, staged, and untracked changes. Record the baseline before editing.
7. Protect user work: do not reset, checkout, clean, stash, overwrite, reformat, or include unrelated changes. If the assigned task overlaps an existing change and intent cannot be preserved confidently, stop and ask for direction.
8. For every feature that may be executed, initialize or reconcile `specs/<feature>/verification.md`. This file is a durable execution ledger, not a requirements authority and not a substitute for `PLAN.md`, `requirements.md`, `design.md`, `tasks.md`, or current verification.
9. Give each task entry enough durable fields to reconstruct the evidence:
   - task ID;
   - code snapshot: exactly one deterministic commit hash, diff patch hash, or tree/content hash that covers the relevant application and test content;
   - snapshot type, hash value, hash algorithm, and hash scope, including repository, base/ref where applicable, path/content boundary, and whether staged, unstaged, and untracked task content is included; use a commit hash only when it fully identifies that scope;
   - `snapshot=unverifiable` when no deterministic hash can be generated; a changed-file list and timestamp may be supporting metadata but never a snapshot identifier or matching fallback;
   - deterministic `spec_contract` hash value, spec hash algorithm, normalization rules, and spec hash scope;
   - spec hash scope covering at least the task ID and normalized task description (excluding checkbox/execution-state markers), every mapped requirements section/ID, relevant design contract section/ID, and every mapped acceptance-criterion ID and normalized content; record the exact files, sections, and IDs included;
   - `spec_contract=unverifiable` when the required contract content or a deterministic normalized-content hash cannot be resolved;
   - implementation status (`not_started`, `in_progress`, or `implementation_complete`), the exact deterministic application-code snapshot it describes, completion timestamp, and concrete file/diff evidence; ledger and specification bookkeeping alone do not change that implementation snapshot;
   - N1 baseline dirty paths, separated into staged, unstaged, and untracked paths;
   - tests and static checks with exact commands, environment, exit codes, and concise outcomes;
   - self-review, specification-review, and quality-review results and unresolved findings;
   - acceptance-criterion matrix and required regression results;
   - blockers with their classification;
   - next route and evidence timestamp.
10. Record the authorized scope, repositories, feature order, dirty-state baseline, applicable instructions, unresolved blockers, and checks available in each project. In the ledger, store only concise evidence and sanitized excerpts; never write credentials, tokens, private keys, personal data, production payloads, or raw sensitive logs.

At N1 and every later recovery, recompute both identities for each task. Only `implementation_complete` evidence matching the current deterministic application-code snapshot and current deterministic `spec_contract` may support routing an unchecked task to N4. If either identity is missing, mismatched, `snapshot=unverifiable`, or `spec_contract=unverifiable`, invalidate every older implementation, review, and QA result and route to N3.

`$atu-prd` may leave `verification.md` unchanged while editing specification files. Do not require it to rewrite the ledger: `$atu-ai` detects the resulting `spec_contract` mismatch itself and invalidates stale evidence.

If the user prohibits writing `verification.md`, obey the prohibition, record `LEDGER WRITE PROHIBITED` in the node report, and continue only within the authorized scope. N7 must not trust a checkbox or chat summary: without durable dual-identity-matching `implementation_complete` evidence, an unchecked task routes to N3, while a checked task that cannot complete its required atomic recovery stops as `BLOCKED`.

Classify blockers consistently:

- For an unresolved business, security, authorization, destructive-data, external-contract, or scope decision, record the blocker in the ledger and node report and route it to N2. N1 does not edit `PLAN.md`; N2 may set `⏸ BLOCKED` when that specification write is authorized.
- For a missing runtime, dependency, credential, service, browser/device, or pending manual verification before any code or test implementation has begun, preserve the current planned status (including `待开发`) and record `execution blocked` only in the ledger and node report. If implementation had already begun before N1 recovery, record that N2/N3 must retain `🚧 开发中`. Keep the task unchecked in either case; N1 still does not edit PLAN.

Do not push, publish, deploy, or mutate an external environment during initialization.
