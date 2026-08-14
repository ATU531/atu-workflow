---
name: atu-init
description: Use when the user invokes $atu-init, asks to create or rebuild repository-level AGENTS.md, wants to initialize or refresh repository-level AI development conventions such as coding, testing, security, or Git guidance, explicitly requests Claude-compatible initialization, or wants verified startup, test, build, and deploy commands captured during AI-guidance initialization.
---

# ATU Init

Initialize project guidance from repository evidence. Treat `AGENTS.md` in the approved write scope as the authoritative Codex entry point while keeping any existing or explicitly requested Claude compatibility files consistent.

Before writing, read [the initialization contract](references/initialization-contract.md) completely.

## Workflow

1. **Locate the repository root and write scope separately.**
   - With an explicit user path, start discovery there and treat it as the requested write scope. Without one, start discovery from the current working directory and default the write scope to the discovered repository root.
   - Prefer the Git root; otherwise use the nearest parent with strong project markers, including `AGENTS.md`, a dependency manifest, a root README, or `.claude/`.
   - Read applicable instructions from the repository root down to the write scope, including governing `AGENTS.md` files.
   - Never write above or outside the requested scope unless the user explicitly widens it. Reading above the scope is allowed only for root discovery and applicable instructions.

2. **Inspect before changing anything.**
   - Read applicable `AGENTS.md` files, README files, dependency/build/test/lint configuration, lockfiles, CI configuration, and the relevant source-directory outline.
   - Inventory `.claude/CLAUDE.md` and `.claude/rules/` recursively when present.
   - Obey applicable `AGENTS.md` for behavioral rules. Derive stack versions, commands, module boundaries, and other repository facts from current manifests, lockfiles, build configuration, code, and CI; report factual conflicts with guidance.

3. **Choose a mode.**
   - **Empty project:** read available product documents, identify unresolved stack or platform choices, and ask the user before making product-level decisions. Stack confirmation does not authorize source, dependency-manifest, or entry-point creation; create a minimal scaffold only after separate explicit authorization.
   - **Existing project:** compare the observed project with existing guidance. Add missing, non-conflicting information incrementally. Never replace a whole file, delete unrelated content, change conflicting text without confirmation, or perform unrelated reformatting or reordering. After confirmation, use the smallest line-level or section-local revision for disputed or stale text.

4. **Write the guidance contract.**
   - Make `AGENTS.md` in the write scope the canonical AI-guidance entry after repository facts have been verified from current artifacts. If project-wide placement requires writing outside the scope, report that and ask before widening.
   - Preserve and synchronize existing `.claude/CLAUDE.md` and `.claude/rules/*.md` without introducing statements that conflict with `AGENTS.md`.
   - Do not create missing `.claude` files during an `AGENTS.md`-only initialization. Create them only when the user explicitly requests Claude compatibility.
   - Keep custom sections and rules. Create only files relevant to detected modules.
   - Use model-neutral prose. Record commands in the repository's evidenced OS, shell, wrapper, and working directory; add cross-platform variants only when repository evidence supports them.

5. **Respect safety boundaries.**
   - For credential-bearing files such as `.env`, key stores, certificates, and service-account files, detect only whether the path exists. Never read, print, copy, summarize, or hash their contents. Read sanitized examples such as `.env.example` only when they contain placeholders.
   - Do not install large dependency sets, start production services, deploy, migrate production data, or make unrelated project changes.

6. **Verify before reporting completion.**
   - Confirm every created or changed file exists, is readable, and has valid relative references.
   - Check documented commands against manifests and configuration; distinguish structurally verified commands from commands actually run.
   - Scan only generated or modified files for embedded secrets, private keys, live tokens, passwords, and credential-bearing URLs.
   - Review the final diff for scope, contradictions, accidental replacement, and unsupported claims.

## Required Result

Return `DONE` when the contract is satisfied or `DONE_WITH_CONCERNS` when unresolved conflicts or user decisions remain. Include separate lists for:

- newly created files;
- modified files and appended sections;
- preserved existing files or sections;
- items requiring manual confirmation;
- verification evidence and commands actually run.
