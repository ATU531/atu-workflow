# Project Initialization Contract

## Contents

1. [Root and evidence rules](#1-root-and-evidence-rules)
2. [Technology-stack detection checklist](#2-technology-stack-detection-checklist)
3. [Mode A: empty project](#3-mode-a-empty-project)
4. [Mode B: existing project](#4-mode-b-existing-project)
5. [Target-file contract](#5-target-file-contract)
6. [Codex and Claude synchronization](#6-codex-and-claude-synchronization)
7. [Safety and verification](#7-safety-and-verification)
8. [Acceptance checklist](#8-acceptance-checklist)

## 1. Root and evidence rules

Resolve two boundaries before writing:

1. **Discovery start:** use the exact directory named by the user. If no directory was named, start from the current working directory.
2. **Repository root:** from the discovery start, use `git rev-parse --show-toplevel` when inside a Git worktree; otherwise walk upward to the nearest directory containing strong project markers such as `AGENTS.md`, a dependency manifest, a root README, or `.claude/`.
3. **Requested write scope:** use the explicit user path when provided. Otherwise default it to the discovered repository root.
4. If markers identify multiple plausible repository roots or the requested project-wide file belongs above the write scope, report the options and ask before writing.

Never widen an explicitly named write scope. Read governing `AGENTS.md` files from the repository root down to the write scope, including nested files that apply to a target subdirectory. This read-only discovery above the scope is required for instruction compliance, but it does not authorize writes there.

Separate instructions from facts:

- Follow normal platform instruction precedence and all applicable `AGENTS.md` behavioral rules for work inside their scope.
- Establish stack versions, commands, module boundaries, and runtime facts from current manifests, lockfiles, build configuration, source code, and CI.
- Treat README, `AGENTS.md`, and `.claude/` factual statements as claims to verify against current repository artifacts. Report a contradiction instead of silently choosing one.

Do not invent framework versions, commands, directory purposes, coverage targets, deployment steps, naming conventions, or branch policies. When evidence is incomplete, mark the fact unknown or request confirmation.

Credential-bearing files are not evidence sources. Detect their paths only; do not open them. Sanitized examples and checked-in templates may be read only when they contain placeholders rather than live values.

## 2. Technology-stack detection checklist

Inspect only the rows relevant to the project.

| Area | Primary evidence | Facts to record |
|---|---|---|
| Repository | `.git/`, README, CI files, workspace config | project purpose, repository boundaries, modules |
| JavaScript / TypeScript | `package.json`, lockfile, `tsconfig*.json`, bundler config | runtime, framework, package manager, scripts, module format |
| Python | `pyproject.toml`, `requirements*.txt`, `uv.lock`, `poetry.lock`, app entry points | Python version, framework, environment manager, commands |
| Go | `go.mod`, `go.work`, `Makefile` | Go version, modules, build/test commands |
| Rust | `Cargo.toml`, `Cargo.lock`, workspace members | toolchain, crates, features, build/test commands |
| JVM / Android | `pom.xml`, `build.gradle*`, `settings.gradle*`, `gradlew*`, manifests | Java/Kotlin version, modules, SDK levels, Gradle tasks |
| .NET | `*.sln`, `*.csproj`, `global.json` | SDK version, projects, restore/build/test commands |
| PHP / Ruby | `composer.json`, `Gemfile`, framework config | language/framework version, package and test commands |
| Web frontend | Vite/Next/Nuxt/Vue/React config, route and component directories | UI framework, routing, state, style and build conventions |
| Backend API | server entry point, route/controller/schema config | framework, API prefix, auth, error and serialization conventions |
| Database | ORM config, schema, migrations, Compose services | engine, ORM, migration and test-data conventions |
| Native/mobile | Android/iOS/Flutter/React Native/Electron/Tauri markers | target platforms, packaging, permissions, platform boundaries |
| WeChat mini program | `project.config.json`, `app.json`, page four-file sets | language, npm usage, subpackages, request/auth conventions |
| Quality | formatter, linter, type-checker, test and coverage config | exact commands, file patterns, required checks |
| Operations | Dockerfiles, Compose, deployment docs, CI/CD | local-only commands, deploy boundaries, service dependencies |

For every documented command:

1. Locate its source in a manifest, wrapper, Makefile, README corroborated by configuration, or CI job.
2. Record its required working directory.
3. Record the OS, shell syntax, executable wrapper, and environment assumptions actually supported by repository evidence.
4. Preserve repository-native commands rather than forcing neutral or cross-platform syntax. Add platform variants only when observed.
5. Mark missing commands as unavailable; never synthesize a plausible command and present it as verified.
6. Distinguish install, development, build, test, lint, format, type-check, migration, and deployment commands.

Choose a package manager from the checked-in lockfile and workspace configuration. If multiple lockfiles conflict, report the conflict instead of choosing silently.

## 3. Mode A: empty project

Classify a directory as empty only when it has no implementation source, dependency manifest, build configuration, or established application structure. A directory containing only product documents may qualify. If the classification is uncertain, treat it as an existing project until the user confirms otherwise.

Follow this sequence:

1. Inventory product and architecture documents within scope.
2. Determine intended surfaces: web frontend, API, database, mini program, native app, desktop app, or other targets.
3. Extract explicitly selected languages, frameworks, data stores, package managers, platforms, and third-party services.
4. List unresolved product-level choices. Ask the user to decide them; offer concise defaults with trade-offs when useful.
5. Ask separately whether the user authorizes a minimal scaffold. Technology-stack confirmation alone is not authorization.
6. Without explicit scaffold authorization, do not create source directories, dependency manifests, build configuration, or entry points. Create only the requested guidance, and label unavailable commands as undecided or pending implementation.
7. With explicit scaffold authorization, create the smallest scaffold needed to make the approved stack concrete.
8. Create `AGENTS.md` within the write scope. Synchronize Claude files that already exist; create missing `.claude` files only when the user explicitly requests Claude compatibility.
9. Validate authorized artifacts and guidance without installing a large dependency tree or starting a production service.

A minimal scaffold may contain dependency manifests, basic compiler/linter configuration, `.gitignore`, a placeholder-only `.env.example`, agreed source directories, and one minimal entry point. It must not contain speculative product features. If any unexpected existing file appears during scaffolding, stop and reclassify the project before writing further.

## 4. Mode B: existing project

Follow this sequence:

1. Inventory existing `AGENTS.md`, `.claude/CLAUDE.md`, `.claude/rules/`, README files, manifests, build configuration, and relevant custom guidance.
2. Build an evidence table for stack facts, commands, directory responsibilities, and conventions.
3. Classify each desired item:
   - **present and consistent:** preserve it;
   - **missing:** append it or create the relevant missing file;
   - **stale or contradictory:** report exact file and heading before proposing a change;
   - **custom but valid:** preserve it even when it is outside the standard layout.
4. Apply only missing, non-conflicting additions.
5. Do not replace whole files, normalize the user's formatting, reorder unrelated sections, rename custom rules, or delete unrelated content.
6. For a conflict, show the observed project evidence and the existing statement. Wait for confirmation before editing the disputed statement.
7. After confirmation, replace only the smallest disputed or stale lines or local section. Do not use confirmation as permission for a whole-file rewrite, unrelated deletion, or unrelated cleanup.
8. Re-read the affected sections and inspect the final diff.

An append is not safe merely because it leaves old text intact. Do not append a second command, version, or convention that contradicts an existing one; classify that as a conflict.

## 5. Target-file contract

### `AGENTS.md` in the write scope

`AGENTS.md` is the authoritative Codex-facing entry point for its scope. The project-wide file normally belongs at the repository root; if that location is outside the requested write scope, report it and ask before widening the scope. Keep the file concise and evidence-based. Include only applicable sections:

- project name and one-sentence purpose;
- technology stack and important version constraints;
- exact commands with working directories;
- key directory or module map;
- project-specific coding, testing, security, database, frontend, backend, app, and Git conventions;
- links or plain relative paths to detailed project rules when useful.

Do not place secrets, machine-specific credentials, unverified operational claims, or generic advice in this file. Preserve nested `AGENTS.md` files and respect their narrower scope.

### `.claude/CLAUDE.md`

When this file already exists, synchronize its shared verified facts incrementally. When it is missing, create it only after the user explicitly requests Claude compatibility. An `AGENTS.md`-only request must not create it. It must:

- remain semantically consistent with root `AGENTS.md`;
- preserve existing custom sections except for the smallest disputed or stale text the user explicitly confirms replacing;
- receive only missing, non-conflicting additions during an incremental refresh;
- identify project-relative rule paths without asserting unsupported import behavior;
- avoid claiming authority over the applicable `AGENTS.md`.

For an `AGENTS.md`-only request, inspect and preserve an existing `.claude/` tree and synchronize only its existing files when changes are non-conflicting. Do not add missing compatibility files or rule files unless the user explicitly asks for them.

### `.claude/rules/*.md`

Create a missing rule only when Claude compatibility was explicitly requested and the rule is justified by a detected module. Otherwise synchronize only rule files that already exist. Common topics include coding style, testing, security, Git workflow, frontend, backend API, database, and native or mini-program development.

Each new rule file should contain:

- a short purpose or description;
- a path scope when the rule applies only to part of the repository;
- concrete rules derived from checked-in configuration and code;
- no duplicated or contradictory command definitions.

Existing rule files are user content. Preserve their names, order, formatting, and custom sections; after explicit confirmation, replace only the smallest disputed or stale text and never delete unrelated content. Add a missing rule only when the corresponding module exists.

### Empty-project scaffold

Scaffold files are allowed only in empty-project mode after the user separately and explicitly authorizes scaffold creation. Agreement on the technology stack is insufficient. Keep the scaffold minimal, placeholder-only, and within the requested write scope. Do not install dependencies as a side effect unless the user separately authorizes it.

## 6. Codex and Claude synchronization

Keep instruction priority and factual evidence separate:

- **Behavioral instructions:** follow the active platform instruction hierarchy and applicable `AGENTS.md`, with the most specific file governing its subtree. Claude compatibility files must not weaken those rules.
- **Repository facts:** verify versions, commands, package managers, paths, and runtime behavior from current manifests, lockfiles, build configuration, source code, wrappers, and CI. Use maintained README or operational documentation as secondary evidence. Treat factual claims in `AGENTS.md` and `.claude/` as potentially stale until corroborated.

When instruction text conflicts with repository facts, obey the behavioral constraint, report the factual mismatch, and do not rewrite either side without the required confirmation. Evidence priority determines what to report; it does not authorize overwriting user content.

Synchronize semantically rather than by copying whole files:

1. Extract shared facts into a comparison table.
2. Map equivalent sections across `AGENTS.md`, `.claude/CLAUDE.md`, and relevant rules.
3. Preserve consistent statements even when wording differs.
4. Append a missing fact to the appropriate file only when it does not conflict.
5. Report contradictions with both locations and the repository evidence.
6. After user confirmation, update only the smallest disputed lines or local section; do not replace the whole file or touch unrelated content.
7. Recompare stack versions, commands, path scopes, safety constraints, and module boundaries.

Claude-only custom guidance may remain if it does not weaken or contradict the canonical project rules. Codex-only operational guidance need not be duplicated when it is irrelevant to Claude compatibility. Never create circular references or imply that one platform automatically loads the other's file.

## 7. Safety and verification

### Credential boundary

For `.env`, `.env.*` other than clearly sanitized examples, private keys, certificates, key stores, cloud credentials, service-account files, and similar artifacts:

- use only filename or existence checks;
- do not read, search, print, copy, summarize, parse, hash, or include their contents in prompts;
- do not transfer values into `AGENTS.md`, `.claude/`, examples, logs, or reports.

If a sanitized example contains a live-looking value, stop treating it as safe, report the path, and do not reproduce the value.

### Command boundary

Do not automatically:

- install large dependency sets;
- launch production or long-running services;
- deploy, publish, or push;
- execute production database migrations;
- run destructive cleanup or formatting across the repository.

Prefer structural verification against manifests and configuration. Run a command only when it is local, bounded, non-destructive, and useful; record exactly what was run and its result.

### Completion verification

Before reporting completion:

1. Confirm each target file exists and can be read back.
2. Resolve every relative file reference from the file that contains it.
3. Validate frontmatter or configuration syntax where applicable.
4. Compare every documented command with its evidence source and working directory.
5. Scan generated or modified files only for private-key blocks, credential assignments, live tokens, passwords, high-entropy secrets, and credential-bearing URLs.
6. Inspect the diff for changes outside the approved scope.
7. Recheck that no whole file was replaced and no unrelated content was deleted or reordered; verify that any replacement of disputed or stale text was explicitly confirmed and minimal.
8. Recheck semantic parity between `AGENTS.md` and Claude compatibility files.
9. Label checks as executed, structurally verified, skipped, or blocked.

## 8. Acceptance checklist

- [ ] The repository root and requested write scope are recorded separately.
- [ ] All applicable existing `AGENTS.md` instructions from the repository root through the write scope were read first.
- [ ] README, manifests, build/test/lint configuration, and relevant `.claude/` files were inventoried.
- [ ] The project was correctly classified as empty or existing.
- [ ] Behavioral rules follow applicable `AGENTS.md`; stack facts and commands follow current repository evidence.
- [ ] `AGENTS.md` is the canonical Codex entry point within the approved write scope.
- [ ] Existing Claude files are preserved and synchronized; missing ones were created only after an explicit compatibility request.
- [ ] No whole file was replaced and no unrelated content was deleted, reordered, or renamed.
- [ ] Conflicts were reported before disputed or stale text changed, and user-confirmed replacements were minimal and local.
- [ ] Empty-project source, manifest, configuration, and entry-point files were created only after explicit scaffold authorization.
- [ ] Commands include evidenced OS, shell, wrapper, and working-directory requirements; unsupported variants were not invented.
- [ ] Credential files were detected only by path and were not read or copied.
- [ ] No large dependency installation, production service start, deployment, or production migration occurred.
- [ ] Created and modified files passed syntax, reference, command, and sensitive-value checks.
- [ ] The final report separately lists new, modified, preserved, and manual-confirmation items.
- [ ] The result is `DONE` only when no unresolved concern remains.
