# GitHub Packages / GHCR

This repository publishes a container image to GitHub Container Registry (GHCR):

`ghcr.io/swervegod1/dlss5-for-ps5:latest`

## Pull and run

```bash
docker pull ghcr.io/swervegod1/dlss5-for-ps5:latest
docker run --rm -p 8765:8080 ghcr.io/swervegod1/dlss5-for-ps5:latest
```

Then open:

`http://127.0.0.1:8765/`

Using localhost keeps browser capture APIs in a trusted local context. The application itself processes video locally in the browser.

## Versioned image

The first preview is also published as:

`ghcr.io/swervegod1/dlss5-for-ps5:0.1.0`

## Important

DLSS5 FOR PS5 is an unofficial experimental PC-side video enhancer for PS5 Remote Play and capture-card sources. It does not install on PS5, does not modify PS5 firmware or games, and does not implement NVIDIA DLSS 5.
