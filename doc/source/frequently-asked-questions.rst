:tocdepth: -1

.. index:: frequently-asked-questions

.. _frequently-asked-questions:

================================
Frequently asked questions (FAQ)
================================

Here, you will learn how to customize the ``bg-cookiecutter`` template for your own project, such as setting the line-width and including/excluding files for PyPI distribution. We also provide design decisions for the current setup of the ``bg-cookiecutter`` template.

Formatting
----------

How do I modify line-width limits?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Three files need to be modified:

1. In ``.isort.cfg``, modify ``line_length``
2. In ``.flake8``, modify ``max-line-length``
3. In ``pyproject.toml``, modify ``line-length`` under ``[tool.black]``.

Pre-commit
----------

.. codespell-add-word:

How do I ignore words/lines/files in automatic spelling checks in pre-commit?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ignore a word, add it to ``.codespell/ignore_words.txt``.

To ignore a specific line, add it to ``.codespell/ignore_lines.txt``. See the example below:

.. code-block:: text

  ;; src/translation.py
  ;; The following single-line comment is written in German.
  # Hallo Welt

To ignore a specific file extension, add ``*.ext`` to the ``skip`` section under ``[tool.codespell]`` in ``pyproject.toml``. For example, to ignore ``.cif`` and ``.dat`` files, use ``skip = "*.cif,*.dat"``.

Release
-------

.. _release_authority:

How can I change who is authorized to release a package?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In ``.github/workflows/build-wheel-release-upload.yml``, modify ``github_admin_username`` to the desired GitHub username. This username will be able to authorize the release by pushing the tag as instructed :ref:`here <release-instructions-project-owner>`.

How is the package version set and retrieved?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In ``pyproject.toml``, the ``setuptools-git-versioning`` tool is used to dynamically retrieve the version based on the latest tag in the repository. The latest tag is pushed during the release workflow. The dynamically parsed version is globally accessible, via ``<package-name>.__version__``.

How do I include/exclude files in PyPI release?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``MANIFEST.in`` file is used to control which files are included in the source distribution. Try running ``python -m build`` and see the content under the ``dist`` folder generated.

To include all files under a folder, use ``graft``:

.. code-block:: text

   graft src
   graft tests

To include specific file(s), use ``include``:

.. code-block:: text

   include AUTHORS.txt LICENSE*.txt README.rst

To exclude files globally, use ``globally-exclude``:

.. code-block:: text

   global-exclude *.py[cod]  # Exclude all .pyc, .pyo, and .pyd files.
   global-exclude .DS_Store  # Exclude Mac filesystem artifacts.
   global-exclude __pycache__  # Exclude Python cache directories.
   global-exclude .git*  # Exclude git files and directories.

Why have we decided to include test files in the PyPI source distribution?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We decided to include test files in the PyPI source distribution to facilitate unit testing with a newly built Conda package.

The conda-forge CI uses the source code distributed via PyPI to build a Conda package. After building the package, we want to run pytest to ensure all unit tests pass before release. Therefore, test files must be included in the source code. In contrast, no documentation is distributed with the package, as it is already accessible from the GitHub repository and does not serve a practical purpose in the distribution package itself.

Documentation
-------------

How can I preview documentation in real-time?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may use Visual Studio Code. Please refer to the following section :ref:`here <build-documentation-preview-real-time>`.

How do I re-deploy online documentation without another release?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Visit the following URL of your package: ``https://github.com/<org-name>/<package-name>/actions/workflows/publish-docs-on-release.yml`` i.e., https://github.com/diffpy/diffpy.utils/actions/workflows/publish-docs-on-release.yml.

Click ``Run workflow`` and select the ``main`` branch. Your online documentation will be updated with the latest changes without a new release.

conda-forge
-----------

How do I add a new admin to the conda-forge feedstock?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to the admin section in the conda-forge release guide :ref:`here <conda-forge-add-admin>`.

How do I do pre-release for conda-forge?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please read our pre-release section in the conda-forge release guide :ref:`here <conda-forge-pre-release>`.

GitHub Actions
--------------

How do I set different Python versions for GitHub CI?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default is Python 3.13 for ``_tests-on-pr.yml`` and ``_publish-docs-on-release.yml``. Python 3.11, 3.12, and 3.13 are used for ``_matrix-and-codecov-on-merge-to-main.yml``. To override the default, modify the three ``.yml`` files above in ``.github/workflows/`` as shown below:

1. Add ``python_version`` in ``.github/workflows/tests-on-pr.yml``:

.. code-block:: yaml

   jobs:
    tests-on-pr:
      uses: Billingegroup/release-scripts/.github/workflows/_tests-on-pr.yml@v0
    with:
      project: package-name
      c_extension: false
      headless: false
      python_version: 3.12
    secrets:
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

