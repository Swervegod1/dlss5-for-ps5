# Validation report — v0.1.0

Prepared September 12, 2026. This is a source/prototype validation report, not a PS5 compatibility certification.

## Completed checks

| Check | Result | What it establishes |
| --- | --- | --- |
| JavaScript syntax with Node `--check` | Passed | The embedded script parses. It does not establish DOM behavior or capture compatibility. |
| Python syntax | Passed | Launcher and check scripts parse. |
| HTML IDs and label references | Passed | No duplicate IDs or broken static control/label references found. |
| Relative documentation links | Passed in final package check | Referenced local Markdown files exist. |
| GitHub Actions source/launcher workflow | Passed on the initial publication commit | GitHub ran the source/launcher checks successfully; this is not a browser or PS5 test. |
| Localhost launcher | Passed | Serves the exact HTML for `/` and `/index.html`; rejects unrelated paths, traversal-like paths, and unrecognized Host headers. |
| GLSL ES 3 shader compilation/linking | Passed | The actual vertex and fragment shader text compiles and links in a standalone GLES context. |
| Shader flat-color preservation | Passed | A constant RGB input remains constant within test tolerance. |
| Shader sharpening and bounds | Passed | A synthetic edge ramp changes with sharpening and stays within its tested source bounds. |
| GLES error check | Passed | No GL error was observed during the standalone numerical shader test. |

Offline shader checks used **Mesa llvmpipe (LLVM 20.1.2, 256 bits)**, a software renderer. They do not measure physical-GPU performance. The test loads shader strings into GLES; it does not run the browser page or emulate a PS5.

Run source/launcher checks with:

```sh
python tests/check_project.py
```

Node.js is optional for users. If Node is missing, this check explicitly skips its JavaScript syntax subtest. The app itself does not depend on Node or Python.

Optional Linux shader check, requiring a system EGL library and surfaceless GLES 3 driver:

```sh
python tests/offline_shader_check.py
```

GitHub Actions passed on initial publication commit `f1344ba41583a2216395611f38a774c09767f6bb`: [verified workflow run](https://github.com/Swervegod1/dlss5-for-ps5/actions/runs/34693494275). Future commits trigger their own checks. All 15 published project files were verified against their local Git blob hashes after publication.

## Checks not completed

- **Browser visual and interaction testing:** the available cloud browser blocked local preview URLs under its security policy. No browser-rendered screenshot or click-through validation was obtained.
- **The in-app Check renderer button:** implemented, but not run in a browser here. Its orientation check specifically needs browser execution because browser texture uploads flip source rows.
- **PS5 / PS5 Pro integration:** no console or authenticated Remote Play app was attached.
- **Capture-card compatibility:** no USB capture device was attached.
- **Local clip and live video playback:** need target-browser tests, including format support and blocked-source behavior.
- **Latency, CPU/GPU utilization, RAM, HDR, sustained resolution/frame rate, and picture-quality improvement:** unmeasured.

## Minimum hardware acceptance checklist

- [ ] Open `index.html` in desktop Chrome/Edge and run **Try demo**.
- [ ] Run **Check renderer**; all results must pass.
- [ ] Verify that Before/after, Original only, Enhanced only, presets, sharpening, output height, and full screen work.
- [ ] Open a local H.264 MP4 and test pause, resume, switching sources, and stop.
- [ ] Start Remote Play normally, then share only its window.
- [ ] Confirm correct picture orientation and aspect ratio, live motion, and working source audio/controller input.
- [ ] Cancel a capture prompt; the existing source should stay usable.
- [ ] Stop sharing through the browser; the app should release the source.
- [ ] Test Stop source and closing the page; the capture indicator should disappear.
- [ ] If using a capture card, verify exact-device selection and that temporary device-name permission leaves no stream running.
- [ ] Compare quality and delay with the unprocessed source in several games before describing the setup as useful or compatible.

## Size

The runtime is the single `index.html` file, roughly **33 KB** before compression. The project also contains text documentation, an optional Python launcher, and small verification scripts. There are no model downloads or installed game copies. Browser/decoder/GPU memory and Remote Play installation space are additional.
