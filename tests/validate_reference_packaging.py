"""Check the installed skill surface and live, package-local reference graph."""

from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MAIN_SKILLS = {"atu-init", "atu-architect", "atu-prd", "atu-ai", "atu-quick"}
SUPPORT_SKILLS = {
    "atu-android-engineer",
    "atu-miniprogram-engineer",
    "atu-code-reviewer",
}
RETIRED_SKILLS = {
    "atu-frontend-engineer",
    "atu-backend-engineer",
    "atu-database-engineer",
    "atu-qa-engineer",
    "atu-doc-syncer",
}
REQUIRED_REFERENCES = {
    "skills/atu-architect/references/architecture-contract.md",
    "skills/atu-architect/references/design-guide.md",
    "skills/atu-ai/references/domains/frontend.md",
    "skills/atu-ai/references/domains/backend.md",
    "skills/atu-ai/references/domains/database.md",
    "skills/atu-ai/references/verification.md",
    "skills/atu-ai/references/documentation.md",
}


def live_sources(root: Path) -> list[Path]:
    """Historical designs, plans, fixtures and replay evidence are not instructions."""
    paths = {
        path
        for path in (root / "skills").rglob("*")
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml", ".json"}
    }
    for relative in ("README.md", "AGENTS.md", "tests/README.md", ".codex-plugin/plugin.json"):
        path = root / relative
        if path.is_file():
            paths.add(path)
    for path in (root / "docs").rglob("*.md"):
        parts = path.relative_to(root / "docs").parts
        if parts[:2] in {("superpowers", "specs"), ("superpowers", "plans")}:
            continue
        if parts and parts[0] in {"archive", "archives", "historical", "obsoleted"}:
            continue
        paths.add(path)
    return sorted(paths)


def markdown_targets(text: str) -> list[str]:
    # Skill references use inline Markdown links or link-reference definitions.
    targets = re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text)
    targets += re.findall(r"(?m)^\[[^\]\n]+\]:\s*(\S+)", text)
    return [target.strip().split(' "', 1)[0].strip("<>") for target in targets]


def validate_bundle(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    expected = {f"skills/{name}/SKILL.md" for name in MAIN_SKILLS | SUPPORT_SKILLS}
    discovered = {path.relative_to(root).as_posix() for path in (root / "skills").rglob("SKILL.md")}
    if discovered != expected:
        errors.append(f"skill entrypoints differ: missing={sorted(expected-discovered)}, unexpected={sorted(discovered-expected)}")
    for name in sorted(RETIRED_SKILLS):
        if (root / "skills" / name).exists():
            errors.append(f"retired skill directory remains: {name}")

    manifest_path = root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        package_root = manifest.get("skills")
        if not isinstance(package_root, str) or (root / package_root).resolve() != root / "skills":
            errors.append("plugin manifest must package the complete skills directory")
    except (OSError, ValueError) as exc:
        errors.append(f"invalid plugin manifest: {exc}")

    for relative in sorted(REQUIRED_REFERENCES):
        path = root / relative
        if not path.is_file():
            errors.append(f"missing migrated reference: {relative}")
            continue
        text = path.read_text(encoding="utf-8-sig")
        if not text.strip():
            errors.append(f"empty migrated reference: {relative}")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if frontmatter and all(re.search(rf"(?m)^{key}:\s*\S", frontmatter.group(1)) for key in ("name", "description")):
            errors.append(f"reference retains skill discovery frontmatter: {relative}")

    graph: dict[Path, set[Path]] = {}
    for source in live_sources(root):
        text = source.read_text(encoding="utf-8-sig")
        label = source.relative_to(root).as_posix()
        for invoked in re.findall(r"\$(?:atu-workflow:)?(atu-[a-z0-9]+(?:-[a-z0-9]+)*)", text):
            if invoked not in MAIN_SKILLS | SUPPORT_SKILLS:
                errors.append(f"unavailable skill invocation in {label}: ${invoked}")
        for retired in sorted(RETIRED_SKILLS):
            # Catch code-formatted paths as well as ordinary Markdown links.
            if re.search(rf"(?:skills[/\\]|\.\.[/\\]){re.escape(retired)}(?:[/\\]|(?=[`\s)]))", text):
                errors.append(f"retired skill path in {label}: {retired}")
        if source.suffix != ".md":
            continue
        graph[source.resolve()] = set()
        for target in markdown_targets(text):
            windows_path = re.match(r"^[A-Za-z]:[/\\]", target)
            if (urlsplit(target).scheme and not windows_path) or target.startswith("//"):
                continue
            local = unquote(target.split("#", 1)[0])
            if not local:
                continue
            resolved = (source.parent / local).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"unpackaged local reference in {label}: {target}")
            elif not resolved.exists():
                errors.append(f"broken local reference in {label}: {target}")
            else:
                graph[source.resolve()].add(resolved)

    reachable = {(root / relative).resolve() for relative in expected}
    pending = list(reachable)
    while pending:
        for target in graph.get(pending.pop(), set()):
            if target not in reachable:
                reachable.add(target)
                pending.append(target)
    for relative in sorted(REQUIRED_REFERENCES):
        if (root / relative).is_file() and (root / relative).resolve() not in reachable:
            errors.append(f"migrated reference has no skill route: {relative}")
    return errors


def main() -> None:
    errors = validate_bundle(ROOT)
    if errors:
        raise AssertionError("\n".join(errors))
    print(f"skill/reference packaging validation ok ({len(MAIN_SKILLS | SUPPORT_SKILLS)} skills, {len(REQUIRED_REFERENCES)} required references)")


if __name__ == "__main__":
    main()
