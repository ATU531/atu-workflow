# ATU Workflow Risk-Adaptive Fast Path Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a general risk-adaptive compact path to `$atu-prd` and `$atu-ai` so bounded, contract-stable changes use one compact specification and a four-stage execution flow while high-risk work retains the existing strict workflow.

**Architecture:** Convert each main `SKILL.md` into a lean router with shared safety invariants and mode selection. Move strict-only instructions into standard references without changing their meaning, and add compact references for one-file planning and Q1-Q4 execution. Deliver `$atu-ai` support first, validate and reinstall it, then deliver `$atu-prd` generation so no installed intermediate version emits an unsupported artifact.

**Tech Stack:** Markdown Agent Skills, Python 3 standard-library validators, Git, Codex plugin cachebuster/install CLI, independent skill behavior evaluations.

## Global Constraints

- Work only in `C:\Users\17321\plugins\atu-workflow`; never edit the installed cache or Marketplace JSON by hand.
- Preserve the existing strict N1-N8 semantics, dirty-worktree protection, dual identities, review, QA, recovery, evidence integrity, and release authorization boundaries.
- Compact mode uses one file, one active task, at most five observable acceptance criteria, and Q1-Q4.
- Compact mode remains test-first and evidence-based; speed targets never authorize skipped required checks or fabricated passes.
- A compact request cannot override a strict trigger; uncertainty selects strict mode.
- Video play/download is one regression fixture, not a hard-coded classifier rule.
- Do not add file/function line limits in this feature.
- Change and deploy one Skill at a time.

---

## File map

- `skills/atu-ai/SKILL.md`: lean execution router, common invariants, compact/strict selection.
- `skills/atu-ai/references/standard-workflow.md`: strict-only rules extracted from the current main skill.
- `skills/atu-ai/references/quick-execution.md`: Q1-Q4 compact execution contract.
- `skills/atu-prd/SKILL.md`: lean planning router, common invariants, compact/strict selection.
- `skills/atu-prd/references/standard-workflow.md`: strict-only planning workflow extracted from the current main skill.
- `skills/atu-prd/references/quick-spec-contract.md`: compact eligibility and one-file schema.
- `tests/validate_risk_adaptive.py`: deterministic router, strict-invariant, compact-schema, link, and word-budget checks.
- `tests/risk-adaptive-fast-path-evidence.md`: exact RED/GREEN prompts, observed behavior, artifact/word/context metrics, and conclusions.
- `tests/validate_workflow.py`: require the new references and preserve the existing plugin contract checks.
- `README.md`: document automatic compact/strict routing and the copyable two-entry workflow.

## Interfaces

- Compact PRD artifact: `specs/quick/YYYYMMDD-feature-name.md` with statuses `READY`, `IN_PROGRESS`, `DONE`, `ESCALATED`, or `BLOCKED`.
- Compact IDs: acceptance criteria `AC-Q01` through `AC-Q05`; exactly one task `T-Q01`.
- `$atu-ai` input: an explicit compact-spec path, or exactly one `READY` compact spec under the requested project.
- Compact execution output: the same file receives changed files, exact command outcomes, criterion states, and manual/external boundaries.
- Promotion interface: set the compact file to `ESCALATED`, record the strict trigger, and route it back to `$atu-prd` as an authoritative source for standard specs.

---

### Task 1: Pin current behavior and strict execution invariants

**Files:**
- Create: `tests/validate_risk_adaptive.py`
- Create: `tests/risk-adaptive-fast-path-evidence.md`
- Modify: `tests/validate_workflow.py`

**Interfaces:**
- Consumes: current `$atu-ai`, its N1-N8 references, and the approved design.
- Produces: failing compact-execution assertions plus passing strict-invariant assertions that Task 2 must preserve.

- [ ] **Step 1: Run independent RED behavior scenarios against current `$atu-ai`**

Use three read-only prompts: a compact protected-API UI change, a simple local backend behavior using stable auth/repository contracts, and a new authorization-sensitive download endpoint. Record the exact prompts and compact final outputs in `tests/risk-adaptive-fast-path-evidence.md`. Expected: the first two cannot enter a Q1-Q4 compact path; the third remains strict.

