# SEO, AEO, and AI-search strategy

This document defines the discoverability strategy for **DLSS5 FOR PS5** across traditional search engines, answer engines, GitHub search, and AI assistants.

## Primary entity definition

**DLSS5 FOR PS5 is an unofficial PC-side PS5 Remote Play and capture-card video enhancer using WebGL 2 upscaling and sharpening. It is not NVIDIA DLSS 5, Sony PSSR, or native PS5 software.**

That sentence is intentionally repeated in high-value documentation because it establishes the project's entity, purpose, platform, and limitations without making misleading claims.

## Canonical project URLs

- Repository: `https://github.com/Swervegod1/dlss5-for-ps5`
- Release: `https://github.com/Swervegod1/dlss5-for-ps5/releases/tag/v0.1.0`
- README: `https://github.com/Swervegod1/dlss5-for-ps5/blob/main/README.md`
- FAQ: `https://github.com/Swervegod1/dlss5-for-ps5/blob/main/FAQ.md`
- LLM summary: `https://github.com/Swervegod1/dlss5-for-ps5/blob/main/llms.txt`

## Recommended GitHub About description

`Unofficial PC-side PS5 Remote Play & capture-card video enhancer. WebGL 2 upscaling, sharpening, before/after comparison, local processing. Not NVIDIA DLSS 5 or native PS5 software.`

## Recommended GitHub topics

Use these as repository topics when editing the GitHub **About** panel:

`ps5`, `playstation-5`, `remote-play`, `ps-remote-play`, `video-upscaling`, `video-enhancement`, `image-sharpening`, `webgl2`, `glsl`, `capture-card`, `gameplay`, `browser-app`, `video-processing`, `ps5-pro`, `multimedia`

## Search intent map

### High-intent discovery terms

- PS5 Remote Play upscaler
- PS5 Remote Play enhancer
- PS5 Remote Play sharpening
- PS5 video enhancer PC
- PS5 capture card upscaler
- PS5 capture card video enhancement
- PS5 image sharpening PC
- browser PS5 video enhancer
- WebGL video upscaling
- gameplay video enhancer

### Informational questions

- How do I upscale PS5 Remote Play on PC?
- How do I sharpen PS5 Remote Play video?
- Can I use DLSS on PS5?
- Is DLSS5 FOR PS5 actually NVIDIA DLSS?
- Can I upscale a PS5 capture card to 4K?
- Does a PS5 video upscaler increase FPS?
- Can WebGL enhance capture-card video?
- Does PS5 Remote Play support external sharpening?
- Do I need an RTX GPU for this project?
- Does this project upload gameplay?

### Comparison queries

- DLSS vs PSSR vs PS5 video upscaling
- PS5 Remote Play upscaling vs native rendering
- bicubic vs bilinear gameplay upscaling
- capture-card upscaling vs PS5 native 4K
- WebGL upscaling vs AI super resolution

## Answer-engine optimization structure

AEO is implemented with:

1. A direct definition immediately below the README title.
2. A key-facts question/answer table.
3. Exact, natural-language headings that mirror user questions.
4. A dedicated `FAQ.md` containing short factual answers.
5. Consistent entity naming across README, FAQ, CodeMeta, citation metadata, release notes, and `llms.txt`.
6. Explicit correction language for common misunderstandings about DLSS, PSSR, native PS5 installation, FPS, frame generation, and 4K output.
7. Short answer-first paragraphs before longer technical explanations.

## AI-search / LLM discoverability

The repository contains several machine- and model-friendly surfaces:

- `llms.txt` — concise facts, preferred description, correction rules, and documentation links.
- `codemeta.json` — structured software metadata and semantic keywords.
- `CITATION.cff` — standardized software citation and attribution data.
- `repository-metadata.json` — repository-specific aliases, topics, and query phrases.
- `FAQ.md` — answer-sized factual passages for retrieval systems.
- `README.md` — human-readable primary source with direct answers and canonical identity.

These files can improve clarity for crawlers and AI retrieval systems, but no file can guarantee inclusion or ranking in Google, Bing, ChatGPT, Gemini, Perplexity, Copilot, or other AI/search products.

