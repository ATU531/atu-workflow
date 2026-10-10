---
name: atu-prd
description: Turn a PRD or change request into ATU implementation specifications under specs/, with acceptance criteria.
---

# ATU PRD

Turn authoritative requirements into reviewable specifications without implementing business code. Select exactly one planning mode and read only that mode's reference completely before writing.

## Common boundaries

- Work only under the authorized project's `specs/` directory. Never edit application code, tests, migrations, manifests, dependencies, deployment state, or production data.
- Ground every material claim in explicit source material, a confirmed user answer, or current repository evidence. Keep an assumption or recommendation as an open question; never invent a decision to keep planning moving.
- Read applicable `AGENTS.md`, relevant existing specifications, target architecture/code/configuration evidence, and nearby tests in proportion to the request. Preserve every unrelated or unrecognized file and all pre-existing changes.
- Block or route around unresolved business, security, authorization, privacy, data, destructive-operation, public-contract, or external-system decisions.
- A user may force standard mode. A request to save time or force compact mode never overrides a strict trigger. When classification is uncertain, use standard mode.

## Select one mode

Use **compact mode** only when repository evidence supports all of these conditions:

- one bounded behavior in one repository and one localized module or coherent vertical slice;
- exactly one implementation-and-verification task and at most five observable acceptance outcomes;
- closed product and technical decisions, stable existing architecture/contracts, focused verification, and localized rollback; and
- no new or changed authentication, authorization, privacy, payment, audit policy, schema, migration, backfill, retention or data-lifecycle rule, destructive data operation, public API/compatibility contract, external service/callback/queue, production configuration, deployment topology, broad shared state, cross-repository boundary, or independently deliverable task, and verification can remain bounded and explicit. If verification cannot remain bounded and explicit, use standard mode.

Consuming an existing authenticated API, repository abstraction, component, or library remains compact-eligible when its security, ownership, protocol, data-lifecycle, and failure contracts stay unchanged.

Use **standard mode** for any strict trigger above, unresolved material question, multiple task or feature slices, a standard `--change` request, a user-forced strict run, or uncertainty about eligibility.

Before writing, read the selected reference completely:

- Compact: [Quick specification contract](references/quick-spec-contract.md)
- Standard: [Standard PRD workflow](references/standard-workflow.md)

Report the selected mode and evidence. End with a copyable `$atu-ai` command only when the resulting specification is implementation-ready; never start implementation from this Skill.
