# Contributing and reporting results

This is an experimental external video filter. Discuss changes with the owner before contributing because an open-source license has not yet been selected.

For a useful compatibility report, provide:

- Computer OS and browser version.
- GPU model, PS5 or PS5 Pro, game, and display resolution.
- Remote Play, local clip, or capture-card source; card model where applicable.
- Input dimensions, output buffer dimensions, selected preset/filter, and renderer-check results.
- Exact steps, expected result, and observed behavior.
- Whether the unprocessed source works and whether focus/minimizing changes the result.

Do not include account credentials, serial numbers, private clips, or unrelated desktop content. Share only footage you are authorized to share.

Keep source changes small and preserve: no telemetry, no automatic capture, no audio requests, clean source release, aspect-ratio preservation, and explicit distinction between video processing and console rendering. Test local clip playback and capture lifecycle on actual devices before claiming support.

Run `python tests/check_project.py` for source and local-server checks. Use **Check renderer** in the app for shader checks on the target browser. Neither check establishes PS5 compatibility.
