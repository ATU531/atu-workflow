# `$atu-quick` Forced Fast Path Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an explicit `$atu-quick` entry that writes or resumes one forced quick specification and immediately executes Q1-Q4 without category-based strict escalation.

**Architecture:** Keep the automatic `$atu-prd/$atu-ai` routers conservative and isolate the override in a new explicit-only Skill. Put discovery and input routing in a short `SKILL.md`, put the single-file schema and Q1-Q4 contract in one reference, and add only a forced-mode handoff guard to `$atu-ai`.

**Tech Stack:** Markdown Agent Skills, YAML UI metadata, Python contract validators, PowerShell, Git, Codex plugin CLI.

## Global Constraints

- Work only in `C:\Users\17321\plugins\atu-workflow`; do not edit the installed cache as source.
- `$atu-quick` is explicit-only; set `policy.allow_implicit_invocation: false`.
- One invocation creates or resumes the forced specification and proceeds directly through Q1-Q4 without a second approval gate.
- Authorization, payment, migration, public API, privacy, audit, external-service, production-configuration, cross-module, and cross-repository categories never cause automatic escalation.
- Use statuses `READY`, `IN_PROGRESS`, `DONE`, and `BLOCKED`; do not add an automatic `ESCALATED` route.
- Keep one authority file, one `T-Q01`, and one through five contiguous `AC-Q*` criteria.
- Workflow selection alone never authorizes commit, push, publish, deploy, real payment, production migration, deletion, or external write.
- `SKILL.md` plus `forced-quick-workflow.md` must contain no more than 1,100 whitespace-separated English words; target about 900.
- Load exactly one most-relevant ATU domain Skill during implementation.
- Do not change `$atu-prd`; modify `$atu-ai` only for forced-mode handoff.
- Preserve all pinned strict-workflow hashes in `tests/validate_risk_adaptive.py`.
- Use `apply_patch` for repository file edits. Do not configure a remote, push, or hand-edit Marketplace configuration.

---

## File map

- `skills/atu-quick/SKILL.md`: explicit entry, shared invariants, input selection, and reference routing.
- `skills/atu-quick/references/forced-quick-workflow.md`: exact specification schema, Q1-Q4, blocking, recovery, and reporting.
- `skills/atu-quick/agents/openai.yaml`: UI name, short description, prompt, and explicit-only policy.
- `tests/validate_forced_quick.py`: structural, semantic, budget, routing, and UI-metadata contract tests.
- `tests/forced-quick-evidence.md`: RED/GREEN prompts and compact raw behavior decisions.
- `skills/atu-ai/SKILL.md`: one forced-mode handoff guard.
- `tests/validate_workflow.py`: discover `atu-quick` and its required reference.
- `README.md`: fourth entry, usage, boundaries, and structure.
- `tests/README.md`: evidence link, metrics, and command.
- `.codex-plugin/plugin.json`: one `$atu-quick` default prompt and later cachebuster refresh.

### Task 1: Establish the RED contract and behavior baseline

**Files:**
- Create: `tests/validate_forced_quick.py`
- Create: `tests/forced-quick-evidence.md`
- Read: `skills/atu-prd/SKILL.md`
- Read: `skills/atu-ai/SKILL.md`

**Interfaces:**
- Consumes: approved design `docs/superpowers/specs/2026-08-14-atu-quick-forced-fast-path-design.md`.
- Produces: `python tests/validate_forced_quick.py --scope skill` with an intentional missing-Skill RED failure and a reusable `--scope all` integration gate.

- [ ] **Step 1: Write the failing validator**

Create a validator with this public shape and concrete contract checks:

```python
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
QUICK = ROOT / "skills" / "atu-quick"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def validate_skill() -> None:
    require(QUICK.is_dir(), "missing atu-quick skill")
    main_path = QUICK / "SKILL.md"
    flow_path = QUICK / "references" / "forced-quick-workflow.md"
    agent_path = QUICK / "agents" / "openai.yaml"
    for path in (main_path, flow_path, agent_path):
        require(path.is_file(), f"missing forced quick file: {path}")

    main = read(main_path)
    flow = read(flow_path)
    agent = read(agent_path)
    require("name: atu-quick" in main, "wrong atu-quick name")
    require("references/forced-quick-workflow.md" in main, "missing forced workflow route")
    require("Mode: forced-quick" in flow, "missing forced mode marker")
    require("explicit $atu-quick invocation" in flow, "missing explicit override marker")
    require("READY | IN_PROGRESS | DONE | BLOCKED" in flow, "wrong status contract")
    for stage in ("Q1", "Q2", "Q3", "Q4"):
        require(stage in flow, f"missing stage: {stage}")
    for trigger in ("authorization", "payment", "migration", "public API"):
        require(trigger.lower() in flow.lower(), f"missing bypass category: {trigger}")
    require("never cause automatic escalation" in flow, "category trigger can still escalate")
    require("BLOCKED" in flow and "missing decision" in flow.lower(), "missing decision gate")
    require("one `T-Q01`" in flow and "AC-Q05" in flow, "bounded task contract missing")
    require("575" in flow and "800 CJK" in flow, "specification budget missing")
    require(word_count(main) + word_count(flow) <= 1100, "forced quick instruction budget exceeded")
    require("allow_implicit_invocation: false" in agent, "atu-quick is not explicit-only")
    require("$atu-quick" in agent, "default prompt does not name atu-quick")


def validate_integration() -> None:
    ai = read(ROOT / "skills" / "atu-ai" / "SKILL.md")
    workflow = read(ROOT / "tests" / "validate_workflow.py")
    require("Mode: forced-quick" in ai and "$atu-quick" in ai, "atu-ai lacks forced handoff")
    require('"atu-quick"' in workflow, "workflow validator does not require atu-quick")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("skill", "integration", "all"), default="all")
    args = parser.parse_args()
    if args.scope in ("skill", "all"):
        validate_skill()
    if args.scope in ("integration", "all"):
        validate_integration()
    print(f"forced quick validation ok ({args.scope})")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the validator and observe RED**

Run:

```powershell
python tests\validate_forced_quick.py --scope skill
```

Expected: non-zero exit with `AssertionError: missing atu-quick skill`.

- [ ] **Step 3: Run five concise no-guidance control samples**

Use fresh read-only subagents. Give each only the current `atu-prd` and `atu-ai` files plus one synthetic request. Require output in no more than six lines: `MODE`, `ARTIFACTS`, `STAGES`, `RISK ROUTE`, `ACTION AUTHORITY`, `BLOCKER`.

Use these five requests:

```text
1. Explicitly demand one-shot fast implementation of a role-permission endpoint change.
2. Explicitly demand one-shot fast implementation of a payment callback contract change.
3. Explicitly demand one-shot fast implementation of a schema migration with backfill.
4. Explicitly demand one-shot fast implementation of a public API response change.
5. Explicitly demand a production migration but omit the retention rule and target authorization.
```

Expected baseline: cases 1-4 route to standard or refuse compact execution; case 5 also identifies missing decisions or action authority.

- [ ] **Step 4: Record RED evidence**

Create `tests/forced-quick-evidence.md` with the shared prompt, five requests, each raw six-line response, and this verdict table:

```markdown
| Scenario | Current route | Desired `$atu-quick` route | RED reason |
|---|---|---|---|
| Authorization | standard/refused | forced quick | no explicit forced entry |
| Payment | standard/refused | forced quick | category trigger cannot be overridden |
| Migration | standard/refused | forced quick | category trigger cannot be overridden |
| Public API | standard/refused | forced quick | category trigger cannot be overridden |
| Missing decision/authority | blocked | blocked | baseline guard retained |
```

Do not commit yet; Task 2 must turn the new contract GREEN in the same logical change.

### Task 2: Create and forward-test the explicit-only Skill

**Files:**
- Create: `skills/atu-quick/SKILL.md`
- Create: `skills/atu-quick/references/forced-quick-workflow.md`
- Create: `skills/atu-quick/agents/openai.yaml`
- Modify: `tests/forced-quick-evidence.md`
- Test: `tests/validate_forced_quick.py`

**Interfaces:**
- Consumes: the RED validator and five control scenarios from Task 1.
- Produces: an explicit-only `$atu-quick` contract that passes `--scope skill` and changes the same five scenarios to the approved behavior.

- [ ] **Step 1: Initialize the Skill with generated UI metadata**

Run from the plugin root:

```powershell
python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\init_skill.py atu-quick --path skills --resources references --interface 'display_name=ATU Quick' --interface 'short_description=Force one fast specification-to-implementation workflow' --interface 'default_prompt=Use $atu-quick to implement this request through the forced fast path.'
```

Expected: `skills/atu-quick/` contains `SKILL.md`, `references/`, and `agents/openai.yaml`.

- [ ] **Step 2: Replace the generated `SKILL.md` with the lean router**

Use this structure and binding language:

```markdown
---
name: atu-quick
description: Use when the user explicitly invokes $atu-quick or explicitly chooses a forced fast path for one coherent change, including authorization, payment, migration, public API, external-service, production-configuration, cross-module, or cross-repository work.
---