2. Add ``python_version`` in ``.github/workflows/_publish-docs-on-release.yml``:

.. code-block:: yaml

   jobs:
    docs:
      uses: Billingegroup/release-scripts/.github/workflows/_tests-on-pr.yml@v0
    with:
      project: package-name
      c_extension: false
      headless: false
      python_version: 3.12

3. Add ``python_versions`` in ``.github/workflows/_matrix-and-codecov-on-merge-to-main.yml``:

.. code-block:: yaml

   jobs:
    matrix-coverage:
      uses: Billingegroup/release-scripts/.github/workflows/_matrix-and-codecov-on-merge-to-main.yml@v0
    with:
      ...
      python_versions: "3.11, 3.12"

What is the difference between ``pull_request`` and ``pull_request_target``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the current GitHub CI for checking a news item, ``pull_request_target`` is used instead of ``pull_request`` as shown below:

.. code-block:: yaml

   name: Check News Item

   on:
    pull_request_target:
      branches:
       - main

- ``pull_request``: This event configures the ``GITHUB_TOKEN`` with read-only permissions by default, especially when triggered by forks.
- ``pull_request_target``: This event grants the ``GITHUB_TOKEN`` write permissions, enabling it to perform actions that modify the repository, such as posting comments, updating pull request statuses, or merging code. The news CI creates a comment when an additional news ``.rst`` is not found under the ``news`` folder. Hence, ``pull_request_target`` is used.

Another key difference is that with ``pull_request_target``, the ``.yml`` file **must already be merged** in the base branch at the time the pull request is opened or updated. For more, please refer to `GitHub docs <https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#pull_request_target>`_.

Dependency management
---------------------

Why are both pip.txt and conda.txt provided?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Our preferred choice for installing the cookiecuttered package is as a Conda package, as outlined in the template ``README.rst`` file. With Conda, the end user can install all associated dependencies by running ``conda create --name new_env <package-name>``. Additionally, the environment is tested via conda-forge CI before the Conda package is released, which helps ensure the package's compatibility with its dependencies. Hence, we list conda package dependencies in ``conda.txt``.

However, we also want to allow users to install the package via ``pip``. To support this, we provide a separate file for pip dependencies, ``pip.txt``. In most cases, the dependencies listed in ``conda.txt`` and ``pip.txt`` will be identical. However, there can be exceptions. For example, ``matplotlib-base`` is preferred for Conda installations, while ``matplotlib`` is used for pip installations.

GitHub workflow
---------------

I am new to GitHub. Why do we use Git/GitHub?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GitHub allows multiple contributors to work on a software project simultaneously under an organization like ``Billingegroup`` or ``diffpy``. There are two primary needs. First, we want to ensure that any changes under this organization are reviewed by the organization's project owner. Second, we want to ensure we add new changes from the latest version of the code, particularly when working with multiple contributors across different time zones. Hence, we use GitHub to serve the needs with a specific workflow below. Please see below for an overview of the GitHub workflow.

.. _github-workflow-overview:

What is the general the workflow?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since cookiecutting requires a basic understanding of GitHub's workflow, we will provide you with a brief overview and how to set up your repository.

First, if you are working on a package from an organization like ``github.com/diffpy`` or ``github.com/Billingegroup``, you first copy the repository of the organization to your GitHub user account. This process is called ``forking``.

Then, you will download the forked repository in your GitHub account to your local machine. This process is called ``cloning``.

In the cloned repository on your local machine, you will make edits. You want to first add a description for the changes by "committing" with a message describing the changes. Then you will upload these changes to the ``forked`` repository in your account. This process of updating code from the local computer to the repository hosted by GitHub is called ``pushing``.

From the forked repository, you then want to upload changes to the repository under ``github.com/Billingegroup/cookiecutter``, for example. This process is done through a process called ``pull request``. The Project Owner reviews this pull request and merges it into the Billinge group's repository. If you are the contributor as well as the Project Owner, you would be the one who reviews your own code and merges your changes.

I have a general understanding of fork, clone, commit, push, and pull request. How do I set up my repository for cookiecutting?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please be familiar with the terminology such as "fork", "clone", "push", and "pull request" :ref:`above <github-workflow-overview>`.

You may fork the repository using the "Fork" button on the top right corner of the repository page. This will copy the repository to your GitHub account. e.g., ``github.com/Billingegroup/cookiecutter`` to ``github.com/sbillinge/cookiecutter``.

Then download the forked repository under your account to the local machine by cloning:

.. code-block:: bash

  git clone https://github.com/<username>/<package-name>

