# Personal Report Video Actions

- Status: READY
- Mode: compact
- Date: 2026-08-14
- Source: matched synthetic request; existing Vue report page; verified authenticated Axios client and protected Blob preview/download endpoints; nearby component/browser checks.

## Goal

Let an authenticated report user preview a video without autoplay and download it with the server-provided filename while releasing temporary browser resources.

## Scope

- In scope: two actions on the existing report page, a non-autoplay dialog, protected Blob requests, server filename handling, object-URL cleanup, and focused verification.
- Out of scope: API, authentication, authorization, ownership, schema, dependency, public compatibility, external service, production configuration, deployment, and unrelated report changes.

## Reused contracts and evidence

- Reuse the page's component conventions and established error feedback.
- Reuse the authenticated Axios client and verified protected endpoints without changing request, response, filename, ownership, or error contracts.

## Compact eligibility and escalation triggers

- Eligible because: one repository, one localized UI/Blob lifecycle slice, one task, four observable outcomes, closed decisions, focused component/browser verification, and localized rollback.
- Escalate if: implementation requires any auth/ownership/API/filename contract, schema, retention/lifecycle, shared-state, dependency, external/config/deployment, cross-repository, independent-task, or unbounded-verification change.

## Bounded design

- Affected boundary: existing Vue report page, local dialog/media state, and focused tests.
- Behavior flow: preview fetches a protected Blob, opens paused with controls, and reports failures without retaining a stale source. Download fetches through the same client and triggers one browser download with the response filename.
- Security and compatibility: never expose an unauthenticated media URL or bypass existing auth, ownership, error, and filename handling.
- Lifecycle and recovery: revoke the prior preview URL before replacement; on close/unmount pause and clear media, revoke once, and ignore or dispose of late responses; revoke the download URL after triggering. Rollback reverts only page/test changes.
- Verification: component tests cover authenticated calls, paused state, success/failure, filename, late responses, repeated open/close, and every revoke point. An authenticated browser verifies user-started playback, close cleanup, and downloaded filename; unavailable required browser evidence remains `MANUAL REQUIRED`.

## Acceptance criteria

- [ ] AC-Q01: Preview opens the existing report video in a controlled dialog and remains paused until explicit user playback.
- [ ] AC-Q02: Successful and failed preview responses use existing authenticated/error behavior without stale playable media.
- [ ] AC-Q03: Replacement, close, unmount, and late completion clear media and revoke every preview object URL.
- [ ] AC-Q04: Download uses the exact server filename, revokes its temporary URL, and triggers nothing on failure.

## Task

- [ ] T-Q01: Implement and verify the complete bounded change. Covers: AC-Q01, AC-Q02, AC-Q03, AC-Q04.

## Execution evidence

- Pre-existing changes: pending Q1
- Changed files and diff scope: pending
- Verification commands and results: pending
- Acceptance matrix: pending
- Manual or external boundaries: authenticated browser evidence pending

## Open questions

None.

## Handoff

`$atu-ai specs/quick/20260814-personal-report-video-actions.md`
