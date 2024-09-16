# cookiecutter
A cookiecutter for Billinge-group packages.

This repository contains a cookiecutter template for generating a group-standard
Python project complete with CI testing and documentation.

To do so, in a conda env that includes the cookiecutter package run:
```
cookiecutter https://github.com/billingegroup/cookiecutter
```

and follow the instructions.

## Workflow for releasing diffpy (and other group) packages using cookiecutter.

This may only be a one-time deal as we bring all our packages up to the same level of uniformity (summer 2024),
but these instructions will be left here in case we need to do this again in the future because of some
desired change in our package structure.

### DISCLAIMER
Do not delete/remove any files before confirming that it is absolutely not necessary. contact Simon (or Andrew) for assistance.
When copying over documentation files, make sure you include any additional package-specific information that may be in those files.
For instance, there may be a more verbose description of what the package does, or tutorial/example/utility files. DO NOT REMOVE THEM.

Finally take a glance at the API/documentation workflow below. This should be done as the last step after the `Pytest` tests are passing.

#### Pre-commit workflow

1. In your `dev` folder, fork and clone the package that you are preparing for release
2. `cd` into the top level directory of that project
3. `git pull upstream main` (make sure you are synchronized)
4. Double check that no bug-fix etc. pull-requests are waiting to be merged.  May as well get them merged before doing this. Check with Simon if not sure.
5. Before running the cookiecutter, we want to run `black` and `flake8` on the top level directory. Create a new branch and call it `black`. Preferrably, do not initialize pre-commit.
6. Edit the `pyproject.toml` so the section `[tools.black]` is consistent with `pyproject.toml` in `{{ cookiecutter.repo_name }}`.
7. Activate an env that contains black and run `black src` (note: some of the older packages do not have an `src` directory, so you may have to run black on a different directory).
8. If it runs successfully and makes changes, commit the changes (if your pre-commit is activated you can override it with `-n` to make these commits).
9. Let's run black on everything else. Run `black .` and commit any edits that are made.
19 Now, edit the `.flake8` file so it's consistent with `.flake8` in `{{ cookiecutter.repo_name }}`.
14. When this passes, open a PR and alert Simon.
15. When the PR is merged, update your main and create a new branch called `precommit`.
16. Make sure that `.pre-commit-config.yaml` is in your current directory. If it is not, copy it over from the cookiecutter.
17. In an env containing pre-commit, run `pre-commit run --all-files`
18. Make a new PR before doing any manual changes to files and have Simon merge it.  Make sure tests are passing first though
13. Fix any errors and make periodic commits.

20. Make necessary edits and make periodic commits to make review easier.
21. Once complete, open a PR and alert Simon. When merged, you can continue on with the cookiecutter.

#### Cookiecutter workflow

1. At this point, make sure your branch is fully sync'd. Now, from the cloned directory run the cookiecutter `cookiecutter https://github.com/billingegroup/cookiecutter`
2. Answer the questions as:
   1. (May occur if it is not the first time you have installed) Is it okay to delete: (y)
   2. github_org: diffpy (if diffpy project) or billingegroup
   3. keywords: current keywords in the `setup.py` or `pyproject.toml` in comma-separated string format, e.g., `diffpy, pdf, something, something else` (no quotes around it)
   4. project_name: name of project (e.g. `diffpy.pdfmorph`)
   5. package_dist_name: default
   6. package_dir_name: default
   7. minimum_python_version: 3.10 (default)
   8. maximum_python_version: 3.12 (default)
   9. is_boost_wrapper: no (in general, but if there are C++ extensions, this will be yes)
