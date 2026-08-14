from pathlib import Path
import argparse
import hashlib
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


def require_exact_heading_order(text: str, tokens: tuple[str, ...], label: str) -> None:
    headings = [line.strip() for line in text.splitlines() if re.fullmatch(r"## .+", line.strip())]
    cursor = -1
    for token in tokens:
        try:
            position = headings.index(token, cursor + 1)
        except ValueError:
            position = -1
        require(position > cursor, f"{label} missing or out of order: {token}")
        cursor = position


def require_strict_triggers(path: Path) -> None:
    canonical = re.sub(r"[-_/]", " ", read(path).lower())
    required = (
        "authentication",
        "authorization",
        "privacy",
        "payment",
        "audit policy",
        "schema",
        "migration",
        "backfill",
        "retention or data lifecycle",
        "destructive",
        "public api",
        "compatibility",
        "external",
        "queue",
        "production configuration",
        "deployment topology",
        "cross repository",
    )
    for trigger in required:
        require(trigger in canonical, f"strict trigger missing from {path}: {trigger}")
    require(
        "independently deliverable" in canonical or "independent task" in canonical,
        f"strict independent-task trigger missing from {path}",
    )
    require(
        "broad shared state" in canonical or "material cross module" in canonical,
        f"strict shared-state trigger missing from {path}",
    )
    require(
        "verification cannot remain bounded and explicit" in canonical,
        f"strict unbounded-verification trigger missing from {path}",
    )
    require("uncertain" in canonical or "uncertainty" in canonical, f"strict uncertainty trigger missing from {path}")


STRICT_GOLDEN_SHA256 = {
    "skills/atu-ai/references/standard-workflow.md": "7ef91aacecf88bef73763c75f5060fc6a71f66e196c6afbf96871cac61cf1490",
    "skills/atu-ai/references/N1-init.md": "3001abf4ea020f3a6e17c43e0be60706b883649edd373ee8cc547b3b313fa8ea",
    "skills/atu-ai/references/N2-enter-feature.md": "972b1a686650c8764ca4c0b5707627d10788341b31ca1eef0752acab65836ae8",
    "skills/atu-ai/references/N3-execute-task.md": "eea42733e0c050f323ba8f21b0b1befb17441fd35a0ae21d3575f12772560715",
    "skills/atu-ai/references/N4-review.md": "77c34ed9c11408f40a3a6078409bf4f2698e11845dad30cb4dd997d2ff89dade",
    "skills/atu-ai/references/N5-mark-done.md": "66f5fee488afeeeaf8e165cfe09e7c9ed6e2eb0ccdc70857ac910e98e51dd935",
    "skills/atu-ai/references/N6-qa-eval.md": "5edbe0364930c384553420f9563887c026d465b11b1d88e61a6b19fff7658983",
    "skills/atu-ai/references/N7-context.md": "843c5bf46366c04c02b5753d7b346f1a3fa9076870b2417aa8c7fcbdde8f8361",
    "skills/atu-ai/references/N8-finish.md": "5620665b3aa64860c185acac10b6ab174bb23aa02354fd75b8215c5f947009f2",
    "skills/atu-prd/references/spec-contract.md": "654a8c163b8964d987b66fcd7003c2ff35a408396c27060cd614fcf42a635c8c",
    "skills/atu-prd/references/standard-workflow.md": "8d9c43b74935e70894896fa8aba62bf4307ef498d9e5634f59408178205ede95",
}


def validate_strict_golden() -> None:
    for relative, expected in STRICT_GOLDEN_SHA256.items():
        normalized = read(ROOT / relative).replace("\r\n", "\n")
        actual = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        require(actual == expected, f"strict workflow golden changed: {relative}")


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
    require("Only `READY` or `IN_PROGRESS` enters Q1-Q4" in main, "atu-ai router lacks executable status routing")
    for status_route in ("READY or IN_PROGRESS", "BLOCKED", "ESCALATED", "DONE"):
        require(status_route in quick, f"quick execution lacks status route: {status_route}")
    require("uncertain" in main.lower(), "atu-ai router lacks strict-on-uncertainty rule")
    for path in (main_path, quick_path):
        require_strict_triggers(path)
    require("one active task" in quick.lower(), "quick execution does not enforce one task")
    require("do not create" in quick.lower() and "verification.md" in quick, "quick execution does not prohibit a separate ledger")
    require("dual" in quick.lower() and "hash" in quick.lower(), "quick execution does not prohibit dual hashes")
    require("staged, unstaged, and untracked" in quick, "quick execution lacks dirty-work inventory")
    require("resetting, cleaning, stashing, overwriting" in quick, "quick execution lacks dirty-work protection")
    require(word_count(main) + word_count(quick) <= 1600, "atu-ai compact instruction budget exceeded")
    require_local_links(main_path)


