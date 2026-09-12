# DLSS5 FOR PS5 v0.1.0 — Experimental Preview

The first packaged preview of **DLSS5 FOR PS5**, an unofficial PC-side video enhancement prototype for PS5 Remote Play and capture-card video.

## What is included

- WebGL 2 video upscaling with bicubic or bilinear filtering
- Adjustable sharpening and contrast
- Before/after split comparison
- 720p, 1080p, 1440p, and experimental 2160p output buffers
- Remote Play window sharing
- Capture-card video input through the browser
- Local video-file testing
- Built-in renderer/self-check tools
- Lightweight single-page implementation with no model downloads
- Docker/GHCR container image for easy local launch

## Run locally

### Simple Python launcher

```bash
python serve.py
```

Then open `http://127.0.0.1:8765/`.

### GitHub Container Registry

```bash
docker pull ghcr.io/swervegod1/dlss5-for-ps5:0.1.0
docker run --rm -p 8765:8080 ghcr.io/swervegod1/dlss5-for-ps5:0.1.0
```

Then open `http://127.0.0.1:8765/`.

## Scope and limitations

This project is **not NVIDIA DLSS 5**, is not affiliated with NVIDIA or Sony, and does not install software on a PS5. It processes an external video feed on the user's computer. It does not generate frames, alter PS5 games or firmware, or guarantee higher FPS, lower latency, or recovered source detail.

This release is marked **pre-release** because live PS5 compatibility, capture-card behavior, latency, and image-quality gains still require broader hardware testing.