- [ ] **Step 2: Write the failing execution validator**

Create a stdlib Python validator with these assertions:

```python
AI = ROOT / "skills" / "atu-ai"
require((AI / "references" / "quick-execution.md").is_file(), "missing quick execution")
require((AI / "references" / "standard-workflow.md").is_file(), "missing standard workflow")
main = read(AI / "SKILL.md")
require("references/quick-execution.md" in main, "atu-ai does not route compact specs")
require("references/standard-workflow.md" in main, "atu-ai does not route strict specs")
```

Also pin strict terms across `standard-workflow.md` plus N1-N8: `spec_contract`, `verification.md`, `N4`, `N6`, `N7`, deterministic snapshot, independent specification review, independent quality review, and checked-task recovery.

- [ ] **Step 3: Run the validator and observe RED**

Run:

```powershell
python tests\validate_risk_adaptive.py
```

Expected: FAIL with `missing quick execution`; strict checks against the current sources remain independently evidenced.

- [ ] **Step 4: Extend the existing structural validator**

Add the future quick/standard reference filenames to explicit required sets, but keep the new assertions in `validate_risk_adaptive.py` so the current RED remains specific.

- [ ] **Step 5: Commit the RED tests and evidence**

```powershell
git add tests\validate_risk_adaptive.py tests\risk-adaptive-fast-path-evidence.md tests\validate_workflow.py
git commit -m "test: pin adaptive workflow contracts"
```

---

### Task 2: Add compact execution to `$atu-ai`

**Files:**
- Modify: `skills/atu-ai/SKILL.md`
- Create: `skills/atu-ai/references/standard-workflow.md`
- Create: `skills/atu-ai/references/quick-execution.md`
- Modify: `tests/validate_risk_adaptive.py`
- Modify: `tests/risk-adaptive-fast-path-evidence.md`

**Interfaces:**
- Consumes: compact artifact/status/ID interface and pinned strict invariants.
- Produces: an execution router that loads exactly one of `quick-execution.md` or `standard-workflow.md`.

- [ ] **Step 1: Extract strict-only main-skill content without semantic loss**

Move the current hard gates, N1-N8 state machine, node-transition report, blocked routing, and node-reference map into `references/standard-workflow.md`. Keep all current N1-N8 files unchanged.

- [ ] **Step 2: Write the lean `$atu-ai` router**

Keep the frontmatter trigger, common authorization/dirty-work/evidence/no-release boundaries, compact-file detection, strict-on-uncertainty rule, and two direct reference links. The router must not summarize Q1-Q4 or N1-N8 in enough detail to bypass their reference files.

- [ ] **Step 3: Write `quick-execution.md`**

Define Q1 eligibility confirmation, Q2 failing-test-first implementation, Q3 one combined verification/review/acceptance pass, Q4 compact evidence/status closure, escalation, interruption recovery, and report contract. Explicitly prohibit a separate ledger, dual hashes, N7, unrelated feature scans, and default independent reviewer/QA contexts.

- [ ] **Step 4: Complete deterministic execution assertions**

Assert:

```python
require(all(f"Q{i}" in quick for i in range(1, 5)), "quick execution lacks Q1-Q4")
require(words(main) + words(quick) <= 1600, "atu-ai compact instruction budget exceeded")
require("strict" in main.lower() and "uncertain" in main.lower(), "strict-on-uncertainty missing")
```

Verify every Markdown link in `atu-ai/SKILL.md` resolves and every pinned strict invariant remains present.

- [ ] **Step 5: Run GREEN structural validation**

Run:

```powershell
python tests\validate_risk_adaptive.py --scope ai
python tests\validate_workflow.py
python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\atu-ai
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .
```

Expected: all AI-scope and existing plugin checks pass.

- [ ] **Step 6: Run GREEN behavior scenarios in fresh independent contexts**

