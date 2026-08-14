---
name: atu-miniprogram-engineer
description: Use when implementing or changing a native WeChat Mini Program built with WXML, WXSS, JavaScript or TypeScript, including pages, components, wx APIs, app.json, login, request integration, storage, privacy, subpackages, preview, or upload.
---

# Mini Program Engineer

Implement only the assigned native WeChat Mini Program scope. Follow the repository's JavaScript/TypeScript choice, component library, request layer, package layout, and platform privacy rules.

## Establish the contract

Before editing:

1. Read the repository's `AGENTS.md` and any nested `AGENTS.md` governing the target files.
2. Read the current feature's `requirements.md`, `design.md`, `tasks.md`, and `LESSONS.md` when present, focusing on page flow, state transitions, API contracts, privacy, and acceptance criteria.
3. Inspect `git status` and relevant diffs. Preserve user changes; avoid unrelated reformatting, generated output, or changes to other pages/features.
4. Inspect `project.config.json`, `app.json`, global app files, existing pages/components, request/auth wrappers, tests, and package configuration.

Escalate ambiguous business behavior, privacy choices, credentials, upload actions, or destructive configuration changes.

## Detect and follow the project

- Read `miniprogramRoot`, appid/settings, page registration, `tabBar`, `subpackages`, `usingComponents`, and rendering backend.
- Use TypeScript only when the project already uses it; otherwise follow JavaScript.
- Detect npm/miniprogram package build and the existing UI library before adding imports or components.
- Match the existing page/component structure, naming, lifecycle, styles, request wrapper, and authentication flow.

## Implement

### Pages and components

- Register new pages in `app.json`.
- Keep each native page's WXML/WXSS/JS-or-TS/JSON files consistent.
- Use `Page` and `Component` lifecycle APIs correctly; mark component JSON with `"component": true`.
- Update view data through `setData`; send only changed fields, use data paths for targeted updates, and coalesce high-frequency updates.
- Give every `wx:for` a stable `wx:key`.
- Use `properties` for parent-to-child input and `triggerEvent` for child-to-parent events.
- Follow existing responsive units and global tokens/styles; do not introduce arbitrary fixed styling.

### Requests, login, and storage

- Reuse the central request wrapper for base URL, token, timeout, error codes, and loading behavior.
- Require HTTPS/WSS in production and document every required WeChat legal-domain allowlist entry.
- Use `wx.login` code once, exchange it on the backend, and carry only the backend-issued application session/token.
- Never place AppSecret or session_key in the client, logs, package, or storage; do not expose sensitive openid data unnecessarily.
- Validate backend data before rendering and handle expired login, offline, non-success, empty, and malformed responses.
- Store only what is needed, for the shortest practical duration. Avoid plaintext persistence of sensitive values.

### Privacy, navigation, and packaging

- Request user data, phone, location, album, or similar access only through an explicit user action and the project's privacy flow; provide denial/cancellation behavior.
- Use the correct navigation API for tab and non-tab pages and preserve back-stack semantics.
- Keep the main package small, use existing subpackage conventions, and move large media to approved remote hosting where appropriate.

## Verify

Run available static checks, tests, and project-specific CI/preview commands. For platform behavior, compile in WeChat DevTools and use real-device testing for authorization, navigation, storage, network-domain, layout, and lifecycle behavior when required. Build npm dependencies first when the project requires DevTools' npm build step.

Preview or upload is an external release action: perform it only when authorized and when appid/upload credentials are available.

Never claim compilation, type checking, lint, preview, upload, real-device behavior, legal-domain configuration, or acceptance criteria passed unless the stated check actually ran successfully. Mark manual-only and unexecuted checks explicitly.

## Report

- List created or modified files, including `app.json` and configuration changes.
- Report exact checks and outcomes.
- State backend method/path, input/output/error contracts, auth behavior, and legal domains.
- Identify privacy approvals, appid/upload keys, DevTools/device-only validation, cross-team dependencies, risks, and blockers.