3. You should have created a new directory tree with the cookiecutter version of all the files in a subdirectory with the name `<package_name>`, e.g., `diffpy.pdfmorph`.  Type `ls` to check it is there.
4. cd to the `diffpy.<package_name>/` directory created by cookiecutter under the main directory (e.g., in our example `pwd` would return `~/dev/diffpy.pdfmorph/diffpy.pdfmorph`) (we will refer to this as the cookiecutter directory).
5. Type `ls -als` (if you have the alias, this is `ll`) compare the directory structures in this directory tree to that in the original repo to see what is different (ignore files at this point).  Nothing to do here, just get familiar with the differences.
6. Move the `.git` directory from the main directory to the cookiecutter directory. From the main directory type `mv ../.git .`.
7. Create a new branch for all the changes, e.g., `git checkout -b cookierelease`.
8. If the package has C extensions or is a gui package, look into `.github/workflows` and change `c_extension` or `headless` parameters to `true`.
9. Copy the code from the old repo to the cookiecutter repo, without overwriting files in the destination (i.e., use `cp -n` or `cp --no-clobber`.  e.g., from the cookiecutter directory where you currently are, type `cp -n -r ../src .` if the old code is already in a directory `src`.  If there is no src directory, it will be something like `cp -n -r ../diffpy ./src`.
10. From the cookiecutter directory type `git status`.  You will see a list of files that have been modified, deleted or are untracked.  Untracked files are in the cookiecutter but not in the original repo, deleted files are in the original but haven't been moved over, and modified files are in both but have been changed.
11. Let's now copy over any documentation, similar to what we did with the src files.  We want to copy over everything in the `doc/<path>/source` file from the old repo to the `doc/source` file in the new repo.  In some old pacakges, `<path>` will be something like `manual` and in others it will just not exist.
    1. If you see this extra `manual` directory, go to your cookiecutter directory. Then run `cp -n -r ../doc/manual/source/* ./doc/source`.
    2. Make sure that if files are moved to a different path compared to root, you must check that the files paths referenced within the file are updated. The best way to do this is to open the project in PyCharm and do a global search (ctrl + shift + f) for `../` or `..` and look at all relative path instances.
12. Now we will work on correcting all the things that are wrong.
    1. Add and commit each of the untracked files to the git repo.  These are in cookiecutter but not in the original repo, so can simply be "git added".  Do it one (or a few) at a time to make it easier to rewind by having multiple commits.
    2. Make a PR of your `cookierelease` branch by pushing your fork and opening a PR.
    3. Files showing as deleted in a `git status` are in the old repo but not in the new cookiecutter.  We took care of most these by moving over the src tree, but let's do the rest now.  Go down the list and for <filename> in the `git status` "delete" files type `cp -n ../<filepath>/<filename> ./<target_filepath>`. Note that, generally, `<filepath>` and `<target_filepath>` will be the same, but may differ in cases such as `/doc/manual/source` and `/doc/source` respectively. If there are files there we don't want, don't move them over. Whenever files are copied over using the `-n` command, you may delete them in the main repository to keep your file-tree clean.
    4. Files that have been modified exist in both places and need to be merged manually.  Do these one at a time. First open the file in pycharm, then select `Git|current file|show diff` and the differences will show up.  Select anything you want to inherit from the original file.   In many cases we don't want to bring over things that have been polished in the cookiecutter, so you are mostly looking for code specific things, such as extended descriptions of the package in README and things like that.
    5. Any files that we moved over from the old place, but put into a new location in the new repo, we need to delete them from git.  For example, files that were in `doc/manual/source/` in the old repo but are not `doc/source` we correct by typing `git add doc/manual/source`.
13. Run pytest `python -m pytest` to make sure everything is working. There should be no errors if all tests passed previously when you were working on pre-commit. You may encounter deprecation warnings. There might be several possibilities:
    1. If you see numpy deprecation warnings, we won't clean up these deprecations now. Pin numpy to 1.x for now to get tests to pass. Do code fixes separate from cookiecuttering. Remember to add it to Github issue.
    2. Most `pkg_resources` depreation warnings will be fixed by cookiecutter, but if you are in a diffpy package using unittests and see this warning you can fix them by replace `from pkg_resources import resource_filename` with `from importlib import resources` and change `path = resource_filename(__name__, p)` to `path = str(resources.files(__name__).joinpath(p))`. If you see `collected 0 items no tests ran` you might want to rename testing files as `test_*.py`. Refer to the [migration guide](https://importlib-resources.readthedocs.io/en/latest/migration.html).

#### API workflow
This should be done only when the above steps are finished.

When you see files with `..automodule::` within them, these are API documentation. However, these are not populated. We will populate them using our release scripts.
1. Make sure you have our release scripts repository. Go to `dev` and running `git clone https://github.com/Billingegroup/release-scripts.git`.
2. Enter your cookiecutter package directory. For example, I would run `cd ./diffpy.pdfmorph/diffpy.pdfmorph`.
3. Build the package using `python -m build`. You may have to install `python-build` first.
4. Get the path of the package directory proper. In the case of `diffpy.pdfmorph`, this is `./src/diffpy/pdfmorph`. In general, for `a.b.c`, this is `./src/a/b/c`.
5. Run the API script. This is done by running `python <path_to_auto_api> <package_name> <path_to_package_proper> <path_to_api_directory>`.
   1. If you have followed the steps above, the command is `python ../../release-scripts/auto_api.py <package_name> <path_to_package_proper> ./doc/source/api`.

Make sure you build the documentation by going to `/doc` and running `make html`.
The error "No module named" (`e.g. WARNING: autodoc: failed to import module 'tools' from module 'diffpy.pdfmorph'; the following exception was raised: No module named 'diffpy.utils'`) can be resolved by adding `autodoc_mock_imports = [<pkg>]` to your `conf.py` right under imports. This file is located in `/doc/source/conf.py`.
In the case of `PDFmorph`, this was done by adding `autodoc_mock_imports = ["diffpy.utils",]`.

Congratulations! You may now commit the changes made by `auto_api.py` (and yourself) and push this commit to the cloud!
Make a PR! It will be merged, trust!

## Final checks and sign-off
This should be done only when the above steps are finished.

1. make sure tests are all passing
2. Make sure news is up to date so the changelog will reflect all changes.  For the `cookierelease` activity make a `<branchname>.rst` file by copying `TEMPLATE.rst` in the news folder and under "fixed" put `Repo structure modified to the new diffpy standard`
3. Check the `README` and make sure that all parts have been filled in and all links resolve correctly.
4. Run through the documentation online and do the same, fix any last typos and make all the links work.  To do this the documentation must have been correctly built on a merge to main and enabled on the github.io website.  Instructions are [here](https://gitlab.thebillingegroup.com/resources/group-wiki/-/wikis/Maintaining-and-Deploying-Documentation)
5. When you are are happy to sign off on the release send a Slack message to Simon saying something like "`OK to release diffpy.<package-name>`"
6. Make sure that the codecov secret is set in the GH actions repository secrets.  Probably Simon will have to do this [here](https://docs.codecov.com/docs/bitbucket-tutorial))
## Workflow for testing diffpy.utils files
We are using diffpy.utils as a template
for building the cookie cutter.  To make sure the cookie cutter
is giving output that is consistent with diffpy utils please use
the following workflow:

### One-time Setup:
1. have all your code off a dir called `dev` or sthg like that
2. within `dev` create a scratch area called `scratch`
1. clone `diffpy.utils` in the scratch area of my hard-drive
1. cd to this directory.
1. create an env that has `cookiecutter` and `pexpect` in it.

## Running:
1. cd to `scratch/diffpy.utils`
1. run `python /path/to/your/local/cookiecutter_project/test_utils.py`  which for me was `python ../../cookiecutter/test_utils.py`
1. This creates a new empty `diffpy.utils` under the old one using the current version of the cookie cutter (watch out, cookie cutter sometimes caches so if you make a change and it is not reflected, clear the cache).
1. cd to the directory that contains the file you are working on (for me it is `cd .` )
1. copy the file I am working on that was created by the cookiecutter to the current directory (for me it was `cp diffpy.utils/.pre-commit-config.yaml .`).  It will overwrite the version that is already there.
1. run git diff
This shows all the things you have to change in the cookiecutter to get it to create the file the same way as it is in `diffpy.utils`.
2. When it passes this "test" and the only things left are things we want, push a PR to `cookiecutter`
3. Paste screenshot of your terminal session showing the result of the copy and git diff.

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
