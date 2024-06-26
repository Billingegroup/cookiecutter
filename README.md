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
2. `git pull upstream main` (make sure you are synchronized)
3. Double check that no bug-fix etc. pull-requests are waiting to be merged.  May as well get them
   merged before doing this
4. cd into the top level directory or that project
5. `mamba activate cookiecutter` (activate your cookiecutter conda env, changing this command as needed)
6. run the cookiecutter `cookiecutter https://github.com/billingegroup/cookiecutter`
7. Answer the questions as:
   1. this
   2. that
   

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
