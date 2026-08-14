# Security Review Checklist

Apply repository `AGENTS.md` security instructions and current feature threat boundaries before this generic checklist. Record evidence and affected trust boundary for every finding. Default severities may be adjusted with justification.

## Secrets and dependencies

- [S1] Keep real passwords, tokens, API keys, signing material, and connection strings out of source, client bundles, resources, logs, and examples — error
- [S2] Exclude files containing real secrets or credentials, such as populated `.env` files, service-account credentials, signing keys, and upload keys, from version control and the reviewed snapshot. Sanitized `.env.example`, `.env.template`, and other placeholder-only templates are allowed and encouraged; judge the values, not the filename — error
- [S3] Read secrets through the project's validated configuration layer and fail safely when required values are absent — warning
- [S4] Treat dependency vulnerability claims as verified only when a current supported audit/source was actually checked — warning

## Untrusted input and output

- [S5] Validate and normalize every external input before use, including body, query, path, header, file, callback, and third-party data — error
- [S6] Use parameterized database/query APIs; do not concatenate untrusted SQL or command fragments — error
- [S7] Sanitize untrusted HTML and avoid dynamic execution such as `eval` or `new Function` — error
- [S8] Do not put credentials or sensitive personal data in URLs, client-visible configuration, or verbose error output — warning
- [S9] Prevent path traversal, unsafe file types, unbounded upload size, and public access when handling files — error

## Authentication and authorization

- [S10] Reject unauthenticated access to protected operations through the established auth boundary — error
- [S11] Check resource ownership, role, tenant, and institution boundaries to prevent IDOR and confused-deputy behavior — error
- [S12] Do not reveal account existence or sensitive policy details through authentication errors — warning
- [S13] Protect cookie-authenticated state changes against CSRF and use appropriate cookie attributes — warning
- [S14] Apply rate limits, replay protection, idempotency, or lockout controls to abuse-sensitive operations as required by the feature — warning

## Integrations and failure handling

- [S15] Verify webhook/callback signatures, freshness, event identity, amount/order ownership, and idempotency before side effects — error
- [S16] Enforce HTTPS/TLS and validate externally supplied destinations rather than allowing SSRF or arbitrary redirects — error
- [S17] Keep stack traces, internal paths, SQL, credentials, and infrastructure details out of client-visible errors — warning
- [S18] Log security-relevant events without recording secrets or unnecessary personal data — warning
