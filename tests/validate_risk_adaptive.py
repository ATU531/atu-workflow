from pathlib import Path
import argparse
import re


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def require_local_links(source: Path) -> None:
    text = read(source)
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        local_target = target.split("#", 1)[0]
        require((source.parent / local_target).is_file(), f"broken link in {source}: {target}")


def validate_ai() -> None:
    ai = ROOT / "skills" / "atu-ai"
    main_path = ai / "SKILL.md"
    main = read(main_path)
    node_text = "\n".join(
        read(path) for path in sorted((ai / "references").glob("N*.md"))
    )
    standard_path = ai / "references" / "standard-workflow.md"
    strict_text = (read(standard_path) if standard_path.is_file() else main) + node_text

    strict_invariants = {
        "deterministic spec identity": "spec_contract",
        "durable ledger": "verification.md",
        "review gate": "N4",
        "QA gate": "N6",
        "context recovery": "N7",
        "independent specification review": "independent specification review",
        "independent quality review": "independent quality review",
        "checked-task recovery": "reopen",
    }
    strict_lower = strict_text.lower()
    for label, token in strict_invariants.items():
        require(token.lower() in strict_lower, f"strict atu-ai invariant missing: {label}")

    quick_path = ai / "references" / "quick-execution.md"
    require(quick_path.is_file(), "missing quick execution")
    require(standard_path.is_file(), "missing standard workflow")
    quick = read(quick_path)

    require("references/quick-execution.md" in main, "atu-ai does not route compact specs")
    require("references/standard-workflow.md" in main, "atu-ai does not route strict specs")
    for stage in ("Q1", "Q2", "Q3", "Q4"):
        require(stage in quick, f"quick execution lacks {stage}")
    for status in ("READY", "IN_PROGRESS", "DONE", "ESCALATED", "BLOCKED"):
        require(status in quick, f"quick execution lacks status {status}")
    require("uncertain" in main.lower(), "atu-ai router lacks strict-on-uncertainty rule")
    require("one active task" in quick.lower(), "quick execution does not enforce one task")
    require("do not create" in quick.lower() and "verification.md" in quick, "quick execution does not prohibit a separate ledger")
    require("dual" in quick.lower() and "hash" in quick.lower(), "quick execution does not prohibit dual hashes")
    require(word_count(main) + word_count(quick) <= 1600, "atu-ai compact instruction budget exceeded")
    require_local_links(main_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("ai", "prd", "all"), default="all")
    args = parser.parse_args()

    if args.scope in ("ai", "all"):
        validate_ai()
    if args.scope == "prd":
        raise AssertionError("PRD adaptive validation is not implemented yet")

    print(f"risk-adaptive workflow validation ok ({args.scope})")


if __name__ == "__main__":
    main()
