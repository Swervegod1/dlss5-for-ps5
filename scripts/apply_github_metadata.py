#!/usr/bin/env python3
"""Preview or apply the reviewed GitHub About description and 20 topics using gh."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = "Swervegod1/dlss5-for-ps5"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write the description/topics using your existing GitHub CLI sign-in")
    args = parser.parse_args()
    metadata = json.loads((ROOT / "repository-metadata.json").read_text())
    topics, description = metadata["topics"], metadata["description"]
    if not 1 <= len(topics) <= 20 or len(set(topics)) != len(topics):
        parser.error("Expected 1–20 unique topics")
    if any(not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,49}", topic) for topic in topics):
        parser.error("Topics must use lowercase letters, numbers, and hyphens; maximum 50 characters")
    print(json.dumps({"repository": REPO, "description": description, "topics": topics}, indent=2))
    if not args.apply:
        print("Preview only. Run again with --apply to update these two GitHub About fields.")
        return
    if not shutil.which("gh"):
        parser.error("Install GitHub CLI from https://cli.github.com and sign in with gh auth login first")

    def api(method, path, payload=None):
        command = ["gh", "api", "--method", method, path]
        if payload is not None:
            command += ["--input", "-"]
        result = subprocess.run(command, input=json.dumps(payload) if payload is not None else None,
                                text=True, capture_output=True)
        if result.returncode:
            raise SystemExit("GitHub rejected the metadata request. Check gh auth status and repository administration access. No credentials are stored by this script.")
        return json.loads(result.stdout)

    # Only these two About fields are changed; no repository access settings are changed.
    api("PUT", f"repos/{REPO}/topics", {"names": topics})
    api("PATCH", f"repos/{REPO}", {"description": description})
    current = api("GET", f"repos/{REPO}")
    if sorted(current.get("topics", [])) != sorted(topics) or current.get("description") != description:
        raise SystemExit("The requested metadata could not be verified; inspect GitHub About before retrying.")
    print("Verified: description and all 20 GitHub topics are live.")


if __name__ == "__main__":
    main()