def validate_prd() -> None:
    prd = ROOT / "skills" / "atu-prd"
    main_path = prd / "SKILL.md"
    main = read(main_path)
    quick_path = prd / "references" / "quick-spec-contract.md"
    standard_path = prd / "references" / "standard-workflow.md"

    require(quick_path.is_file(), "missing quick spec contract")
    require(standard_path.is_file(), "missing PRD standard workflow")
    quick = read(quick_path)
    strict = read(standard_path) + read(prd / "references" / "spec-contract.md")

    strict_invariants = {
        "plan authority": "PLAN.md",
        "lessons ledger": "LESSONS.md",
        "requirements authority": "requirements.md",
        "design authority": "design.md",
        "tasks authority": "tasks.md",
        "blocking question gate": "blocking-question gate",
        "standard task limit": "eight",
        "acyclic dependency graph": "directed acyclic graph",
        "permanent IDs": "IDs are permanent",
        "traceability matrix": "traceability matrix",
        "completed-task preservation": "byte-for-byte preserved",
    }
    strict_lower = strict.lower()
    for label, token in strict_invariants.items():
        require(token.lower() in strict_lower, f"strict atu-prd invariant missing: {label}")

    require("references/quick-spec-contract.md" in main, "atu-prd does not route compact requests")
    require("references/standard-workflow.md" in main, "atu-prd does not route strict requests")
    require("specs/quick/" in quick, "quick PRD path is not defined")
    for status in ("READY", "IN_PROGRESS", "DONE", "ESCALATED", "BLOCKED"):
        require(status in quick, f"quick PRD contract lacks status {status}")
    require("AC-Q01" in quick and "AC-Q05" in quick, "quick PRD acceptance limit is not explicit")
    require("exactly one" in quick.lower() and "T-Q01" in quick, "quick PRD does not enforce one task")
    require("do not create" in quick.lower() and "PLAN.md" in quick, "quick PRD does not prohibit standard artifacts")
    require("575" in quick and "800 CJK" in quick, "quick PRD output budget is not explicit")
    require("uncertain" in main.lower(), "atu-prd router lacks strict-on-uncertainty rule")
    for path in (main_path, quick_path):
        require_strict_triggers(path)
    require("existing authenticated" in main.lower(), "atu-prd router does not protect stable authenticated API consumption")
    require(word_count(main) + word_count(quick) <= 1400, "atu-prd compact instruction budget exceeded")
    require_local_links(main_path)
    require_local_links(quick_path)
    require_local_links(standard_path)

    compact_headings = (
        "## Goal",
        "## Scope",
        "## Reused contracts and evidence",
        "## Compact eligibility and escalation triggers",
        "## Bounded design",
        "## Acceptance criteria",
        "## Task",
        "## Execution evidence",
        "## Open questions",
        "## Handoff",
    )
    require_exact_heading_order(quick, compact_headings, "quick PRD schema")
    design = read(ROOT / "docs" / "superpowers" / "specs" / "2026-08-14-atu-workflow-risk-adaptive-fast-path-design.md")
    require_exact_heading_order(design, compact_headings, "design compact schema")

    fixture_path = ROOT / "tests" / "fixtures" / "personal-report-video-actions-compact.md"
    require(fixture_path.is_file(), "missing matched compact artifact fixture")
    fixture = read(fixture_path)
    require_exact_heading_order(fixture, compact_headings, "matched compact artifact schema")
    require(word_count(fixture) <= 575, "matched compact artifact output budget exceeded")
    require(len(re.findall(r"^- \[[ x]\] AC-Q\d{2}:", fixture, re.MULTILINE)) in range(1, 6), "matched compact artifact AC count invalid")
    require(len(re.findall(r"^- \[[ x]\] T-Q01:", fixture, re.MULTILINE)) == 1, "matched compact artifact task count invalid")

    ai_main = read(ROOT / "skills" / "atu-ai" / "SKILL.md")
    ai_quick = read(ROOT / "skills" / "atu-ai" / "references" / "quick-execution.md")
    require(
        word_count(main) + word_count(quick) + word_count(ai_main) + word_count(ai_quick) <= 3000,
        "combined compact instruction budget exceeded",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("ai", "prd", "all"), default="all")
    args = parser.parse_args()

    validate_strict_golden()
    if args.scope in ("ai", "all"):
        validate_ai()
    if args.scope in ("prd", "all"):
        validate_prd()

    print(f"risk-adaptive workflow validation ok ({args.scope})")


if __name__ == "__main__":
    main()