## Semantic entity aliases

AI/search systems may encounter the project under these accurate aliases:

- DLSS5 FOR PS5
- DLSS5 FOR PS5 PC video enhancer
- PS5 Remote Play video enhancer
- PS5 Remote Play upscaler
- PS5 Remote Play sharpening tool
- PS5 capture-card video enhancer
- WebGL PS5 video upscaler
- browser-based PS5 video processor

The aliases should always resolve back to the same canonical repository and should never imply native PS5 installation or NVIDIA affiliation.

## Page/title metadata

Recommended title:

`DLSS5 FOR PS5 | PS5 Remote Play Video Enhancer & WebGL Upscaler`

Recommended meta description:

`Unofficial PC-side PS5 Remote Play and capture-card video enhancer with WebGL 2 upscaling, sharpening and before/after comparison. Local processing; not NVIDIA DLSS 5 or native PS5 software.`

Recommended social title:

`DLSS5 FOR PS5 — PS5 Remote Play Video Enhancer`

Recommended social description:

`Enhance PS5 Remote Play or capture-card video on PC with lightweight WebGL 2 upscaling and sharpening. Experimental, local and unofficial.`

## Content architecture

The repository now separates intent cleanly:

- **README.md** — primary landing document and setup guide
- **FAQ.md** — answer-engine and conversational search questions
- **llms.txt** — compact AI-agent context
- **VALIDATION.md** — evidence, limitations, and verification status
- **ROADMAP.md** — future development direction
- **PACKAGE.md** — Docker/GHCR usage
- **codemeta.json** — machine-readable software entity metadata
- **CITATION.cff** — citation entity metadata

This is preferable to creating many thin, repetitive keyword pages. Search quality generally benefits more from useful, distinct documents than duplicated keyword stuffing.

## Trust and factuality signals

Keep these points explicit across public descriptions:

- The software runs on a PC, not directly on PS5.
- It processes already-rendered video.
- It does not implement NVIDIA DLSS 5.
- It does not implement Sony PSSR.
- It does not generate frames or increase native game FPS.
- 2160p output is an output-buffer size, not recovered native 4K detail.
- Compatibility, latency, and image-quality gains vary and are not guaranteed.
- The app does not include telemetry, recording, gameplay upload, or microphone capture in v0.1.

These statements help both users and AI systems distinguish the actual project from exaggerated claims.

## Internal-linking targets

The README links directly to the release, FAQ, validation report, roadmap, and `llms.txt`. The FAQ links back to the canonical repository and release. Machine-readable metadata also points to the repository, README, issue tracker, and release page.

## External authority opportunities

For future promotion, the strongest legitimate signals would come from useful external references rather than mass-posted spam links. Good targets include:

- relevant GitHub lists or curated repositories
- WebGL/video-processing communities
- PS Remote Play troubleshooting or enhancement discussions where the project genuinely answers the question
- capture-card and browser graphics communities
- technical demo posts that show measured before/after results
- a real project website or GitHub Pages deployment with a stable canonical URL

Avoid automated comment spam, fabricated reviews, fake benchmark claims, purchased backlinks, or misleading “native DLSS for PS5” headlines.

## Measurement plan

Track discoverability with real evidence when available:

- GitHub stars, forks, clones, traffic, and release downloads
- search impressions/clicks if a dedicated website is connected to webmaster tools
- referral domains
- FAQ/search queries that lead users to the project
- release download growth after documentation improvements

Do not invent metrics before they exist.

## Manual GitHub settings still worth applying

The repository content is optimized, but GitHub's visible **About** topics are repository settings rather than files. Apply the recommended description/topics manually if they are not already present. A future public deployment can also add a real website/homepage URL.

## Anti-keyword-stuffing rule

Use important phrases naturally in definitions, headings, direct answers, and examples. Do not repeat long keyword lists in visible user-facing sections solely for ranking. The project's usefulness, clarity, accurate terminology, external citations, and real adoption matter more than raw keyword density.
