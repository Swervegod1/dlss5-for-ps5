#!/usr/bin/env python3
"""Build a small complete source preview, with per-file SHA-256 provenance."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build(output):
    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT))
    entries = {}
    for name in sorted(filter(None, paths)):
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Expected a regular tracked file: {name}")
        entries[name] = path.read_bytes()
    manifest = {
        "repository": "https://github.com/Swervegod1/dlss5-for-ps5",
        "source_revision": revision,
        "working_tree_dirty": dirty,
        "sha256": {name: hashlib.sha256(data).hexdigest() for name, data in entries.items()},
    }
    entries["BUILD_INFO.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    output = Path(output).resolve()
    if output.is_relative_to(ROOT) and output.relative_to(ROOT).as_posix() in entries:
        raise ValueError("The archive output cannot overwrite a tracked source file")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in entries.items():
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    print(f"Built {output.name}: {output.stat().st_size:,} bytes, {len(entries)} files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", default=str(ROOT / "dist" / "dlss5-for-ps5-preview.zip"))
    build(parser.parse_args().output)