Reuse Task 1 prompts verbatim with the changed skill path. Expected: bounded stable-contract changes select compact Q1-Q4; authorization-sensitive endpoint work selects strict mode. Record outputs and prompt/output word counts.

- [ ] **Step 7: Commit `$atu-ai` support**

```powershell
git add skills\atu-ai tests\validate_risk_adaptive.py tests\risk-adaptive-fast-path-evidence.md
git commit -m "feat: add compact atu-ai execution path"
```

- [ ] **Step 8: Update and reinstall the plugin**

Run the plugin-creator cachebuster helper, read the personal marketplace name, install `atu-workflow@personal`, and verify `codex plugin list` reports the new version. Do not edit Marketplace JSON.

---

### Task 3: Pin current planning behavior and compact specification expectations

**Files:**
- Modify: `tests/validate_risk_adaptive.py`
- Modify: `tests/risk-adaptive-fast-path-evidence.md`

**Interfaces:**
- Consumes: current `$atu-prd`, full `spec-contract.md`, and the compact artifact interface already supported by `$atu-ai`.
- Produces: failing compact-generation assertions plus pinned standard-spec invariants.

- [ ] **Step 1: Run independent RED planning scenarios**

Use read-only prompts for a local UI field/button change, a bounded backend behavior using stable contracts, a report field/layout change, an ambiguous requirement, a schema migration, and a payment callback. Expected: current `$atu-prd` expands bounded cases into the full standard set.

- [ ] **Step 2: Add failing PRD assertions**

Add:

```python
PRD = ROOT / "skills" / "atu-prd"
require((PRD / "references" / "quick-spec-contract.md").is_file(), "missing quick spec contract")
require((PRD / "references" / "standard-workflow.md").is_file(), "missing standard PRD workflow")
require("references/quick-spec-contract.md" in read(PRD / "SKILL.md"), "atu-prd lacks compact routing")
```

Pin standard invariants: exactly three authority documents for ready strict features, blocking-question gate, acyclic dependency graph, eight-task limit, stable IDs, traceability, and change-mode preservation.

- [ ] **Step 3: Run PRD validator and observe RED**

Run `python tests\validate_risk_adaptive.py --scope prd`.

Expected: FAIL with `missing quick spec contract`.

- [ ] **Step 4: Commit PRD RED evidence**

```powershell
git add tests\validate_risk_adaptive.py tests\risk-adaptive-fast-path-evidence.md
git commit -m "test: define compact prd contract"
```

---

### Task 4: Add compact generation to `$atu-prd`

**Files:**
- Modify: `skills/atu-prd/SKILL.md`
- Create: `skills/atu-prd/references/standard-workflow.md`
- Create: `skills/atu-prd/references/quick-spec-contract.md`
- Modify: `tests/validate_risk_adaptive.py`
- Modify: `tests/risk-adaptive-fast-path-evidence.md`

**Interfaces:**
- Consumes: compact artifact interface and evidence-based mode rules.
- Produces: automatic compact/strict classification and one-file compact specifications consumable by Task 2.

- [ ] **Step 1: Extract strict-only planning content**

Move the existing standard new/change workflow and required handoff into `references/standard-workflow.md`. Keep `spec-contract.md` unchanged and linked only from the strict path.

- [ ] **Step 2: Write the lean `$atu-prd` router**

Keep source authority, write-scope, no-business-code, no-assumption, and blocker boundaries. Route bounded evidence-supported requests to the compact contract; route any strict trigger or uncertainty to the standard workflow.

- [ ] **Step 3: Write `quick-spec-contract.md`**

Define generic eligibility, strict triggers, stable-contract consumption, the single-file path and collision rule, exact headings/statuses, `AC-Q01..AC-Q05`, exactly one `T-Q01`, no `PLAN.md`/`LESSONS.md`/numbered feature/ledger writes, promotion, and the copyable `$atu-ai <compact-path>` handoff.

- [ ] **Step 4: Complete deterministic PRD and integration assertions**

Assert the schema/status/ID tokens, maximum-five and exactly-one rules, no standard artifact writes in compact mode, strict-on-uncertainty, stable authenticated API consumption eligibility, resolved links, and:

