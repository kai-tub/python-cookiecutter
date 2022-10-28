# Auto scripts

These scripts are used to build the release automatically.
The [auto](https://intuit.github.io/auto/) tool bumps the tag version and publishes the release on GitHub.
The configuration file is the [.autorc](../.autorc) file in the root project folder.
During the release process, `auto` will trigger the [update_version](update_version.sh) script.
This script replaces the version specification in the `pyproject.toml` file with the newest release.
It will use PDM to bump the version inside the `pyproject.toml` file.

## Setup

To setup the CI/CD pipeline:
1. create an `.env` file that contains a GitHub token, the contents should look like this:
    - `GH_TOKEN=ghp_XXXXXXXX`
2. Be **very** sure that this file is in your `.gitignore` and not synced with git
3. Download [auto](https://intuit.github.io/auto/) and run:
    - `auto-create labels`
4. Add GitHub secrets under the `Security > Secrets > Actions` tab to the settings of the new repository:
    - `GH_Token`
    - `PYPI_PWD`
    - `PYPI_USER`
5. Change GitHub pages settings to use `gh-pages` branch from `/ (root)`!
    - If you change the root directory to the docs directory it will try to generate an empty Jekyll site.
5. Tag the latest release of your software, see [auto getting-started entry](https://intuit.github.io/auto/docs/welcome/getting-started#make-latest-release)
    - Don't forget to push with `--tags` flag!