# ATU Quick

Execute the user's coherent outcome end-to-end with one forced quick specification. Explicit selection bypasses category-based strict routing; it does not waive truthful evidence or grant unnamed external actions.

## Invariants

- Resolve the authorized repository, requirement, or forced quick path and read effective project instructions.
- Preserve staged, unstaged, and untracked work.
- Stop only for a missing material decision, incoherent outcomes, unavailable required acceptance evidence, or an unauthorized requested action.
- Never infer commit, push, publish, deploy, real payment, production migration, deletion, or external-write authority from the entry name.
- Load exactly one most-relevant ATU domain Skill during implementation.

## Workflow

Read [Forced quick workflow](references/forced-quick-workflow.md) completely. Create or resume its single authority file and continue Q1-Q4 in this invocation without a second approval gate.
```

- [ ] **Step 3: Write the forced workflow reference**

Implement these exact sections in order:

```markdown
# Forced Quick Workflow
## Entry and authority
## Specification contract
## Q1: Establish contract and boundary
## Q2: Implement test-first
## Q3: Verify once
## Q4: Close truthfully
## Blocking and recovery
## Output
```

The reference must explicitly contain:

```text
Status: READY | IN_PROGRESS | DONE | BLOCKED
Mode: forced-quick
Override: explicit $atu-quick invocation
```

It must say that authorization, payment, migration, public API, privacy, audit, external-service, production-configuration, deployment-topology, cross-module, and cross-repository categories **never cause automatic escalation**. A newly discovered category is appended to the risk record and execution continues unless it reveals a missing decision or unnamed action authority, which becomes `BLOCKED`.

Include the exact one-file path, unique-name collision rule, required heading order from the design, contiguous `AC-Q01` through `AC-Q05`, exactly one `T-Q01`, the 575-word/800-CJK initial limit, dirty-work protection, test-first failure evidence, combined Q3 acceptance matrix, `NOT RUN`/`MANUAL REQUIRED`, and later-run recovery.

End with this output contract:

```text
COMPLETED
- List the implemented behavior and its current evidence.

BLOCKED
- Write `none`, or list the exact unfinished decision, evidence, or authorization.

NEXT STEP
- Write `none`, or list the smallest concrete action and owner.
```

- [ ] **Step 4: Make the Skill explicit-only**

Preserve the generated interface values and append:

```yaml
policy:
  allow_implicit_invocation: false
