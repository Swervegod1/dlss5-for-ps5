# GitHub Packages / GHCR

This repository publishes a container image to GitHub Container Registry (GHCR):

`ghcr.io/swervegod1/dlss5-for-ps5:latest`

## Pull and run

```bash
docker pull ghcr.io/swervegod1/dlss5-for-ps5:latest
docker run --rm -p 127.0.0.1:8765:8080 ghcr.io/swervegod1/dlss5-for-ps5:latest
```

Then open:

`http://127.0.0.1:8765/`

Using localhost keeps browser capture APIs in a trusted local context. The application itself processes video locally in the browser.

## Local build fallback

If the registry requires authentication or the image is unavailable, download the source and build it locally:

```bash
docker build -t dlss5-for-ps5:local .
docker run --rm -p 127.0.0.1:8765:8080 dlss5-for-ps5:local
```

For the smallest disk footprint, open `index.html` directly; Docker and its base image are optional additional downloads. The [Docker port-publishing guide](https://docs.docker.com/engine/network/port-publishing/) explains why the loopback address is explicit.

## Versioned image

The first preview is also published as:

`ghcr.io/swervegod1/dlss5-for-ps5:0.1.0`

## Important

DLSS5 FOR PS5 is an unofficial experimental PC-side video enhancer for PS5 Remote Play and capture-card sources. It does not install on PS5, does not modify PS5 firmware or games, and does not implement NVIDIA DLSS 5.

## Preview build identity

`latest` and `0.1.0` are rolling experimental tags in the current publishing workflow. For reproducible container tests, record the pulled image digest. New release ZIPs include `BUILD_INFO.json` with the exact source commit and SHA-256 file hashes. The ZIP includes the linked documentation and preserves its directory structure.
