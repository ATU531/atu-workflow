# Persistence changes

Use this reference when schema, migration, query, transaction, or Redis behavior changes; read only the relevant section.

## Schema and durable data

- Use the repository's migration mechanism and preserve existing migration history. Keep model constraints, ownership/session contracts, and consumers compatible with the agreed change; a manual schema edit is not a durable migration.
- Assess the affected table size, lock/backfill cost, deployment order, and mixed-version compatibility. Separate large backfills when necessary. Provide the project's required downgrade or a concrete forward-recovery plan; code rollback does not restore deleted data.
- Before an irreversible data change, establish the affected scope and usable backup/recovery evidence. Actual destructive or production application requires authorization for that action and target; preparation is not application, and existing authorization need not be requested again.
- In a suitable test environment, establish application from the current schema, constraints/model agreement, recovery, and affected transactional/query behavior. Inspect query plans where performance is part of the acceptance contract. Record environment, unapplied steps, and unavailable evidence rather than claiming production parity.

## Redis and cache state

For changed keys, specify namespace/scope, serialization/version, TTL or justified persistence, and durable authority. Prevent collisions across the required environment/tenant/version boundaries.

- Keep multi-step state transitions atomic. Locks need a unique owner, bounded lease/renewal, and owner-checked release; never release another worker's lock.
- Invalidate after the authoritative transaction commits and account for update/delete races and rolling versions. Preserve the required protection against negative lookups and concurrent hot-key rebuilds.
- Distinguish disposable-cache fallback from security/session/idempotency invariants, which must not silently fail open. Test relevant expiry, serialization, invalidation, concurrency, and Redis-unavailable paths in an isolated test namespace.
- Expired or invalidated state is not restored by code rollback. Define targeted invalidation, versioned keys, warm-up, natural expiry, or explain the absence of safe recovery. `FLUSHDB`, `FLUSHALL`, broad key deletion, and production cache/lock mutation require explicit authorization.
