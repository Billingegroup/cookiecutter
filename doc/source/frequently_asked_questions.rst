:tocdepth: -1

.. index:: frequently_asked_questions

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
