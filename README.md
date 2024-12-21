# cookiecutter

A cookiecutter for Billinge-group packages.

## Purpose

The purpose of cookiecutting is to standardize each repository on GitHub Actions, folder structures, documentation, syntax linting, and running unit tests with Pytest.

## Final checks and sign-off

This should be done only when the above steps are finished.

1. Make sure tests are all passing.
2. Make sure news is up to date so the changelog will reflect all changes. For the `cookierelease` activity make a `<branchname>.rst` file by copying `TEMPLATE.rst` in the news folder and under "fixed" put `Repo structure modified to the new diffpy standard`
3. Check the `README` and make sure that all parts have been filled in and all links resolve correctly.
4. Run through the documentation online and do the same, fix any last typos and make all the links work. To do this the documentation must have been correctly built on a merge to main and enabled on the github.io website. Instructions are [here](https://gitlab.thebillingegroup.com/resources/group-wiki/-/wikis/Maintaining-and-Deploying-Documentation).
5. When you are are happy to sign off on the release send a Slack message to Simon saying something like "`OK to release diffpy.<package-name>`"
6. Make sure that the codecov secret is set in the GH actions repository secrets. Probably Simon will have to do this [here](https://docs.codecov.com/docs/bitbucket-tutorial))

---

## Workflow for testing diffpy.utils files

We are using diffpy.utils as a template
for building the cookie cutter. To make sure the cookie cutter
is giving output that is consistent with diffpy utils please use
the following workflow:

### One-time Setup:

1. have all your code off a dir called `dev` or sthg like that
2. within `dev` create a scratch area called `scratch`
3. clone `diffpy.utils` in the scratch area of my hard-drive
4. cd to this directory.
5. create an env that has `cookiecutter` and `pexpect` in it.

## Running:

1. cd to `scratch/diffpy.utils`
1. run `python /path/to/your/local/cookiecutter_project/test_utils.py` which for me was `python ../../cookiecutter/test_utils.py`
1. This creates a new empty `diffpy.utils` under the old one using the current version of the cookie cutter (watch out, cookie cutter sometimes caches so if you make a change and it is not reflected, clear the cache).
1. cd to the directory that contains the file you are working on (for me it is `cd .` )
1. copy the file I am working on that was created by the cookiecutter to the current directory (for me it was `cp diffpy.utils/.pre-commit-config.yaml .`). It will overwrite the version that is already there.
1. run git diff
   This shows all the things you have to change in the cookiecutter to get it to create the file the same way as it is in `diffpy.utils`.
1. When it passes this "test" and the only things left are things we want, push a PR to `cookiecutter`
1. Paste screenshot of your terminal session showing the result of the copy and git diff.

## Why we decided to include test files in PyPI release

Billinge and Bob have agreed to include tests and the associated data files necessary for running these tests in the PyPI source distribution file. This decision is primarily aimed at enabling continuous integration (CI) on the Conda-Forge feedstock, which uses the PyPI release. You can monitor the CI progress by clicking on any of the PRs here: [Conda-Forge diffpy.utils feedstock](https://github.com/conda-forge/diffpy.utils-feedstock/pulls).

Conversely, we have opted not to include the documentation in the release package, as it is already accessible from the GitHub repository and does not serve a practical purpose in the distribution package itself.

Late update: Sep 10, 2024

### How to include/exclude files in PyPI source distribution with `MANIFEST.in`

If you use `graft` and add the folder path, you will include all files in the source distribution when executing `python -m build`.

```
graft src
graft tests
```

You can also specifically include files in the sdist:

```
include AUTHORS.txt LICENSE*.txt README.rst
```

Additionally, you can globally exclude static files:

```
global-exclude *.py[cod]  # Exclude all .pyc, .pyo, and .pyd files.
global-exclude .DS_Store  # Exclude Mac filesystem artifacts.
global-exclude __pycache__  # Exclude Python cache directories.
global-exclude .git*  # Exclude git files and directories.
```

Reference:

- [Setuptools - Controlling files in the distribution](https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html)

## GitHub Actions

### Difference between pull_request and pull_request_target

In the current CI setup checking for `news`, we use `pull_request_target` instead of `pull_request`.

```yaml
name: Check News Item

on:
  pull_request_target:
    branches:
      - main
```

- `pull_request`: This event configures the GITHUB_TOKEN with read-only permissions by default, especially when triggered by forks.
- `pull_request_target`: This event grants the GITHUB_TOKEN write permissions, enabling it to perform actions that modify the repository, such as posting comments, updating pull request statuses, or merging code.

Another key difference is that when using the `pull_request_target` event in GitHub Actions, the workflow configuration **must already be present** in the base branch at the time the pull request is opened or updated ([diffpy.snmf example PR](https://github.com/diffpy/diffpy.snmf/pull/79))

Reference:

- [GitHub docs](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request_target)

## Acknowledgements

Adapted from the NSLS-II scientific cookiecutter, thanks guys!:
https://github.com/nsls-ii/scientific-python-cookiecutter

Here are more in-depth docs for using this from NSLS-II, adapted for this repr:

**[Documentation](https://nsls-ii.github.io/scientific-python-cookiecutter/)**