```python
require(words(prd_main) + words(quick_spec) <= 1400, "atu-prd compact instruction budget exceeded")
require(ai_compact_words + prd_compact_words <= 3000, "combined compact budget exceeded")
```

- [ ] **Step 5: Run GREEN PRD and full validation**

Run:

```powershell
python tests\validate_risk_adaptive.py
python tests\validate_workflow.py
Get-ChildItem skills -Directory | ForEach-Object {
  python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
}
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .
```

Expected: all checks pass.

- [ ] **Step 6: Run GREEN planning scenarios**

Reuse Task 3 prompts verbatim. Expected: bounded cases emit one compact artifact with one task and at most five criteria; ambiguity blocks; schema/payment/public-security changes select strict mode. Record artifacts and metrics.

- [ ] **Step 7: Commit `$atu-prd` support**

```powershell
git add skills\atu-prd tests\validate_risk_adaptive.py tests\risk-adaptive-fast-path-evidence.md
git commit -m "feat: add compact atu-prd planning path"
```

- [ ] **Step 8: Update and reinstall the plugin**

Repeat the cachebuster/install/list verification. Confirm the installed version points to `C:\Users\17321\plugins\atu-workflow` and Marketplace remains `personal`.

---

### Task 5: Integrate, document, and audit completion

**Files:**
- Modify: `README.md`
- Modify: `tests/README.md`
- Modify: `tests/risk-adaptive-fast-path-evidence.md`
- Modify: `docs/superpowers/plans/2026-08-14-atu-workflow-risk-adaptive-fast-path.md`

**Interfaces:**
- Consumes: installed compact generator/executor and all design acceptance criteria.
- Produces: user-facing workflow documentation, final RED/GREEN evidence, and requirement-by-requirement audit.

- [x] **Step 1: Run end-to-end compact handoff evaluations**

Use a synthetic/read-only copy of the personal-report play/download request plus generic CRUD, report-layout, backend, schema-migration, payment, and ambiguity scenarios. Do not modify `D:\Workspace\x_insight_projcet`.

- [ ] **Step 2: Measure performance proxies**

Record mandatory loaded-document words, prompt/output words, tool calls, independent contexts, transitions, and artifacts for matched RED/GREEN cases. Require compact instructions at most 3,000 words, prompt/output at most 35% baseline, at most four transitions, one task, one artifact, and no default independent review/QA context.

Partial result: instruction words, observed artifact words, transitions, tasks, artifacts, hashes, and independent-context counts are recorded. Aggregate prompt/output tokens, tool-call counts, and live orchestration wall time require a newly created Codex task and remain `MANUAL REQUIRED`.

- [x] **Step 3: Update operator documentation**

Document automatic routing, compact eligibility, strict triggers, compact file location, copyable `$atu-prd` then `$atu-ai <quick-file>` usage, escalation, and the fact that users may force strict but cannot force compact past a strict trigger.

- [ ] **Step 4: Run the complete verification suite fresh**

Run all validators from Task 4, `git diff --check`, exact link/placeholder scans, `codex plugin list`, and a source-versus-installed-cache hash comparison for changed plugin files.

- [ ] **Step 5: Audit every design acceptance criterion**

Map each criterion in `docs/superpowers/specs/2026-08-14-atu-workflow-risk-adaptive-fast-path-design.md` to current files, behavior evidence, validator output, and installed-plugin state. Continue implementation if any evidence is missing or indirect.

- [ ] **Step 6: Commit final documentation and evidence**

```powershell
git add README.md tests docs\superpowers\plans\2026-08-14-atu-workflow-risk-adaptive-fast-path.md
git commit -m "docs: document adaptive atu workflow"
```

- [ ] **Step 7: Verify final repository state**

Require a clean Git worktree, no remotes, the expected commit sequence, all validators passing, and the new installed plugin version enabled. Report that a newly created Codex task is still the final real `$`-entry smoke boundary if the current task cannot reload the plugin.