```

Verify all YAML strings remain quoted and the default prompt explicitly names `$atu-quick`.

- [ ] **Step 5: Run structural GREEN checks**

Run:

```powershell
python tests\validate_forced_quick.py --scope skill
python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\atu-quick
```

Expected: both exit zero. If the word budget fails, remove duplicated prose instead of raising 1,100.

- [ ] **Step 6: Run five concise with-guidance samples**

Run the Task 1 requests in fresh read-only subagents, now supplying `skills/atu-quick/SKILL.md` and its reference. Require the same six-line response shape.

Expected:

```text
Cases 1-4: Mode forced-quick; one specs/quick file; Q1-Q4; risk recorded; no automatic escalation.
Case 5: Mode forced-quick; BLOCKED for the exact missing retention decision and production action authority; no invented values and no external action.
```

- [ ] **Step 7: Update GREEN evidence and commit**

Append the five raw GREEN responses, compare them with controls, record the actual word counts, then run `git diff --check`.

Commit only Task 1-2 files:

```powershell
git add -- skills/atu-quick tests/validate_forced_quick.py tests/forced-quick-evidence.md
git commit -m "feat: add explicit atu-quick workflow"
```

### Task 3: Add the isolated handoff and regression gates

**Files:**
- Modify: `skills/atu-ai/SKILL.md`
- Modify: `tests/validate_workflow.py`
- Test: `tests/validate_forced_quick.py`
- Test: `tests/validate_risk_adaptive.py`

**Interfaces:**
- Consumes: `Mode: forced-quick` from Task 2.
- Produces: `$atu-ai` stops with the exact `$atu-quick specs/quick/YYYYMMDD-feature-name.md` handoff while all ordinary compact and standard contracts remain unchanged.

- [ ] **Step 1: Confirm the integration test is RED**

Run:

```powershell
python tests\validate_forced_quick.py --scope integration
```

Expected: non-zero exit because `$atu-ai` and `validate_workflow.py` do not yet recognize `atu-quick`.

- [ ] **Step 2: Add one `$atu-ai` routing guard**

Add this sentence before ordinary compact/standard mode selection:

```markdown
A specification with `Mode: forced-quick` belongs only to `$atu-quick`; report the exact `$atu-quick specs/quick/YYYYMMDD-feature-name.md` command for the selected file and stop without reclassifying, promoting, or executing it through `$atu-ai`.
```

Do not modify `quick-execution.md`, `standard-workflow.md`, or any N1-N8 reference.

- [ ] **Step 3: Require the new main Skill and reference**

In `tests/validate_workflow.py`:

```python
MAIN_SKILLS = {"atu-init", "atu-prd", "atu-ai", "atu-quick"}
QUICK_REFERENCES = {"forced-quick-workflow.md"}
```

Add:

```python
quick_reference_dir = ROOT / "skills" / "atu-quick" / "references"
require(
    QUICK_REFERENCES <= {path.name for path in quick_reference_dir.glob("*.md")},
    "missing atu-quick workflow reference",
)
```

- [ ] **Step 4: Run integration and strict regressions**

Run:

```powershell
python tests\validate_forced_quick.py --scope all
python tests\validate_workflow.py
python tests\validate_risk_adaptive.py --scope all
```

Expected: all exit zero; strict golden hashes remain unchanged.

- [ ] **Step 5: Commit the isolated integration**

```powershell
git add -- skills/atu-ai/SKILL.md tests/validate_workflow.py
git commit -m "feat: route forced specs to atu-quick"
```

### Task 4: Document the fourth entry and update plugin prompts

**Files:**
- Modify: `README.md`
- Modify: `tests/README.md`
- Modify: `.codex-plugin/plugin.json`
- Test: `tests/validate_workflow.py`
- Test: plugin manifest validator

**Interfaces:**
- Consumes: installed contract from Tasks 2-3.
- Produces: user-facing commands and plugin UI prompt for explicit `$atu-quick` selection.

- [ ] **Step 1: Update the main README**

Make these concrete changes:

- change `三个主入口` to `四个主入口`;
- add `$atu-quick` after `$atu-ai` with explicit-only, one-invocation, risk-bypass, and action-authority wording;
- add `$atu-quick D:\Workspace\example "修改支付回调并补齐迁移"` to the example block;
- add a short `强制快速入口` subsection contrasting automatic compact with forced quick;
- state forced statuses are `READY / IN_PROGRESS / DONE / BLOCKED` and never automatically `ESCALATED`;
- add `atu-quick/` to the structure tree; and
- add `python ...\tests\validate_forced_quick.py --scope all` to verification commands.

- [ ] **Step 2: Update test documentation**

Add the evidence link and record the measured forced-entry word count. Explain that the five RED controls route risk categories to standard, while five GREEN samples retain forced quick and keep missing-decision/action-authority blockers.

- [ ] **Step 3: Add the plugin default prompt**

Append this exact entry to `.codex-plugin/plugin.json` `interface.defaultPrompt`:

```json
"Force this coherent change through $atu-quick."
```

Do not change the cachebuster in this task.

- [ ] **Step 4: Validate documentation and manifest**

Run:

```powershell
python tests\validate_forced_quick.py --scope all
python tests\validate_workflow.py
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .
git diff --check
```

Expected: all validators exit zero and no whitespace error appears.

- [ ] **Step 5: Commit documentation and prompt**

```powershell
git add -- README.md tests/README.md .codex-plugin/plugin.json
git commit -m "docs: document explicit atu-quick entry"
```

### Task 5: Run the full gate, refresh the plugin, and audit the cache

**Files:**
- Modify: `.codex-plugin/plugin.json` through the cachebuster helper
- Verify: source tree and installed cache

**Interfaces:**
- Consumes: all committed Skill, test, router, documentation, and manifest changes.
- Produces: an enabled local plugin whose relevant source/cache files have matching SHA-256 values.

- [ ] **Step 1: Run the complete source validation suite**

Run:

```powershell
python tests\validate_forced_quick.py --scope all
python tests\validate_risk_adaptive.py --scope all
python tests\validate_workflow.py

