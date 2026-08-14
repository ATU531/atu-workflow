---
name: atu-backend-engineer
description: Use when implementing or changing server APIs, RPC procedures, authentication and authorization, service-layer business logic, environment configuration, queues, webhooks, or third-party integrations in an existing backend.
---

# Backend Engineer

Implement only the assigned server-side scope. Adapt to the repository's framework, API conventions, authentication model, persistence layer, and deployment runtime.

## Establish the contract

Before editing:

1. Read the repository's `AGENTS.md` and any nested `AGENTS.md` governing the target files.
2. Read the current feature's `requirements.md`, `design.md`, `tasks.md`, and `LESSONS.md` when present, focusing on API contracts, business rules, ownership, and security.
3. Inspect `git status` and relevant diffs. Protect user changes, avoid unrelated formatting or cleanup, and do not overwrite work outside the assigned task.
4. Inspect existing routes/controllers, service modules, authentication middleware/decorators, configuration, models/repositories, error handling, and tests.

Escalate material ambiguity, destructive behavior, or a required change outside the authorized scope.

## Detect and follow the stack

- For Node/TypeScript, identify the runtime, web/RPC framework, validation library, auth library, environment schema, and test/build commands from repository configuration.
- For Python, identify Flask/FastAPI/Django, SQLAlchemy or other ORM, Marshmallow/Pydantic validation, auth mechanism, WSGI/ASGI entrypoint, and test/lint/type-check commands.
- For other stacks, apply the same rule: reuse established routing, validation, auth, error, configuration, and data-access abstractions.
- Consume existing models and repositories. If schema or migration work is needed, document the required database change rather than silently extending the task.

## Implement

- Reuse the project's module registration and request lifecycle; do not initialize a second router, application, RPC context, or database session pattern.
- Separate public and protected endpoints. Enforce authentication and authorization centrally where the framework supports it.
- Validate every untrusted path, query, header, body, callback, and third-party payload before use.
- Check resource ownership and tenant/institution boundaries to prevent IDOR and cross-account access.
- Keep business logic in the project's service/domain layer rather than duplicating it in handlers.
- Return the established JSON envelope, HTTP/RPC status, and business error codes. Do not leak stack traces, SQL, internal paths, or account-existence details.
- Use parameterized ORM/query APIs and explicit transaction, commit, and rollback behavior.
- Read secrets and connection values through the project's environment/configuration layer. Never hardcode them.
- For external services, implement timeout, error mapping, idempotency/retry behavior where relevant, signature verification for callbacks, and a truthful not-configured path.
- For mini-program or WebView clients, keep platform secrets on the backend, use HTTPS, and document the client-facing domain and contract requirements.

### Queues and background workers

- Assume at-least-once delivery unless the selected queue proves otherwise. Carry a stable message/event identifier and make the consumer idempotent before irreversible side effects, using the project's deduplication or unique-state mechanism.
- Acknowledge only after durable success. Set visibility timeout or lease longer than the expected handler duration, renew it when supported, and ensure a worker crash before ack results in safe redelivery rather than lost work.
- Classify failures: retry transient errors with bounded exponential backoff and jitter; do not retry permanent validation or authorization errors indefinitely. Cap attempts and route exhausted or poison messages to a dead-letter queue with enough safe diagnostic context for inspection/redrive.
- Version and validate message payloads, bound message size, and preserve compatibility across rolling producer/consumer deploys.
- On shutdown, stop taking new work, let in-flight handlers finish within a bounded grace period, then nack/requeue or allow visibility expiry safely; close queue, database, and network resources without acknowledging unfinished work.
- Keep publish, consume, purge, dead-letter redrive, and live worker operations scoped to authorized environments. Never use production queues for verification without explicit authorization.

## Verify

Run the repository's actual targeted and broader checks. Examples include:

```text
pnpm test
pnpm check
pnpm check-types
pnpm build

pytest
ruff check .
mypy .
```

Add or update tests for successful flows, invalid input, unauthenticated access, unauthorized ownership, dependency failure, boundary values, and transaction behavior. Start the service only when startup verification is relevant and safe.

For queue changes, verify duplicate delivery and idempotent consumption, crash/redelivery around the side-effect-to-ack boundary, visibility timeout or lease renewal, transient backoff, permanent failure, max-attempt dead-letter routing, payload-version compatibility, and graceful worker shutdown. Use an isolated test queue/worker; distinguish simulated behavior from a real broker and do not claim production queue state was validated unless it was.

Never claim type checking, linting, tests, builds, startup, integrations, or acceptance criteria passed unless they ran successfully. Mark failed, skipped, unavailable, and manual-only checks explicitly.

## Report

- List created or modified files.
- Report commands and exact outcomes, including failures.
- State endpoint contracts: method/path, authentication, input, output, errors, and side effects.
- State queue contracts: producer, payload/version, idempotency key, ack/visibility policy, retry/backoff limits, dead-letter behavior, and worker shutdown semantics.
- Identify required schema/migration work, environment variables, third-party setup, downstream coordination, risks, and blockers.
