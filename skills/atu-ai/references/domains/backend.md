# Backend changes

Use this reference for changed API, service, callback, or worker contracts; apply the queue section only when queue behavior is affected.

## Service boundaries

- Preserve the agreed method/path, payload, error envelope, authentication, ownership/tenant checks, and side effects. Reuse established request and transaction boundaries; do not silently extend an API task into unassigned schema or migration work.
- Keep platform credentials on the server and use the project's configuration layer. For callbacks and external services, verify the affected signature, timeout, retry/idempotency, error, and not-configured behavior against the real integration contract.
- Validate affected success, invalid input, unauthorized ownership, dependency failure, and commit/rollback behavior. Distinguish a simulated dependency from a tested real service; record target environment and client-facing domain/configuration requirements that remain unresolved.

## Queues and workers

For changed queue behavior, establish the producer/payload version, event identity, durability boundary, and recovery behavior:

- Assume redelivery unless the broker proves otherwise. Make irreversible side effects idempotent, and acknowledge only durable success. A crash between the side effect and acknowledgement must allow safe redelivery.
- Ensure visibility/lease duration and renewal cover the handler. Bound transient retries with backoff/jitter; separate permanent failures and route exhausted/poison messages to the established dead-letter path.
- Bound and validate payloads and preserve producer/consumer compatibility during rolling deployment. On shutdown, stop intake and allow bounded completion; unfinished work must remain recoverable without a false acknowledgement.

Verify affected duplicate delivery, crash/redelivery, lease, retry/dead-letter, payload compatibility, and shutdown paths using an isolated test queue/worker. State which checks used a real broker. Production publish/consume, purge, redrive, and worker operations require authorization for that environment; a test result does not establish production queue state.