Now, you also want to link with the repository of the organization by adding the URL. Recall, we want to make changes from the latest state of the source code.

.. code-block:: bash

  git remote add upstream https://github.com/<org-name>/<package-name>

.. note::

   What is ``upstream``? The repository that you forked from, e.g. ``Billingegroup/cookiecutting`` is referred to as the ``upstream`` repository.

Verify that you have the ``upstream`` URL set up as the organization.

.. code-block:: bash

  git remote -v

Notice that you also have ``origin`` with an URL linking to your forked repository under your account. This is another GitHub jargon that refers to your forked repository.

.. note::

  What is ``remote``? The term ``remote`` is the opposite of ``local``. In other words, ``remote`` refers to the repository that is hosted by GitHub. e.g., ``github.com/Billingegroup/cookiecutter`` or ``github.com/sbillinge``.

Do you have a general summary of each term used in the GitHub workflow?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:fork: The process of copying a repository from an organization to your GitHub account. e.g., ``github.com/Billingegroup/cookiecutter`` to ``github.com/sbillinge/cookiecutter``.

:upstream: The repository of the original source code. e.g., ``github.com/Billingegroup/cookiecutter``.

:origin: The forked repository under your account. e.g., ``github.com/sbillinge/cookiecutter``.

:remote: The repository that is hosted by GitHub. e.g., ``github.com/Billingegroup/cookiecutter`` or ``github.com/sbillinge/cookiecutter``.

:branch: The branch serves as a folder that contains the files of the repository. The ``main`` branch is the branch that is used for the final version of the code. Many branches can be created for different features or bug fixes that are later merged into the ``main`` branch.

:git clone: The process of locally downloading a repository from GitHub (``remote``) to your local machine.

:git push: The process of updating code from the local computer to the GitHub remote repository. Push can be made to the ``origin`` or ``upstream`` repository. But, in our workflow, we push to the ``origin`` repository, and then we create a pull request to merge the changes from ``origin`` to the ``upstream`` repository.

:git commit: The process of adding a description for the changes made in the files that are ready to be pushed.

:git add: The process of selecting files to be included within a single commit.

I have cloned and added ``upstream``. What is the next step?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to first sync our local folder with the ``upstream`` repository. This process is called ``pulling``.

.. code-block:: bash

  git checkout main
  git pull upstream main

Above, we checkout the ``main`` branch of your cloned folder. We then download all the latest changes from the ``upstream`` repository. Recall that a GitHub repository is contributed by multiple contributors. Hence, we want to ensure that we are working with the latest version of the code in the ``main`` branch.

Once we are fully synced with the ``upstream`` repository, we can now start making changes to the code.

Instead of directly working in the ``main`` branch of your cloned repository, you will create a copy of ``main`` by "branching" it from ``main``. Think of a tree. You can name it anything you want like ``docs-faq``, etc.

.. code-block:: bash

  git checkout -b docs-faq

The above command not only creates a new branch but also switches to the new branch. You can verify that you are in the new branch by running:

.. code-block:: bash

  git branch

Of course, you can always switch back to the ``main`` branch by using ``git checkout main``.

Now, you are ready to make changes to the code in the branch. If you have a README file in your project, try to modify it. Once you are done, you want to add the changes to a hidden folder called ``.git``. This process is called ``staging``.

.. code-block:: bash

  git add README.rst

Then, now you want to commit the changes with a message describing the changes.

.. code-block:: bash

  git commit -m "docs: added a FAQ section in the README"

Now, you want to push the changes to the ``origin`` repository under your account. Recall ``origin`` refers to the forked repository under your account hosted by GitHub.

.. code-block:: bash

  git push --set-upstream origin docs-FAQ

Go to your forked repository under your account on GitHub. You will see a green button that says "Compare & pull request". Click on it. You will see the changes you made in the branch. Click on "Create pull request". Add a description of the changes you made. Click on "Create pull request".

The reviewer will review the changes and merge them into the ``upstream`` repository. You have successfully made your first contribution to the organization's repository.

I still need to make another pull request. How do I do that?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, you want to make another pull request. You want to make sure that you are working with the latest version of the code in the ``main`` branch.

.. code-block:: bash

  git checkout main
  git pull upstream main

The command above will sync your local folder with the ``upstream`` repository. It should download the changes made by other contributors as well as the recent commit you made in the ``docs-FAQ`` branch, for example.

Again, you checkout a new branch from the ``main`` branch. You can name it anything you want, e.g. ``docs-typo``.

.. code-block:: bash

  git checkout -b docs-typo

You repeat the process of git add, commit, push to your ``origin`` (your forked repository) and then make a PR to the ``upstream`` repository (the organization's repository).
