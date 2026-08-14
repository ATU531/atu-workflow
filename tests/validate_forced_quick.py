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
