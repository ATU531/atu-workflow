"""Exercise bundle failures without editing release fixtures or the real plugin."""

from pathlib import Path
import json
import tempfile
import unittest

from validate_reference_packaging import (
    MAIN_SKILLS,
    SUPPORT_SKILLS,
    REQUIRED_REFERENCES,
    validate_bundle,
)


class ReferencePackagingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="atu-reference-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in MAIN_SKILLS | SUPPORT_SKILLS:
            self.write(f"skills/{name}/SKILL.md", f"---\nname: {name}\ndescription: Test fixture\n---\n# {name}\n")
        self.write(".codex-plugin/plugin.json", json.dumps({"skills": "./skills/"}))
        routes = []
        for relative in sorted(REQUIRED_REFERENCES):
            self.write(relative, "# Reference\nTask-specific project guidance.\n")
            routes.append(f"[Guide]({Path(relative).relative_to('skills/atu-ai').as_posix()})")
        self.ai = self.root / "skills/atu-ai/SKILL.md"
        self.ai.write_text(self.ai.read_text(encoding="utf-8") + "\n".join(routes), encoding="utf-8")

    def write(self, relative: str, text: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def assert_rejected(self, token: str) -> None:
        errors = validate_bundle(self.root)
        self.assertTrue(any(token in error for error in errors), errors)

    def test_complete_bundle_is_valid(self) -> None:
        self.assertEqual(validate_bundle(self.root), [])

    def test_deleted_skill_invocation_in_live_metadata_is_rejected(self) -> None:
        self.write("skills/atu-ai/agents/openai.yaml", 'interface:\n  default_prompt: "Use $atu-workflow:atu-qa-engineer"\n')
        self.assert_rejected("unavailable skill invocation")

    def test_unknown_skill_invocation_in_live_docs_is_rejected(self) -> None:
        self.write("docs/usage.md", "Use $atu-backned-engineer to implement the API.\n")
        self.assert_rejected("unavailable skill invocation")

    def test_missing_reference_is_rejected(self) -> None:
        (self.root / "skills/atu-ai/references/domains/database.md").unlink()
        self.assert_rejected("missing migrated reference")

    def test_orphan_reference_is_rejected(self) -> None:
        self.ai.write_text(self.ai.read_text(encoding="utf-8").replace("[Guide](references/documentation.md)", ""), encoding="utf-8")
        self.assert_rejected("no skill route")

    def test_transitive_reference_route_is_valid(self) -> None:
        self.ai.write_text(self.ai.read_text(encoding="utf-8").replace("[Guide](references/documentation.md)", "[Stages](references/S4.md)"), encoding="utf-8")
        self.write("skills/atu-ai/references/S4.md", "[Documentation](documentation.md)\n")
        self.assertEqual(validate_bundle(self.root), [])

    def test_broken_cross_skill_link_is_rejected(self) -> None:
        self.write("skills/atu-quick/references/flow.md", "[Backend](../../atu-ai/references/domains/missing.md)\n")
        self.assert_rejected("broken local reference")

    def test_unpackaged_relative_link_is_rejected(self) -> None:
        self.write("README.md", "[Local secret](../outside.md)\n")
        self.assert_rejected("unpackaged local reference")

    def test_absolute_local_link_is_not_mistaken_for_url(self) -> None:
        outside = (self.root.parent / "atu-outside-test.md").as_posix()
        self.write("README.md", f"[Unpackaged file]({outside})\n")
        self.assert_rejected("unpackaged local reference")

    def test_manifest_cannot_exclude_shared_references(self) -> None:
        self.write(".codex-plugin/plugin.json", json.dumps({"skills": "./skills/atu-quick"}))
        self.assert_rejected("manifest must package")

    def test_reference_cannot_become_discoverable_skill(self) -> None:
        self.write("skills/atu-ai/references/domains/backend/SKILL.md", "# Accidental skill\n")
        self.assert_rejected("skill entrypoints differ")

    def test_renamed_skill_body_cannot_keep_frontmatter(self) -> None:
        self.write("skills/atu-ai/references/verification.md", "---\nname: atu-qa-engineer\ndescription: Review tests\n---\n# Verification\n")
        self.assert_rejected("reference retains skill discovery frontmatter")

    def test_retired_directory_cannot_remain_in_package(self) -> None:
        self.write("skills/atu-doc-syncer/README.md", "Unused old resource\n")
        self.assert_rejected("retired skill directory remains")

    def test_empty_retired_directory_is_not_valid_plugin_schema(self) -> None:
        (self.root / "skills/atu-doc-syncer").mkdir()
        self.assert_rejected("retired skill directory remains")

    def test_live_code_formatted_retired_path_is_rejected(self) -> None:
        self.write("README.md", "Read `skills/atu-frontend-engineer/SKILL.md`.\n")
        self.assert_rejected("retired skill path")

    def test_historical_evidence_does_not_define_live_routes(self) -> None:
        old = "Use $atu-qa-engineer; [old](../../../skills/atu-qa-engineer/SKILL.md).\n"
        for relative in ("docs/superpowers/specs/old.md", "docs/superpowers/plans/old.md", "tests/fixtures/old.md", "tests/behavior-evidence.md"):
            self.write(relative, old)
        self.assertEqual(validate_bundle(self.root), [])

    def test_external_links_and_local_anchors_are_valid(self) -> None:
        self.write("README.md", "[Web](https://example.invalid/guide) [Anchor](#heading)\n")
        self.assertEqual(validate_bundle(self.root), [])


if __name__ == "__main__":
    unittest.main()
