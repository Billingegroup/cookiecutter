:tocdepth: -1

.. index:: cookiecutter_guide
    
==================================
How to migrate an existing package
==================================

The following creates and activates a new environment named ``cookiecutter_env`` ::

        conda create -n cookiecutter_env python=3.13

Activate the environment ::

        conda activate cookiecutter_env

Install packages ::

        pip install cookiecutter black pre-commit

Overview
--------

The cookiecutting is divided into three main sections:

1. Pre-commit workflow: Use ``black`` and ``pre-commit`` to standardize line lengths and remove flake8 errors.

2. Cookiecutting workflow: Use the Cookiecutter project setup and move files from an older to a new structure with Pytest passing.

3. API documentation build workflow: Use a script to build and host API documentation.

WARNINGS
--------

- Do not delete/remove any files before confirming that it is absolutely not necessary. Create an issue or contact the maintainer for assistance.

- When copying over documentation files, make sure you include any additional package-specific information that may be in those files.

- For instance, there may be a more verbose description of what the package does, or tutorial/example/utility files.


1. Pre-commit workflow
----------------------

1. In your ``dev`` folder, fork and clone the package

2. ``cd`` into the top level directory of that project.

3. Type ``git pull upstream main`` to sync with the main branch.

4. Double check that no bug-fix etc. pull-requests are waiting to be merged. Check with Simon if not sure.

5. Create a new branch called ``black``.

6. Create ``pyproject.toml``. Copy and paste the ``[tools.black]`` and ``[tool.codespell]`` sections from ``pyproject.toml`` in the ``{{ cookiecutter.repo_name }}`` folder path.

7. Run ``black src`` (note: some of the older packages do not have an ``src`` directory, so you may have to run black on a different directory).

8. Commit the automatic changes by ``black``.

9. Run ``black .`` and create a PR into ``main``. Follow the group's GitHub workflow tutorial on GitLab.

10. After the ``black`` branch has been merged, run pytest or unit tests to ensure all tests pass locally. If the code is failing, please consult with Simon before further proceeding.

11. Type ``git checkout main && git pull upstream main`` and create a new branch called ``precommit``.

12. Copy and paste the ``.flake8`` and ``.pre-commit-config.yaml`` files from ``{{ cookiecutter.repo_name }}`` to the top directory level. Cross-check with https://github.com/diffpy/diffpy.utils.

13. Run ``pre-commit run --all-files``. Fix any spelling suggestions from Codespell. To ignore a specific word or line, add it under  ``.codespell/ignore_words.txt`` or ``.codespell/ignore_lines.txt``. To ignore specific file types, add the file extensions i.g. ``*.gr`` in ``skip = line`` under ``[tool.codespell]`` in ``pyproject.toml``. Include explanations for each addition.

14. Create a PR to ``main``. Mention in the PR that you need to address flake8 errors.

15. After the  ``precommit`` branch has been merged, sync with ``main`` in Step 11, create a new branch called ``flake8``

16. Fix flake8 errors manually:

    - Tip 1: Start with easier error types to fix, such as line-lenghts and "module imported not used", etc.

    - Tip 2: Submit periodic commits within a single PR.

    - Tip 3: Create multiple PRs, each containing a specific theme (e.g., "Fix docstring line-length flake8 errors" using ``flake8-length`` branch, etc.) to reduce cognitive overload for the reviewer (Simon).

    - Tip 4: Don't hesitate to reach out to group members who have contributed to this repository. They probably have seen those errors before!

17. Only proceed to the next section after addressing all PRs relevant to the pre-commit workflow.

2. Cookiecutter workflow
------------------------

1. Type ``cookiecutter https://github.com/billingegroup/cookiecutter`` inside the package directory

2. . Answer the questions as the following -- note that (default) means to hit enter without modifying anything:

   1. (May occur if it is not the first time you have installed) Is it okay to delete: (y)

   2. github_org: diffpy (if diffpy project) or billingegroup

   3. keywords: current keywords in the ``setup.py`` or ``pyproject.toml`` in comma-separated string format, e.g., ``diffpy, pdf, something, something else`` (no quotes around it)

   4. project_name: <name_of_project (e.g. ``diffpy.pdfmorph``)>

   5. package_dist_name: (default)

   6. package_dir_name: (default)

   7. repo_name: (default)

   8. minimum_python_version: (default -- this is 3.11)

   9. maximum_python_version: (default -- this is 3.13)

   10. have_c_code: no (in general, but if there are C++ extensions, this will be yes)

   11. Is a GUI application, run 'HEADLESS' tests (default: false): (default). If it is a GUI package, change this to ``true``.

   12. Enter value for workflow 'VERSION' (default: v0): (default). Version of the workflow to use.

4. cd into the new ``diffpy.<package_name>/`` directory (e.g., in our example ``pwd`` would return ``~/dev/diffpy.pdfmorph/diffpy.pdfmorph``) (we will refer to the nested directory as the "**cookiecutter**" directory and ``~/dev/diffpy.pdfmorph/`` as the "**main**" directory).

