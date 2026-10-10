# Frontend changes

Use this reference when the assigned change affects browser UI or its API integration.

- Keep the agreed page flow, states, permissions, responsive behavior, and API contract. Use existing components, tokens, and request handling. A supplied design that conflicts with the specification needs a product decision; absence of a design alone is not a blocker when the contract and existing product are sufficient.
- Do not invent backend fields or behavior. If an unavailable dependency is replaced by an authorized mock, isolate it and record what real integration must replace it. Mock success does not establish service compatibility.
- Preserve relevant server-rendering boundaries and existing navigation/state behavior when changing client code.

Verify changed interactions in a real browser at the required viewport sizes, including relevant loading, empty, denied, and failure states and console/network errors. When the acceptance source is a design or screenshot, compare the rendered result with it and identify deviations. Compilation and component tests alone do not establish browser behavior, accessibility, or design fidelity; record unavailable checks under the selected workflow's acceptance evidence.
