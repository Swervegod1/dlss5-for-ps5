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

The reviewed About description is:

> Unofficial PC-side PS5 Remote Play and capture-card video enhancer. WebGL 2 upscaling, sharpening and before/after comparison. Single HTML app, local processing, no model downloads. Experimental; not NVIDIA DLSS 5 or a PS5 installer.

The complete 20-topic list is in [DISCOVERY_TAGS.md](DISCOVERY_TAGS.md) and [repository-metadata.json](repository-metadata.json). These files document settings; they do not update GitHub by themselves.

### Apply the reviewed About settings

With [GitHub CLI](https://cli.github.com/) installed and signed in to the repository owner's account, run from the project folder:

```sh
python scripts/apply_github_metadata.py
python scripts/apply_github_metadata.py --apply
```

The first command previews the exact description and topic list. The second updates those two About fields and reads GitHub back to verify them. It uses your existing `gh` sign-in, stores no credentials, and leaves repository permissions unchanged. GitHub requires administration access for topic updates; the connected file-publishing tool does not expose this setting.

Alternatively, open the repository, click the gear beside **About**, enter the description and topics, and save. GitHub allows [up to 20 topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).

## Release and website status

The [v0.1.0 experimental release](https://github.com/Swervegod1/dlss5-for-ps5/releases/tag/v0.1.0) contains downloadable browser source. It is not a native console binary. No public app website has been deployed, so do not advertise an unverified Pages URL in About. The runtime works as a local file or through the loopback launcher.

The experimental release assets and container tags are rolling preview builds. `BUILD_INFO.json` in newly generated ZIPs records their exact source revision and SHA-256 file hashes. GitHub's automatically generated tag archives represent the original tag commit and can differ from updated attached assets.

Public visibility does not guarantee indexing or rankings. The owner has not selected an open-source license; see [LICENSE.md](LICENSE.md).
