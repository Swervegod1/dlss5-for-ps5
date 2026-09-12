# DLSS5 FOR PS5

**Unofficial PS5 Remote Play video enhancer for PC · WebGL upscaling and sharpening · v0.1**

[Download ZIP](https://github.com/Swervegod1/dlss5-for-ps5/archive/refs/heads/main.zip) · [PS5 setup](#connect-a-ps5-with-remote-play) · [Troubleshooting](#troubleshooting) · [Validation report](VALIDATION.md)

A tiny, independent **PC-side video enhancement prototype** for PS5 gameplay viewed through Remote Play or a capture card. The complete app is in `index.html`. No build, installer, account, model download, or package dependencies are required for the app itself.

**Status: v0.1, experimental. It is not a PS5 executable or a DLSS 5 implementation.** It processes video that has already been rendered. It cannot change a game's rendering, raise PS5 engine FPS, generate extra frames, or reconstruct DLSS 5's AI lighting. Live PS5 capture, browser behavior, picture quality, and latency need testing on actual equipment.

The title is the project name requested by its owner. **This repository does not contain NVIDIA DLSS 5, Sony PSSR, or a native PS5 installer.**

## PS5 video enhancement: quick start

1. Select **Code → Download ZIP** on [this repository](https://github.com/Swervegod1/dlss5-for-ps5), or use the Download ZIP link above. Extract the ZIP.
2. Open `index.html` in desktop Chrome or Edge. Open the downloaded file, rather than its preview on GitHub or in a messaging app.
3. Click **Try demo** to see a moving synthetic test scene.
4. Change **Sharpness**, **Output height**, and **Preview mode**. Use **Before / after** to compare the same input frame.
5. Click **Check renderer** to run checks through the browser's actual graphics shader.

The demo is synthetic and does not demonstrate PS5 compatibility or measured quality gains.

## Connect a PS5 with Remote Play

This is the starting route if you do not own a capture card.

### Requirements

- A PS5 or PS5 Pro, a compatible controller, and your own PlayStation account.
- A computer that meets Sony's current Remote Play requirements. The [official Windows guide](https://remoteplay.dl.playstation.net/remoteplay/lang/en/1100001.html) lists Windows 10/11, 2 GB RAM, and at least 100 MB of storage for Remote Play; dependencies and updates can use more space.
- Desktop Chrome or Edge with WebGL 2 and graphics acceleration enabled.
- A stable network. Wired Ethernet is a useful starting point if you already have it.

### Setup

1. Download and install **PS Remote Play** from [Sony's official guide](https://remoteplay.dl.playstation.net/remoteplay/lang/en/1100001.html).
2. On PS5, enable **Settings → System → Remote Play → Enable Remote Play**.
3. Open Sony's app, sign in yourself, connect your controller, and connect to the console. Complete any requested account sign-in in Sony's app; DLSS5 FOR PS5 never asks for a password.
4. Confirm that the game works normally in Remote Play first. For this initial SDR prototype, disable HDR in the Remote Play client.
5. Open `index.html`, then select **Share Remote Play window**.
6. In the browser's source picker, choose **only the Remote Play window**. Do not choose DLSS5 FOR PS5 or a screen containing its preview, which creates a feedback loop.
7. Keep Remote Play visible and unminimized. Some combinations of operating system and capture method stop delivering frames when the source is minimized or fully covered.
8. Start with **Balanced**, **1080p**, and **Before / after**. Choose **Enhanced only** for an unobstructed preview.
9. Keep audio and controller input with Remote Play. This app requests no audio and implements no controller forwarding. If input stops, give Remote Play focus or return to Sony's original view. A second monitor helps keep the source visible while displaying the enhanced preview.
10. Click **Stop source** to release the capture, or use the browser's stop-sharing control.

### Show the processed picture on a TV

Connect the **computer's video output** to the TV and display DLSS5 FOR PS5 full screen there. The TV needs to show the computer's input. The enhanced picture does not travel back into the console and does not appear in the PS5's own HDMI output.

## Use an HDMI capture card instead

This route requires separate hardware that this project does not provide.

1. Connect **PS5 HDMI output → capture-card HDMI input**, then connect the card's USB output to the computer.
2. Supply SDR gameplay at a resolution and frame rate the card supports. A normal laptop HDMI connector is usually an output, not a capture input.
3. Click **Capture card**, then **Refresh devices**.
4. If names are hidden, **Reveal device names** requests browser camera permission, briefly opens the default video device (possibly a webcam), and immediately stops it. Nothing is recorded. Then select your capture card by name.
5. Click **Connect selected device**. The browser treats USB video capture cards as cameras. The app requests that exact device and requests no microphone/audio access.
6. Keep audio and controls in your existing console setup. The preview itself is silent.

This app cannot decode an HDCP-protected HDMI signal, DRM-protected media, or streaming-service video. Use the card manufacturer's supported gameplay configuration; there is no decryption or bypass code here. Compatibility differs by card, driver, browser, and operating system. If processing delay is distracting, play through the card's direct passthrough; that picture will not include this app's filter.

## If double-clicking the file cannot start capture

Browser capture APIs need a supported secure context and a click from the user. Browser policy can restrict local files. An optional localhost launcher is included, using an **existing Python 3 installation**:

```sh
python serve.py
```

On Windows, `py serve.py` may be the available command; on macOS/Linux, try `python3 serve.py`. Open the localhost address printed in the terminal. Press Ctrl+C to stop. The launcher serves only this HTML file on `127.0.0.1`; it does not expose your other files or listen on your network.

You can also use Python's built-in server from this project folder:

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8765/index.html`. The built-in server serves the whole current folder; prefer `serve.py` for the restricted route. No Python is required when opening the HTML directly works.

## What the controls mean

| Control | Behavior |
| --- | --- |
| Output height | Sets the output buffer to 720, 1080, 1440, or 2160 pixels high while retaining the source aspect ratio. This does not recover native 4K detail. |
| Bicubic | A 16-sample spatial interpolation filter that can smooth enlarged contours. It is not temporal or AI super-resolution. |
| Bilinear | A lighter interpolation option. Try this and 720p if the preview cannot keep up. |
| Sharpness | Adds a spatial detail term, gated by local contrast and clamped to neighborhood color bounds to limit halos. Strong settings can amplify compression artifacts. |
| Contrast | Adds a small global contrast adjustment. Zero preserves the default contrast; increases can clip dark or bright detail. |
| Before / after | Compares bilinear original video with the enhanced filter using the same source frame. |
| Preview updates / sec | Counts redraws made by this app. It is not measured PS5 FPS or end-to-end latency. |
| Open clip | Loads a local browser-decodable video through a blob URL. Clips loop silently and are never uploaded. |
| Check renderer | Tests flat colors, image orientation, sharpening, and graphics errors using synthetic inputs. |

## Storage, privacy, and limits

- The app is a single small text file. Exact release sizes and verification status are in [VALIDATION.md](VALIDATION.md).
- There are **no model weights, game assets, third-party JavaScript packages, telemetry, account fields, or recording output**.
- The app makes no network requests to process video. The browser's capture picker and Sony's Remote Play connection operate separately.
- Capture and decoding require RAM and GPU memory. A 3840 × 2160 RGBA buffer alone is roughly 32 MiB; multiple browser/decoder buffers can use substantially more. Small disk size does not imply low GPU load.
- SDR is the supported prototype format. HDR tone mapping, wide-gamut accuracy, 4K throughput, VRR, frame pacing, and audio synchronization are unvalidated.
- Capturing, decoding, filtering, and displaying add delay. A processed Remote Play stream may look worse or respond more slowly than the PS5's direct HDMI output.
- The app sees only final video pixels. It has no game-engine motion vectors, depth buffers, textures, or lighting data.
- A connection is never started automatically. **Stop source**, stopping browser sharing, navigating away, or closing the page releases the source tracks.

## Troubleshooting

| Problem | Action |
| --- | --- |
| Capture button says unavailable | Use desktop Chrome/Edge, open the downloaded file outside an attachment preview, or use `serve.py`. |
| Browser or organization policy blocks capture | Use an allowed browser/context or your original Remote Play view. This project does not bypass policy restrictions. |
| Black or frozen Remote Play preview | Keep the selected window visible and unminimized. Confirm it plays correctly in Sony's app. Try a local clip to separate capture problems from filtering problems. |
| No named capture devices | Use **Reveal device names**, then select the card. Close other programs that may have exclusive use of it. |
| Source is protected or unsupported | Use an unprotected, card-supported gameplay signal. Protected media cannot be processed by this app. |
| Slow preview | Lower output to 720p/1080p, switch to Bilinear, close GPU-heavy apps, and compare with the original Remote Play view. |
| Harsh edges or flickering detail | Reduce Sharpness or select Gentle cleanup. Video filters cannot restore detail discarded by stream compression. |
| No audio or controller response in this page | Expected: audio and input remain in Remote Play or your console setup. Give Remote Play focus as needed. |
| Graphics context lost | Reload the file and choose a lower output resolution. |

## Frequently asked questions

### Can I install DLSS 5 directly on PS5?

This project runs on a computer and processes captured PS5 video. It provides no console installer or NVIDIA DLSS binaries.

### Does it improve PS5 FPS or add ray tracing?

No. It adjusts the displayed video after the console renders it. PS5 game performance and lighting remain determined by the game and console.

### Can I use it without an NVIDIA RTX graphics card?

The app uses WebGL 2 rather than NVIDIA-specific libraries. Hardware compatibility and throughput depend on the browser and GPU; check the renderer and start at 720p or 1080p.

### How much storage does the enhancer use?

The app is approximately 33 KB of HTML, JavaScript, and shader source, with no AI model downloads. Remote Play, the browser, and runtime memory require additional space.

### Is 4K output the same as native 4K gameplay?

No. Selecting 2160p enlarges the output buffer; it does not recover missing native detail. Sustained 4K frame rate and quality are not verified.

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | Complete app, styling, JavaScript, and GLSL shader source. |
| `serve.py` | Optional localhost launcher using the Python standard library. |
| `README.md` | Setup, usage, troubleshooting, and limits. |
| `VALIDATION.md` | Checks performed and checks still required. |
| `GITHUB-SETUP.md` | Instructions to publish the project to your own GitHub repository. |
| `ROADMAP.md` | Hardware testing and future AI-development stages. |
| `CHANGELOG.md` | Version history and release limitations. |
| `SEO.md` | Search metadata, GitHub description, and repository topics. |
| `repository-metadata.json` | Final public-repository name, owner, description, and topics. |
| `LICENSE.md` | Current licensing status; no open-source grant selected. |
| `CONTRIBUTING.md` | Useful compatibility reports and contribution scope. |
| `tests/check_project.py` | Source integrity and local-server checks. |
| `tests/offline_shader_check.py` | Optional Linux EGL numerical shader check. |
| `.github/workflows/check.yml` | GitHub Actions source/launcher check workflow. |
| `.gitignore` | Keeps temporary files and common secret-file names out of Git. |

See [LICENSE.md](LICENSE.md). No open-source license has been selected by the owner yet. Do not assume that a public repository grants permission to redistribute or relicense it. Choose a license deliberately before accepting outside contributions.

## Development

The application is intentionally contained in one file. Edit its CSS, JavaScript, or GLSL and reload. `serve.py` serves the current contents on each request without caching. To check Python syntax without generating bytecode:

```sh
python -c "import ast,pathlib; ast.parse(pathlib.Path('serve.py').read_text()); print('Python syntax OK')"
```

Run `python tests/check_project.py` for source and launcher checks. On Linux with EGL/GLES 3 available, `python tests/offline_shader_check.py` checks the shader independently. Use **Check renderer** and the hardware checklist in [VALIDATION.md](VALIDATION.md) before advertising compatibility. Do not represent upscaled buffer dimensions or browser redraws as native console resolution or increased game FPS.

For software inside a PS5 game we develop, the legitimate route is [PlayStation Partners](https://sonyinteractive.com/en/news/blog/showing-your-game-to-playstation/). Access to development tools would not turn this browser app into a system-wide enhancer for other publishers' games. PS5 Pro also has Sony's [PSSR in supported games](https://www.playstation.com/en-us/ps5/ps5-pro/).

Independent project. PlayStation, PS5, PSSR, NVIDIA, and DLSS are their respective owners' names; there is no affiliation or endorsement.