Get-ChildItem skills -Directory | ForEach-Object {
  python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
  if ($LASTEXITCODE -ne 0) { throw "quick_validate failed: $($_.FullName)" }
}

python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .
git diff --check
```

Expected: every command exits zero, including all twelve Skills.

- [ ] **Step 2: Refresh the cachebuster with the supported helper**

Run:

```powershell
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\update_plugin_cachebuster.py C:\Users\17321\plugins\atu-workflow
```

Inspect `.codex-plugin/plugin.json` and verify the version keeps base `0.1.0` with exactly one `+codex.YYYYMMDDHHMMSS`-shaped suffix generated by the helper.

- [ ] **Step 3: Revalidate and commit the cachebuster**

```powershell
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py .
git add -- .codex-plugin/plugin.json
git commit -m "chore: refresh atu-workflow cachebuster"
```

- [ ] **Step 4: Resolve the personal Marketplace name and reinstall**

Run:

```powershell
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\read_marketplace_name.py
codex plugin add atu-workflow@personal
codex plugin list
```

Expected: Marketplace name is `personal`; `atu-workflow` is enabled at the new manifest version. Do not run `codex plugin marketplace add`.

- [ ] **Step 5: Compare relevant source and cache hashes**

Run:

```powershell
$sourceRoot = 'C:\Users\17321\plugins\atu-workflow'
$version = (Get-Content "$sourceRoot\.codex-plugin\plugin.json" -Raw | ConvertFrom-Json).version
$cacheRoot = "C:\Users\17321\.codex\plugins\cache\personal\atu-workflow\$version"
$relativeFiles = @(
  '.codex-plugin\plugin.json',
  'skills\atu-quick\SKILL.md',
  'skills\atu-quick\references\forced-quick-workflow.md',
  'skills\atu-quick\agents\openai.yaml',
  'skills\atu-ai\SKILL.md'
)

foreach ($relative in $relativeFiles) {
  $sourceHash = (Get-FileHash (Join-Path $sourceRoot $relative) -Algorithm SHA256).Hash
  $cacheHash = (Get-FileHash (Join-Path $cacheRoot $relative) -Algorithm SHA256).Hash
  if ($sourceHash -ne $cacheHash) { throw "cache hash mismatch: $relative" }
  "MATCH $relative $sourceHash"
}
```

Expected: five `MATCH` lines and no exception.

- [ ] **Step 6: Final repository audit**

Run:

```powershell
git status --short
git log -6 --oneline
```

Expected: clean worktree and scoped local commits only. Report that a fresh Codex task must perform the final manual `$atu-quick` discovery smoke because the current task cannot hot-reload the installed Skill.
