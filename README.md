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
8. Open two terminals and displace togther.  in one cd to `diffpy.<pkg>` (we will refer to this as the main directory) top level directory, in the other cd to the `diffpy.<pkg>/` directory created by cookiecutter (we will refer to this as the cookiecutter directory)
9. type `ls` in each case and compare the directory structures (ignore files at this point)
   1. In the cookiecutter directories, `ls src/<path>` for each sub-directory all the way        down to `tests`.  Each time also do the same from the main directory.  Ignore the          files for now, but if a subdirectory is missing in main but is present in      cookiecutter, add that subdirectory in main.
   2. do as above in the `doc` tree, `ls doc/<path>` recursing down until you get `api`
10. The new structure as all the code under a `./src/diffpy/<package_name>` directory.  Some of the old projects have the structure `/diffpy/<package_name>`.  If this applies to you, move the `diffy` tree over to your new `src` directory. e.g., from main dir type `mv diffpy src`.
11. for every file moved in this way, search it for relative file-paths in the file and update them to account for the new src top-level directory
12. do a `git commit` and create a PR
13. redo 10-12 for the `doc` tree.  In this case the new structure has no `manual` directory but old projects did, also we may have a new `api` directory.
14. e.g., to copy everything from `./manual/source` to `./source` use `cp -r ./manual/source .`.  Then delete `manual/source`.  `rm -r ./manual/source`.  Be careful not to delete other files in there.
   
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
