from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
AI = ROOT / "skills" / "atu-ai"
REFERENCES = AI / "references"
STAGES = {
    "S1-boundary.md",
    "S2-implement.md",
    "S3-verify.md",
    "S4-close.md",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def validate_reference_shape() -> str:
    names = {path.name for path in REFERENCES.glob("*.md")}
    require(STAGES <= names, "missing S1-S4 standard stage reference")
    require(not list(REFERENCES.glob("N*.md")), "legacy N1-N8 references remain")
    return "\n".join(read(REFERENCES / name) for name in sorted(STAGES))


def validate_four_stage_contract(stage_text: str) -> None:
    standard = read(REFERENCES / "standard-workflow.md")
    positions = [standard.find(f"S{number}") for number in range(1, 5)]
    require(all(position >= 0 for position in positions), "standard workflow lacks S1-S4")
    require(positions == sorted(positions), "S1-S4 are not ordered")
    for name in STAGES:
        require(name in standard, f"standard workflow does not link {name}")

    current = read(AI / "SKILL.md") + standard + stage_text
    require(word_count(current) <= 3000, "simplified standard instruction budget exceeded")
    for obsolete in ("spec_contract", "dual-identity", "atomically reopen"):
        require(obsolete not in current, f"obsolete audit mechanism remains: {obsolete}")


def validate_risk_proportion(stage_text: str) -> None:
    lower = stage_text.lower()
    critical = (
        "authentication or authorization",
        "payment",
        "destructive or irreversible",
        "public api",
        "production change",
    )
    for token in critical:
        require(token in lower, f"critical review trigger missing: {token}")
    require("once per feature" in lower, "independent review is not feature-scoped")
    require("independent qa" in lower and "only" in lower, "independent QA is not conditional")
    require("verification.md" in lower and "when" in lower, "evidence ledger is not optional")


def validate_safety(stage_text: str) -> None:
    lower = stage_text.lower()
    for token in (
        "pre-existing",
        "test-first",
        "not run",
        "manual required",
        "blocked",
        "explicit authorization",
        "do not push",
    ):
        require(token in lower, f"essential safety boundary missing: {token}")


def validate_readme() -> None:
    readme = read(ROOT / "README.md")
    require("S1" in readme and "S4" in readme, "README lacks simplified standard stages")
    require("原 N1 至 N8" not in readme, "README still advertises legacy audit")


def main() -> None:
    stages = validate_reference_shape()
    validate_four_stage_contract(stages)
    validate_risk_proportion(stages)
    validate_safety(stages)
    validate_readme()
    print("simplified standard audit validation ok")


if __name__ == "__main__":
    main()
