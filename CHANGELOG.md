# Changelog

## Preview maintenance — 2026-09-13

- Added a compact README banner, check-status badge, support links, and compatibility-report entry points.
- Unified the prepared 20 GitHub topics and added a preview/apply helper for the owner’s existing GitHub CLI sign-in.
- Corrected Docker examples to bind the published port to loopback and documented its additional disk usage.
- Fixed release packaging to include linked documentation, nested assets, checks and per-file SHA-256 build provenance.
- Added archive integrity checks and source validation before publishing.
- Clarified the untested live-PS5 status, rolling preview assets, and undeployed website status.

## 0.1.0 — 2026-09-12

- Created a self-contained HTML/WebGL 2 video-filter prototype.
- Added local clip input and experimental Remote Play window/capture-card paths.
- Added bicubic/bilinear resizing, bounded sharpening, contrast, presets, before/after comparison, and full-screen preview.
- Added source cleanup, capture-cancellation handling, and synthetic renderer checks.
- Added a restricted localhost launcher, setup and troubleshooting documentation, a hardware-validation checklist, and a GitHub publishing guide.
- Added descriptive search/social metadata and repository topic suggestions using the owner-requested title **DLSS5 FOR PS5**.

Limitations: no NVIDIA DLSS implementation, neural model, PS5 binary, engine-level integration, frame generation, or verified live-console compatibility. Browser preview was blocked by the test environment's URL security policy. See VALIDATION.md for exact test coverage.
