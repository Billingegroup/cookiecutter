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

1. In your `dev` folder, fork and clone the package that you are preparing for release
4. cd into the top level directory of that project
2. `git pull upstream main` (make sure you are synchronized)
3. Double check that no bug-fix etc. pull-requests are waiting to be merged.  May as well get them merged before doing this. Check with Simon if not sure.
5. run the cookiecutter `cookiecutter https://github.com/billingegroup/cookiecutter`
6. Answer the questions as:
   1. (May occur if it is not the first time you have installed) Is it okay to delete: (y)
   2. github_org: diffpy (if diffpy project) or billingegroup
   3. keywords: current keywords in the `setup.py` or `pyproject.toml`
   4. project_name: name of project (e.g. `diffpy.pdfmorph`)
   5. package_dist_name: default
   6. package_dir_name: default
   7. minimum_python_version: 3.10 (default)
   8. maximum_python_version: 3.12 (default)
   9. is_boost_wrapper: no (in general)
7. You should have created a new directory tree with the cookiecutter version of all the files in a subdirectory with the name `<packagename>`, e.g., `diffpy.pdfmorph`.  Type `ls` to check it is there.
8. Open two terminals and display togther (e.g., above and below).  in one cd to `diffpy.<pkg>` (we will refer to this as the main directory) top level directory, in the other cd to the `diffpy.<pkg>/` directory created by cookiecutter (we will refer to this as the cookiecutter directory)
9. type `ls -als` in each case and compare the directory structures (ignore files at this point)
10. move the `.git` directory from the main directory to the cookiecutter directory. From the main directory type `mv -r .git diffpy.<package_name>`
11. copy the code from the old repo to the cookiecutter repo, without overwriting files in the destination (i.e., use `cp -n` or `cp --no-clobber`.  e.g., from the cookiecutter directory type `cp -n ../src .` if the old code is already in a directory `src`.
12. from the cookiecutter directory type `git status`.  You will see a list of files that have been modified, deleted or are untracked.
    1. add and commit each of the untracked files to the git repo.  Do it one at a time.
   
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



## Acknowledgements
Adapted from the NSLS-II scientific cookiecutter, thanks guys!:
https://github.com/nsls-ii/scientific-python-cookiecutter

Here are more in-depth docs for using this from NSLS-II, adapted for this repr:

**[Documentation](https://nsls-ii.github.io/scientific-python-cookiecutter/)**
