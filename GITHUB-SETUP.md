# GitHub project maintenance

The public repository is **[Swervegod1/dlss5-for-ps5](https://github.com/Swervegod1/dlss5-for-ps5)**. Keep the experimental status and unverified live-PS5 compatibility prominent when updating it.

## Download and run

Choose **Code → Download ZIP**, extract the project, and open `index.html` in desktop Chrome or Edge. The [README](README.md) contains Remote Play setup, capture-card instructions, and troubleshooting. A GitHub source-code page does not execute the app.

## Update files through GitHub

Open the file to edit, use GitHub's edit action, review the change, and commit it. Use **Add file → Upload files** for new files. Keep the root app and its supporting documents together; avoid uploading archives instead of source. Preserve the tests and `.github/workflows/check.yml` when replacing project files.

GitHub's official [file upload guide](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) explains the upload interface.

## Optional local Git workflow

With Git already installed, clone the existing repository:

```sh
git clone https://github.com/Swervegod1/dlss5-for-ps5.git
cd dlss5-for-ps5
```

Edit the files, run the checks, review the diff, then commit and push using your normal authenticated Git setup:

```sh
python tests/check_project.py
git diff
git add index.html README.md
git commit -m "Update video enhancer and documentation"
git push origin main
```

Adjust the explicit `git add` paths to match your changes. Do not force-push or overwrite unrelated work. Never put passwords or access tokens into source files.

## Description and topics

The repository About description is:

> DLSS5 FOR PS5: unofficial PC-side PS5 Remote Play and capture-card video enhancer. Lightweight WebGL 2 upscaling, sharpening, before/after comparison and local processing. No model downloads. Experimental prototype; not NVIDIA DLSS 5 or native PS5 software.

The complete suggested topic list is in [repository-metadata.json](repository-metadata.json). Those suggestions do not automatically update GitHub About settings. The owner can add them through the About settings; the publishing connection exposes file writes but does not expose topic edits.

The project has no deployed website, release binary, or native console installer. Its HTML includes search/social metadata for any future requested web deployment. Public repository visibility does not guarantee search indexing or rankings. The owner has not yet selected an open-source license; see [LICENSE.md](LICENSE.md).