5. Type ``ls -als`` (if you have the alias, this is ``ll``) compare the directory structures in this directory tree to that in the original repo to see what is different (ignore files at this point).  Nothing to do here, just get familiar with the differences.

6. Type ``mv ../.git .`` to move the ``.git`` directory from the main repo to the cookiecutter repo.

7. Create a new branch for all the changes, e.g., ``git checkout -b cookierelease``.

8. Type ``cp -n -r ../src .`` to copy the source code from the main to the cookiecutter repo, without overwriting exiting files in the destination. If there is no src directory, it will be something like ``cp -n -r ../diffpy ./src``.

9. Type ``git status`` to see a list of files that have been (1) untracked, (2) deleted, (3) modified.  Untracked files are in the cookiecutter but not in the original repo, deleted files are in the original but haven't been moved over, and modified files are in both but have been changed.

10. Let's now copy over any documentation, similar to what we did with the src files.  We want to copy over everything in the ``doc/<path>/source`` file from the old repo to the ``doc/source`` file in the new repo.

    1. If you see this extra ``manual`` directory, run ``cp -n -r ../doc/manual/source/* ./doc/source``.

    2. If files are moved to a different path, open the project in PyCharm and do a global search (ctrl + shift + f) for ``../`` or ``..`` and modify all relative path instances.

11. Now we will work on correcting all the things that are wrong.

    1. Add and commit each of the (1) untracked files to the git repo.  These files are in the cookiecutter repo but not in the main repo, so can simply be "git added".  Do it one (or a few) at a time to make it easier to rewind by having multiple commits.

    2. Make a PR of your ``cookierelease`` branch by pushing your fork and opening a PR.

    3. Files showing as (2) "deleted" upon git status are in the main repo but not in the cookiecutter repo.  We took care of most these by moving over the src tree, but let's do the rest now.  Go down the list and for <filename> in the ``git status`` "delete" files type ``cp -n ../<filepath>/<filename> ./<target_filepath>``. Do not move files that we do not want. If you are unsure, feel free to confirm with Simon.

    4. Files that have been (3) modified exist in both places and need to be merged **manually**.  Do these one at a time. First open the file in pycharm, then select ``Git|current file|show diff`` and the differences will show up.  Select anything you want to inherit from the file in the main repo. For example, you want to copy useful information such as LICENSE and README files from the main repo to the cookiecutter repo.

    5. Any files that we moved over from the old place, but put into a new location in the new repo, we need to delete them from git.  For example, files that were in ``doc/manual/source/`` in the old repo but are not ``doc/source`` we correct by typing ``git add doc/manual/source``.

12. Run pytest ``python -m pytest`` to make sure everything is working. There should be no errors if all tests passed previously when you were working on pre-commit. You may encounter deprecation warnings. There might be several possibilities:

    1. If you see numpy deprecation warnings, we won't clean up these deprecations now. Pin numpy to 1.x for now to get tests to pass. Do code fixes separate from cookiecuttering. Remember to add it to Github issue.

    2. Most ``pkg_resources`` deprecation warnings will be fixed by cookiecutter, but if you are in a diffpy package using unittests and see this warning you can fix them by replace ``from pkg_resources import resource_filename`` with ``from importlib import resources`` and change ``path = resource_filename(__name__, p)`` to ``path = str(resources.files(__name__).joinpath(p))``. If you see ``collected 0 items no tests ran`` you might want to rename testing files as ``test_*.py``. Refer to the [migration guide](https://importlib-resources.readthedocs.io/en/latest/migration.html).

3. API documentation workflow
-----------------------------

This should be done only when the above steps are finished.

When you see files with ``..automodule::`` within them, these are API documentation. However, these are not populated. We will populate them using our release scripts.

1. Make sure you have our release scripts repository. Go to ``dev`` and running ``git clone https://github.com/Billingegroup/release-scripts.git``.

2. Enter your cookiecutter package directory. For example, I would run ``cd ./diffpy.pdfmorph/diffpy.pdfmorph``.

3. Build the package using ``python -m build``. You may have to install ``python-build`` first.

4. Get the path of the package directory proper. In the case of ``diffpy.pdfmorph``, this is ``./src/diffpy/pdfmorph``. In general, for ``a.b.c``, this is ``./src/a/b/c``.

5. Run the API script. This is done by running ``python <path_to_auto_api> <package_name> <path_to_package_proper> <path_to_api_directory>``.

   1. If you have followed the steps above, the command is ``python ../../release-scripts/auto_api.py <package_name> <path_to_package_proper> ./doc/source/api``.

Make sure you build the documentation by going to ``/doc`` and running ``make html``.
The error "No module named" (``e.g. WARNING: autodoc: failed to import module 'tools' from module 'diffpy.pdfmorph'; the following exception was raised: No module named 'diffpy.utils'``) can be resolved by adding ``autodoc_mock_imports = [<pkg>]`` to your ``conf.py`` right under imports. This file is located in ``/doc/source/conf.py``.
In the case of ``PDFmorph``, this was done by adding ``autodoc_mock_imports = ["diffpy.utils",]``.

Congratulations! You may now commit the changes made by ``auto_api.py`` (and yourself) and push this commit to the cloud!
Make a PR! It will be merged, trust!
