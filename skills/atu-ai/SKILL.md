---
name: atu-ai
description: Use when the user invokes $atu-ai or asks to continue implementation from an approved specs/PLAN.md, numbered feature specification set, or specs/quick compact specification.
---

# ATU AI

Implement an approved ATU specification using exactly one execution mode. Do not load both mode references speculatively.

## Common boundaries

- Resolve the authorized specification and code repositories from the request. Read applicable `AGENTS.md` and protect all pre-existing or concurrent changes.
- Treat confirmed requirements and acceptance outcomes as the contract. Stop for unresolved business, security, authorization, destructive-data, external-contract, or scope decisions.
- Use test-first implementation, the repository's supported checks, current diff evidence, and truthful `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, or `MANUAL REQUIRED` results.
- Keep credentials, production data, destructive actions, external writes, dependencies, and generated artifacts within explicit authorization.
- Never infer commit, push, publish, deploy, production migration, or release authority from workflow selection or completion.
- A request to save time or force compact mode never overrides a strict trigger. When mode evidence is uncertain, use the standard workflow.

## Select one mode

Use the **compact workflow** only for an approved file under `specs/quick/` that contains the required compact status, design, acceptance, and single-task contract. An explicit compact-spec path wins; otherwise auto-select only when exactly one compact file is `READY`. Re-check eligibility against repository evidence before editing.

Use the **standard workflow** for `specs/PLAN.md`, numbered feature specifications, a user-forced strict run, multiple independently deliverable tasks, or any new/changed authentication, authorization, privacy, payment, schema, migration, backfill, destructive-data, public API, external-service, queue, production-configuration, deployment-topology, cross-repository, or material cross-module contract. Use it whenever classification is uncertain.

Consuming an existing authenticated API, repository abstraction, component, or library may remain compact when its security, ownership, protocol, data-lifecycle, and failure contracts stay unchanged.

If no approved standard or compact specification exists, stop and route the request to `$atu-prd`; `$atu-ai` does not invent the missing contract.

Before taking any workflow action, read the selected reference completely:

- Compact: [Quick execution](references/quick-execution.md)
- Standard: [Standard workflow](references/standard-workflow.md)
