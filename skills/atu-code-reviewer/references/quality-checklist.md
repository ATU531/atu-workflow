# Code Quality Review Checklist

Apply project `AGENTS.md` instructions and current feature contracts before this generic checklist. Record a finding only when the reviewed code supplies concrete evidence. Default severities may be adjusted with justification.

## Correctness

- [C1] Handle empty, null, zero, missing, malformed, oversized, and boundary inputs — error
- [C2] Handle errors and rejected operations; do not silently swallow exceptions or promises — error
- [C3] Preserve correct asynchronous ordering, cancellation, cleanup, and concurrency behavior — warning
- [C4] Match feature contracts for routes, inputs, outputs, statuses, fields, and state transitions — error
- [C5] Register and wire new routes, components, jobs, migrations, platform pages, and services in every required entrypoint — error
- [C6] Preserve transactionality or compensate for partial failure in multi-step writes — error

## Regression and architecture

- [R1] Preserve compatibility for callers, stored data, configuration defaults, and rolling deploy order — error
- [R2] Respect module/layer boundaries; avoid UI business orchestration, direct database access from clients, or duplicated session parsing — warning
- [R3] Reuse established components, services, request clients, repositories, and helpers — warning
- [R4] Add regression coverage for changed success, failure, boundary, authorization, and lifecycle behavior — warning

## Types and interfaces

- [T1] Avoid unjustified `any`, unsafe casts, ignore directives, and unchecked dynamic values — error
- [T2] Keep function, component, API, and event interfaces explicit and consistent with project conventions — warning
- [T3] Handle nullable values deliberately; avoid unjustified non-null assertions — warning

## Performance and resources

- [P1] Avoid N+1 database or network access — error
- [P2] Bound large lists, scans, loops, payloads, and retries with pagination, batching, or limits — warning
- [P3] Avoid unnecessary UI re-renders or repeated expensive computations — warning
- [P4] Clean up subscriptions, timers, listeners, browser/device resources, files, and connections — warning
- [P5] Inspect query plans or generated SQL for performance-sensitive data paths — info

## Maintainability

- [M1] Use names that communicate domain intent and follow existing file/module naming — warning
- [M2] Remove accidental dead/debug code and unused imports; preserve purposeful diagnostics — info
- [M3] Keep functions cohesive and control flow comprehensible; reduce excessive nesting and duplication — info
- [M4] Centralize repeated constants and business rules where the project has an established home for them — info
- [M5] Avoid unrelated refactors and formatting churn that obscure the reviewed behavior — warning
