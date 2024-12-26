#######
|title|
#######

.. |title| replace:: bg-cookiecutter documentation

| Software version |release|.
| Last updated |today|.

Welcome to Billinge Group's Python cookiecutter documentation!

Benefits
--------

``bg-cookiecutter`` is a Python project template designed for scientific software development. The template allows you to save time and prioritize the scientific content of your package by providing the following features:

- Automated `PEP8 <https://peps.python.org/pep-0008/>`_ and `PEP256 <https://peps.python.org/pep-0256/>`_ standard checks.
- Automated PyPI/GitHub release, testing, documentation, and CHANGELOG updates.
- Streamlined package release workflow with a checklist.
- Latest Python version support compatible with `SPEC0 <https://scientific-python.org/specs/spec-0000/>`_.
- Rich README template containing badges, installation, support, and contribution guide.
- Automatic spelling check, linting for .json, .yml, and .md files.

For more technical details, it includes:

- Pull requests with coverage reports using ``Codecov`` and checks with ``pre-commit CI``.
- Namespace package support, e.g., ``import diffpy.utils``.
- conda-package ``meta.yaml`` generation with a template.
- Support for non-pure Python package releases with ``cibuildwheel``.
- Support for headless GitHub CI testing for GUI applications.
- Reusable GitHub Actions workflows located in `Billingegroup/release-scripts <https://github.com/Billingegroup/release-scripts/tree/main/.github/workflows>`_.

How do I get started?
---------------------

Please visit the :ref:`Getting started <getting_started>` page to learn how to navigate the documentation!

How do I receive support?
-------------------------

If you have any questions or have trouble, please read the :ref:`Frequently asked questions (FAQ) <frequently_asked_questions>` section to see if your questions have already been answered. If there aren't answers available, please create an issue. The team will reach out.

How can I contribute?
---------------------

Do you have any new features? Please make an issue via the GitHub issue tracker for further discussions. For a minor typo or grammatically incorrect sentence, please make a pull request. Before making a PR, please run ``pre-commit run --all-files`` to ensure the code is formatted.

Who are using ``bg-cookiecutter``?
----------------------------------

The full list of packages is as follows:

- `diffpy.pdffit2 <https://github.com/diffpy/diffpy.pdffit2>`_
- `diffpy.fourigui <https://github.com/diffpy/diffpy.fourigui>`_
- `diffpy.pdfgui <https://github.com/diffpy/diffpy.pdfgui>`_
- `diffpy.utils <https://github.com/diffpy/diffpy.utils>`_
- `diffpy.structure <https://github.com/diffpy/diffpy.structure>`_
- `diffpy.labpdfproc <https://github.com/diffpy/diffpy.labpdfproc>`_
- `diffpy.pdfmorph <https://github.com/diffpy/diffpy.pdfmorph>`_
- `diffpy.snmf <https://github.com/diffpy/diffpy.snmf>`_
- `diffpy.srmise <https://github.com/diffpy/diffpy.srmise>`_
- `regolith <https://github.com/regro/regolith>`_
- `bg-mpl-stylesheets <https://github.com/Billingegroup/bg-mpl-stylesheets>`_

=======
Authors
=======

bg-cookiecutter is developed by Billinge Group and its community contributors.

For a detailed list of contributors, see
https://github.com/Billingegroup/cookiecutter/graphs/contributors.

================
Acknowledgements
================

The Billinge Group's cookiecutter has been modified from the
The Billinge Group's cookiecutter has been modified from the NSLS-II scientific cookiecutter: https://github.com/nsls-ii/scientific-python-cookiecutter

=================
Table of contents
=================
.. toctree::
   :maxdepth: 2

   getting_started
   cookiecutter_guide
   release_guide
   conda_forge_guide
   frequently_asked_questions
   license
   release

=======
Indices
=======

* :ref:`genindex`
* :ref:`search`
