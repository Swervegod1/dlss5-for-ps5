# Security Policy

## Supported version

The current experimental `v0.1.x` line is the only version receiving fixes. This project is a browser-based external video enhancer and does not install software on a PS5.

## Reporting a vulnerability

Please do **not** publish credentials, private account details, access tokens, capture links, device serial numbers, or other sensitive information in a public issue.

For ordinary bugs that do not expose sensitive information, use the repository's **Bug report** issue form.

For a security-sensitive report, contact the repository owner privately through an appropriate GitHub contact channel before posting technical details publicly. Include:

- affected version/commit;
- browser and operating system;
- a concise impact description;
- minimal reproduction steps;
- whether the issue requires local user interaction;
- any proposed mitigation.

## Security boundaries

The application intentionally does not request microphone audio, does not contain telemetry, does not upload gameplay through an application service, and does not include HDCP/DRM bypass functionality. The optional Python launcher binds to loopback (`127.0.0.1`) and is intended only for local use.

Do not report expected browser permission prompts, normal PS Remote Play authentication handled by Sony's software, or the absence of protected-content capture as vulnerabilities.
