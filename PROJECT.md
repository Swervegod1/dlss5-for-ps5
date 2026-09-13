# DLSS5 FOR PS5 — Project Plan

This document turns the repository roadmap into a public, contribution-friendly project plan. It can also be copied into a GitHub Projects board.

## Goal

Build and validate a lightweight external PS5 video-enhancement workflow for PC that improves the presentation of PS Remote Play, capture-card feeds, and local video through WebGL 2 spatial processing while remaining clear about what it does and does not do.

## Project status

**Current release:** v0.1.0 experimental preview  
**Primary stack:** HTML, JavaScript, WebGL 2, GLSL, optional Python launcher, Docker/GHCR  
**Current focus:** compatibility testing, latency measurement, capture-card validation, discoverability, documentation, and safe performance tuning.

## Workstreams

| Workstream | Priority | Status | Success criteria |
| --- | --- | --- | --- |
| Remote Play compatibility | P0 | Testing | Repeatable setup on Windows with documented browser/GPU combinations |
| Capture-card compatibility | P0 | Testing | At least several real USB capture devices documented |
| Latency benchmarking | P0 | Planned | Measured input-to-preview latency methodology and published results |
| Image-quality validation | P0 | Planned | Repeatable before/after test clips and artifact notes |
| Renderer reliability | P1 | Active | WebGL checks remain green across supported browsers |
| Accessibility | P1 | Active | Keyboard/focus/labels remain usable and documented |
| Packaging | P1 | Active | Release ZIP and GHCR image remain reproducible |
| SEO/AEO/AI discovery | P1 | Active | Accurate repository metadata, FAQ, llms.txt, citation metadata, and topic set |
| Community reporting | P1 | Planned | Structured issue templates for bugs, compatibility reports, and ideas |
| Future AI research | P2 | Research | Only after benchmarked spatial baseline and a licensed model path exist |

## Suggested GitHub Projects columns

1. **Inbox** — new reports and ideas
2. **Triaged** — reproducible and scoped
3. **Ready** — requirements clear
4. **In progress** — active work
5. **Validation** — testing/review required
6. **Done** — merged and verified
7. **Research** — ideas not yet committed to the product roadmap

## Recommended fields

- Priority: P0 / P1 / P2 / P3
- Area: Remote Play / Capture Card / Rendering / Performance / Docs / Packaging / Discovery / Research
- Type: Bug / Enhancement / Compatibility / Benchmark / Documentation / Research
- Release: v0.1.x / v0.2 / Future
- Hardware tested: Yes / No

## High-value next milestones

### Milestone A — Compatibility baseline
- Collect Windows + Chrome/Edge Remote Play reports.
- Record GPU/browser/input resolution/output resolution.
- Document capture-card models that expose usable browser video devices.
- Add reproducible failure cases to VALIDATION.md.

### Milestone B — Performance baseline
- Measure preview update rate under 720p, 1080p, 1440p, and 2160p output buffers.
- Add a defensible end-to-end latency test method.
- Record CPU/GPU/browser behavior instead of claiming unmeasured FPS gains.

### Milestone C — Public launch polish
- Apply GitHub Topics from DISCOVERY_TAGS.md.
- Add a real social-preview image.
- Publish a short demo clip showing the original/enhanced split view.
- Keep release notes, screenshots, FAQ, package instructions, and README synchronized.

## Definition of done

A feature is considered done when its source is committed, automated checks pass, user-facing behavior is documented, limitations are explicit, and any performance/compatibility claim has a reproducible test behind it.
