# Standard ATU AI Workflow

Continue an approved standard specification through four stages. `PLAN.md`, each feature's `requirements.md`, `design.md`, and `tasks.md`, plus applicable `LESSONS.md`, remain the delivery contract. Read only the current stage reference; do not preload all four.

## Boundaries

- Work only in authorized repositories, features, tasks, and environments. Preserve pre-existing and concurrent changes.
- Stop for an unresolved business, security, authorization, destructive-data, external-contract, or scope decision. Do not invent a decision to keep moving.
- Treat unavailable required environments or evidence truthfully as `NOT RUN`, `MANUAL REQUIRED`, or `BLOCKED`; narrower or mocked checks cannot prove an unavailable real boundary.
- Keep credentials, production data, dependencies, destructive operations, and external writes within explicit authorization.
- Workflow progress never authorizes a commit, push, publication, deployment, migration, or release.

## Four-stage route

```text
S1 Boundary
  -> S2 Implement one task test-first
       -> S2 for another ready task in the same feature
  -> S3 Verify the complete feature once
       -> S2 for an implementation or test fix
       -> S3 for a verification-only gap
  -> S4 Close or recover
       -> S1 for another ready feature
       -> DONE when no authorized work remains
```

A blocked feature may yield to an independent ready feature. Otherwise report the exact blocker and stop.

## Stage routing

- S1: [Boundary](S1-boundary.md)
- S2: [Implement](S2-implement.md)
- S3: [Verify](S3-verify.md)
- S4: [Close and recover](S4-close.md)

Report progress at stage boundaries without narrating every internal check. Re-enter only the affected stage after a fix; do not restart the whole workflow when current evidence remains valid.
