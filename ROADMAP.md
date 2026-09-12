# Development roadmap

## v0.1 — external video prototype

Implemented: local video-file input, browser window-capture path, selected USB video-device path, bicubic/bilinear interpolation, bounded spatial sharpening, before/after comparison, buffer-size control, presets, full-screen preview, source cleanup, and a synthetic renderer check. The presence of an input path does not establish tested hardware compatibility.

## Next — validate the actual setup

Record computer OS, GPU model, browser version, PS5 model, source method, game, input resolution, and display resolution. Never include serial numbers, passwords, tokens, or account identifiers in public bug reports.

1. Validate local clip playback and all renderer checks in the target browser.
2. Establish a working unprocessed Remote Play or capture-card baseline.
3. Test capture start, cancel, stop, source switching, window focus, and controller behavior.
4. Compare the filter with that baseline in motion, not only screenshots. Look for sharper text, ringing, moiré, noise, and shimmer. Keep the filter only where it helps.
5. Measure end-to-end latency with high-frame-rate camera footage of an input and visible response. Browser redraw frequency alone cannot measure it. Report median and worst observed delay over repeated samples.
6. Measure CPU/GPU load and memory at 720p, 1080p, and 1440p. Try 2160p only if the hardware can sustain it. Do not promise 4K/60 before measurement.

## Later — compact AI enhancement research

Select a small, explicitly licensed video-restoration or super-resolution model after knowing the target GPU and acceptable disk/memory budget. Evaluate a supported inference backend, temporal stability, edge preservation, compression robustness, quality gains, and added latency. A licensed pretrained model might avoid training from scratch, but would add dependencies and model storage.

The current shader is deterministic spatial image processing. It contains no neural model. A video-only AI stage still lacks game-engine motion vectors, geometry, and material data. Generative relighting could alter artwork or produce unstable detail, so it needs separate quality evaluation and a clear opt-in.

## Native PS5 research

Native integration belongs inside a game we own and develop through Sony's approved developer program. It requires authorized SDK access and platform hardware/testing. Approval is not guaranteed. Neither a repository nor developer access creates a universal patch for games written by other publishers.
