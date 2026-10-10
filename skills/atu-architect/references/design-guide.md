# Architecture and pattern decision guide

Read only the section relevant to the current choice. Start with existing conventions and the least complex design that meets evidenced requirements. These are options, not a required stack or checklist of patterns.

## Boundaries and quality

Group behavior that changes together; assign each business rule and authoritative write one owner. Name each module's public contract and forbidden dependencies. Keep coordination separate from persistence and external protocol details when they vary independently. Check whether a developer can change a module without understanding every caller's internals.

Test maintainability with a realistic change: adding a device provider should change its adapter and composition/configuration, not duplicate authorization or domain rules across providers. If the product has one stable provider and no independent variation, a direct integration may be sufficient.

Translate “scalable” into a workload and bottleneck hypothesis; “reliable” into a failure and recovery objective. Do not invent throughput/availability targets. Propose what to measure and the point at which an alternative becomes worthwhile. Enforce readability through cohesive responsibilities and explicit contracts, not arbitrary abstraction layers.

## Architecture styles

| Option | Consider when | Main cost / check |
| --- | --- | --- |
| Existing/simple layered design | A bounded application has straightforward rules and stable integrations | Keep business rules out of transport/persistence glue; avoid pass-through layers with no responsibility. |
| Modular monolith | Several business domains need clear ownership but one deployment and local transactions are adequate | Enforce module APIs; shared database access must not bypass ownership. Check dependency cycles and cross-domain writes. |
| Ports and adapters | A core use case must remain independent of changing external systems or needs meaningful substitutes | Introduce ports at actual variation boundaries, not an interface for every class. Verify adapter semantics and error mapping. |
| Asynchronous/event-driven collaboration | Decoupled timing, burst absorption, or independent consumers are requirements | Define event owner, durability, ordering needs, idempotency, bounded retry, lag visibility, and recovery. Compare with direct calls or an existing job mechanism first. |
| Separate services | Independent scale, deployment, isolation, or team ownership justifies a network/process boundary | Account for consistency, compatibility, observability, operations, and failure modes. Multiple modules alone do not justify services. |

DDD domain modeling can clarify complex rules and ownership; it does not require microservices. CQRS can separate materially different read/write needs; it does not require event sourcing. Event sourcing requires a demonstrated audit/replay need that outweighs event evolution and projection/recovery complexity.

## Implementation patterns at architectural boundaries

| Pattern | Concrete reason to use | Avoid / verify |
| --- | --- | --- |
| Strategy | Multiple supported policies implement the same stable business operation | One fixed branch rarely needs a hierarchy; test substitutability and policy selection. |
| Adapter | External protocols differ from the internal contract | Preserve protocol-specific failures; do not normalize unknown outcomes into success. |
| Facade / application service | A use case coordinates multiple owned operations | Keep authoritative rules in their owner; avoid a service that accumulates every domain. |
| Repository | Domain logic needs a meaningful persistence boundary | Reuse the existing ORM/repository when sufficient; avoid generic CRUD wrappers without a domain purpose. |
| Domain event / outbox | A confirmed state change must reliably notify another boundary | Use an outbox only where durable state/event coupling is required; verify duplicate delivery and partial failure. |

For each selected style/pattern record: **problem → simple alternative → choice and boundary → cost → verification**. Include only consequential decisions in architecture; defer local implementation details to feature design. Do not add patterns merely to demonstrate expertise.

## Existing-system evolution

Start with an evidence-backed current map. Identify what remains stable, the smallest seam for new behavior, and any dependency inversion or contract adjustment actually needed. Prefer incremental migration with compatibility windows and a clear data authority. Code rollback is not data restoration; distinguish reversible steps from irreversible state changes. Keep unrelated refactoring out of scope.
