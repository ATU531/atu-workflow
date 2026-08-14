# Native WeChat Mini Program Review Checklist

Load this checklist only for native Mini Program changes, in addition to the quality and security checklists. Default severities may be adjusted when evidence justifies it.

## Security and privacy

- [MP1] Use HTTPS/WSS for production platform requests and document/configure required WeChat legal-domain allowlists — error
- [MP2] Keep session_key out of the client; avoid exposing sensitive openid data, and use each `wx.login` code only once — error
- [MP3] Never include AppSecret or other backend credentials in client code, configuration, logs, or packages — error
- [MP4] Keep application tokens scoped and short-lived where possible; avoid unnecessary plaintext persistence of sensitive information — warning
- [MP5] Access user information, phone, location, album, and similar data only through explicit user action and the required privacy flow — warning
- [MP6] Validate backend data before rendering or using it in navigation/state transitions — info

## Performance

- [MP7] Limit `setData` to changed fields, use data paths, coalesce updates, and avoid frequent large payloads — warning
- [MP8] Give every `wx:for` a stable `wx:key` — warning
- [MP9] Respect current platform package limits and repository subpackage/CDN strategy; verify limits rather than relying on stale constants — info
- [MP10] Page or virtualize long lists instead of rendering unbounded node counts — info

## Engineering

- [MP11] Register new pages in `app.json` and mark component JSON with `"component": true` — error
- [MP12] Reuse the central request layer for base URL, authentication, timeout, errors, and loading behavior — warning
- [MP13] Update rendered state through `setData`, not direct `this.data` mutation — warning
- [MP14] Follow the project's responsive units, tokens, and shared styles instead of isolated fixed styling — info
