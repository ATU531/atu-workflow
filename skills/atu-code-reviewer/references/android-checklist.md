# Android and WebView Review Checklist

Load this checklist only for native Android Java/Kotlin changes, in addition to the quality and security checklists. Default severities may be adjusted when evidence justifies it.

## WebView security

- [AND1] Do not expose objects to untrusted pages through `addJavascriptInterface`; if required, restrict content to an explicit trusted origin — error
- [AND2] Enable `setWebContentsDebuggingEnabled(true)` only for debug builds — warning
- [AND3] Keep file access, file-URL access, and universal file-URL access disabled unless explicitly required — warning
- [AND4] Validate scheme and host before loading or redirecting; block untrusted non-HTTP(S) navigation — error

## Networking and configuration

- [AND5] Keep network and disk I/O off the main thread; return to the main looper for UI updates — error
- [AND6] Prefer HTTPS and disabled cleartext traffic; if HTTP is unavoidable, constrain it through a narrow network security configuration — warning
- [AND7] Configure connection/read timeouts and handle non-2xx responses and parsing failures — warning
- [AND8] Validate server-provided URLs and configuration before use; do not trust arbitrary remote redirects — error

## Storage and secrets

- [AND9] Keep credentials, device secrets, and tokens out of source code and resources — error
- [AND10] Do not store sensitive values in plaintext preferences; use the project's secure storage strategy — warning
- [AND11] Handle missing/corrupt assets and preferences with safe defaults and controlled errors — warning

## Components and permissions

- [AND12] Declare `android:exported` explicitly and minimize externally reachable Activities, Services, Receivers, and ContentProviders; do not rely on SDK-version-dependent defaults — warning
- [AND13] Request dangerous permissions at runtime where required and handle denial with a safe fallback — warning
- [AND14] Register every added Activity, Service, Receiver, and ContentProvider in the manifest — error

## Kiosk and field operation

- [AND15] Keep operator-facing error screens and logs actionable, with enough status and lifecycle/failure context for normal field diagnosis — info
- [AND16] Recover from WebView renderer loss such as `onRenderProcessGone` instead of leaving a permanent blank screen — warning
- [AND17] Preserve an authorized, reversible maintenance/recovery route; do not require uninstalling the app or clearing configuration data — warning

## ContentProviders, URI grants, and logging

- [AND18] Give each ContentProvider a unique application-scoped authority; keep internal providers unexported, and protect exported providers with the narrowest read/write permission, preferably signature-level for trusted-app sharing — error
- [AND19] Constrain `FileProvider` roots and provider paths; validate caller, URI, MIME/mode, and prevent traversal or arbitrary file access — error
- [AND20] Grant only the required temporary URI read/write flags to the intended recipient and revoke them when the flow ends; do not expose broad or durable URI access accidentally — warning
- [AND21] Do not write credentials, tokens, device secrets, authentication material, or sensitive PII to logs or operator-facing errors — error
- [AND22] Keep production logs and error screens from exposing internal URLs, filesystem paths, stack traces, or infrastructure details — warning
