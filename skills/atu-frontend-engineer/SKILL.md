---
name: atu-frontend-engineer
description: Use when implementing or changing browser-based frontend pages, components, routes, state, styling, accessibility, API integration, or design-file fidelity in React, Vue, Svelte, Next.js, Nuxt, or similar projects.
---

# Frontend Engineer

Implement only the assigned frontend scope. Match the existing framework, component system, visual language, state model, and routing conventions.

## Establish the contract

Before editing:

1. Read the repository's `AGENTS.md` and any nested `AGENTS.md` governing the target files.
2. Read the current feature's `requirements.md`, `design.md`, `tasks.md`, and `LESSONS.md` when present, focusing on states, interactions, responsive behavior, accessibility, and API contracts.
3. Inspect `git status` and relevant diffs. Preserve user changes and avoid unrelated refactors, formatting churn, or generated-file changes.
4. Inspect `package.json`, TypeScript/JavaScript configuration, routes, state management, API client, styles/tokens, existing components, and tests.

If a supplied design conflicts with the feature contract or leaves a material product decision unresolved, report the mismatch and request the decision. If no design is supplied and the contract is sufficient, follow the existing product system rather than blocking.

## Detect and follow the stack

- Identify the framework/version, rendering model, TypeScript/JavaScript mode, build tool, aliases, UI library, styling system, state manager, test stack, and supported commands.
- Search public/common component directories before creating a component.
- Reuse the installed UI library and design tokens. Do not add a second component framework or hardcode one-off colors/spacing when tokens exist.
- Match existing component, file, prop, composable/hook, and route patterns.

## Implement

- Keep reusable presentation components free of business-specific orchestration; compose them in feature components/pages.
- Model loading, empty, success, partial, disabled, unauthorized, and error states required by the contract.
- Keep state local unless it must be shared; use the project's store for cross-route/shared state.
- Integrate through the existing API client. Match request/response/error contracts and do not silently invent backend behavior.
- If a backend dependency is unavailable and a mock is explicitly appropriate, isolate it and mark the replacement condition clearly.
- Preserve SSR/SSG boundaries and avoid browser-only APIs during server rendering.
- Use semantic HTML, keyboard access, labels, focus handling, and adequate contrast.
- Keep responsive behavior consistent with existing breakpoints and tokens.
- Avoid unnecessary re-renders, unbounded lists, leaked subscriptions/listeners/timers, and duplicated derived state.

## Verify

Run the repository's actual targeted and broader checks, such as:

```text
pnpm test
pnpm lint
pnpm typecheck
pnpm build
```

When UI behavior changed, verify the relevant flows in a real browser at required viewport sizes. Check interactions, loading/error/empty states, console errors, network behavior, and visual fidelity. Use screenshots or design comparison when a design is the acceptance source.

Never claim lint, type checking, tests, builds, browser flows, responsiveness, accessibility, or design fidelity passed unless that validation actually ran and supports the claim. Mark manual-only and unexecuted checks explicitly.

## Report

- List created or modified files.
- Report exact commands and browser checks with outcomes.
- State design fidelity and any intentional deviation.
- Document backend contracts, mocks, cross-team dependencies, unresolved product decisions, and blockers.
