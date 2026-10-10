from pathlib import Path
import re
import sys

from validate_reference_packaging import live_sources, validate_bundle


ROOT = Path(__file__).resolve().parents[1]
MAIN_SKILLS = {"atu-init", "atu-prd", "atu-ai", "atu-quick"}
SUPPORT_SKILLS = {
    "atu-android-engineer",
    "atu-code-reviewer",
    "atu-miniprogram-engineer",
}
STANDARD_STAGES = {
    "S1-boundary.md",
    "S2-implement.md",
    "S3-verify.md",
    "S4-close.md",
}
AI_REFERENCES = STANDARD_STAGES | {"quick-execution.md", "standard-workflow.md"}
PRD_REFERENCES = {"quick-spec-contract.md", "spec-contract.md", "standard-workflow.md"}
QUICK_REFERENCES = {"forced-quick-workflow.md"}
CHECKLISTS = {
    "android-checklist.md",
    "miniprogram-checklist.md",
    "quality-checklist.md",
    "security-checklist.md",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


skill_dirs = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
require(MAIN_SKILLS | SUPPORT_SKILLS <= skill_dirs, "missing required skill directory")

for skill_name in MAIN_SKILLS | SUPPORT_SKILLS:
    text = (ROOT / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"{skill_name}: missing YAML frontmatter")
    require(f"name: {skill_name}" in text, f"{skill_name}: wrong frontmatter name")
    require("description:" in text, f"{skill_name}: missing description")
    require("[TODO:" not in text, f"{skill_name}: unresolved TODO placeholder")

node_dir = ROOT / "skills" / "atu-ai" / "references"
require(
    AI_REFERENCES <= {path.name for path in node_dir.glob("*.md")},
    "missing atu-ai workflow reference",
)
require(not list(node_dir.glob("N*.md")), "legacy atu-ai node reference remains")

prd_reference_dir = ROOT / "skills" / "atu-prd" / "references"
require(
    PRD_REFERENCES <= {path.name for path in prd_reference_dir.glob("*.md")},
    "missing atu-prd workflow reference",
)

quick_reference_dir = ROOT / "skills" / "atu-quick" / "references"
require(
    QUICK_REFERENCES <= {path.name for path in quick_reference_dir.glob("*.md")},
    "missing atu-quick workflow reference",
)

checklist_dir = ROOT / "skills" / "atu-code-reviewer" / "references"
require(
    CHECKLISTS <= {path.name for path in checklist_dir.glob("*.md")},
    "missing review checklist",
)

all_text = "\n".join(path.read_text(encoding="utf-8") for path in live_sources(ROOT))
for forbidden in (r"Agent\s*\(", r"Skill\s*\(", r"codex:codex-rescue"):
    require(not re.search(forbidden, all_text), f"Claude-only call remains: {forbidden}")

for main in MAIN_SKILLS:
    require(f"${main}" in all_text, f"missing Codex invocation ${main}")

packaging_errors = validate_bundle(ROOT)
require(not packaging_errors, "\n".join(packaging_errors))

print("atu-workflow contract ok")
sys.exit(0)
