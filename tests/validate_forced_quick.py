from pathlib import Path
import argparse
import re


ROOT = Path(__file__).resolve().parents[1]
QUICK = ROOT / "skills" / "atu-quick"
FORCED_FIXTURE = ROOT / "tests" / "fixtures" / "editor-grant-viewer-forced.md"
FORCED_HEADINGS = (
    "## Goal",
    "## Scope",
    "## Risk override and action authorization",
    "## Reused contracts and evidence",
    "## Bounded design",
    "## Acceptance criteria",
    "## Task",
    "## Execution evidence",
    "## Open questions",
    "## Handoff",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def validate_forced_spec(text: str) -> None:
    require(re.search(r"(?m)^# \S", text) is not None, "forced spec lacks title")
    metadata = {
        "status": r"(?m)^- Status: (READY|IN_PROGRESS|DONE|BLOCKED)$",
        "mode": r"(?m)^- Mode: forced-quick$",
        "override": r"(?m)^- Override: explicit \$atu-quick invocation$",
        "date": r"(?m)^- Date: \d{4}-\d{2}-\d{2}$",
        "source": r"(?m)^- Source: \S.+$",
    }
    for label, pattern in metadata.items():
        require(re.search(pattern, text) is not None, f"forced spec lacks {label}")

    headings = tuple(
        line.strip() for line in text.splitlines() if re.fullmatch(r"## .+", line.strip())
    )
    require(headings == FORCED_HEADINGS, "forced spec section order is invalid")

    criteria = [
        int(value)
        for value in re.findall(r"(?m)^- (?:\[[ x]\] )?AC-Q(\d{2}):", text)
    ]
    require(1 <= len(criteria) <= 5, "forced spec acceptance count is invalid")
    require(criteria == list(range(1, len(criteria) + 1)), "forced spec acceptance IDs are not contiguous")

    tasks = re.findall(r"(?m)^- \[([ x])\] T-Q(\d{2}):", text)
    require(len(tasks) == 1 and tasks[0][1] == "01", "forced spec task contract is invalid")
    status = re.search(metadata["status"], text).group(1)
    require(status != "DONE" or tasks[0][0] == "x", "DONE forced spec task is unchecked")
    require(status == "DONE" or tasks[0][0] == " ", "open forced spec task is checked")


def require_fixture_examples() -> None:
    require(FORCED_FIXTURE.is_file(), "missing completed forced spec fixture")
    valid = read(FORCED_FIXTURE)
    validate_forced_spec(valid)

    invalid_examples = {
        "missing section": valid.replace("## Scope", "## Removed scope", 1),
        "noncontiguous acceptance": valid.replace("AC-Q02:", "AC-Q05:", 1),
        "multiple tasks": valid.replace(
            "## Execution evidence",
            "- [ ] T-Q02: Extra task.\n\n## Execution evidence",
            1,
        ),
    }
    for label, candidate in invalid_examples.items():
        try:
            validate_forced_spec(candidate)
        except AssertionError:
            continue
        raise AssertionError(f"forced spec negative fixture accepted: {label}")


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
    require(
        "references/forced-quick-workflow.md" in main,
        "missing forced workflow route",
    )
    require("Mode: forced-quick" in flow, "missing forced mode marker")
    require(
        "explicit $atu-quick invocation" in flow,
        "missing explicit override marker",
    )
    require(
        "READY | IN_PROGRESS | DONE | BLOCKED" in flow,
        "wrong status contract",
    )
    for stage in ("Q1", "Q2", "Q3", "Q4"):
        require(stage in flow, f"missing stage: {stage}")
    for trigger in ("authorization", "payment", "migration", "public API"):
        require(
            trigger.lower() in flow.lower(),
            f"missing bypass category: {trigger}",
        )
    require(
        "never cause automatic escalation" in flow,
        "category trigger can still escalate",
    )
    require(
        "BLOCKED" in flow and "missing decision" in flow.lower(),
        "missing decision gate",
    )
    require(
        "one `T-Q01`" in flow and "AC-Q05" in flow,
        "bounded task contract missing",
    )
    resume_contract = {
        "path": "path under `specs/quick/`",
        "metadata": "required metadata",
        "section order": "exact section order",
        "acceptance continuity": "one to five contiguous `AC-Q*`",
        "task count": "exactly one `T-Q01`",
        "initial size": "initial size limit",
        "pre-Q2 block": "set `BLOCKED` before Q2",
    }
    for label, token in resume_contract.items():
        require(token in flow, f"named spec resume lacks {label} validation")
    require("575" in flow and "800 CJK" in flow, "specification budget missing")
    require(
        word_count(main) + word_count(flow) <= 1100,
        "forced quick instruction budget exceeded",
    )
    require(
        "allow_implicit_invocation: false" in agent,
        "atu-quick is not explicit-only",
    )
    require("$atu-quick" in agent, "default prompt does not name atu-quick")
    require_fixture_examples()


def validate_integration() -> None:
    ai = read(ROOT / "skills" / "atu-ai" / "SKILL.md")
    workflow = read(ROOT / "tests" / "validate_workflow.py")
    require(
        "Mode: forced-quick" in ai and "$atu-quick" in ai,
        "atu-ai lacks forced handoff",
    )
    require('"atu-quick"' in workflow, "workflow validator does not require atu-quick")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scope",
        choices=("skill", "integration", "all"),
        default="all",
    )
    args = parser.parse_args()
    if args.scope in ("skill", "all"):
        validate_skill()
    if args.scope in ("integration", "all"):
        validate_integration()
    print(f"forced quick validation ok ({args.scope})")


if __name__ == "__main__":
    main()
