:tocdepth: -1

==================================
How to release conda-forge package
==================================

conda-forge: release for the first time
---------------------------------------

Step 1. Prepare ``meta.yaml``. See Appendix 1 to learn more about ``meta.yaml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run ``pip install cookiecutter`` and ``cookiecutter https://github.com/billingegroup/staged-recipes-cookiecutter``

1. Answer the following questions. Default values in parentheses are used if no value is provided.

    1. github_org (diffpy):
    
    2. module_name (diffpy.my_project): diffpy.srreal
    
    3. repo_name (diffpy.srreal):
    
    4. version (1.0.0): 1.3.1
    
    5. Select source 1 - PyPi or 2 - GitHub: 1
    
       1. Choose 1. Conda package can be built using PyPI's ``sdist`` containing requirements files, src/tests, and ``pyproject.toml``
       
    6. project_short_description (Python package for doing science.):
    
    7. project_full_description (This is a Python package for doing science.):
    
    8. license_file (LICENSE.rst):
    
    9.  recipe_maintainers (sbillinge,):
    
    10. build_requirements ():
    
        1.  copy ``requirements/build.txt`` from the project repo.
        
        2.  Empty for pure Python packages, otherwise compilers will be required.
        
    11. host_requirements (python >=3.11, setuptools, setuptools-git-versioning >=2.0, pip,):
    
        1.  copy ``requirements/host.txt``
        
    12. runtime_requirements (python >=3.11, numpy,):
    
        1.  copy ``requirements/conda.txt``

    13. testing_requirements (pip, pytest,):
        1.  copy ``requirements/test.txt``

As an example, check https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml

4. Now, ``recipes/<package-name>/meta.yaml`` is generated.

Checklist for ``meta.yaml`` file (extremely important)

- [ ] For pure python packages, the ``build`` section under the ``requirements`` will be empty. Remove that section. Ex) https://github.com/conda-forge/diffpy.utils-feedstock/blob/main/recipe/meta.yaml

- [ ] Double-check the license file name in ``meta.yaml`` against the license files in the project repository. If you are unsure, please confirm with Prof. Billinge.


Step 2. Upload ``meta.yaml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork https://github.com/conda-forge/staged-recipes and clone your forked repository

2. cd into ``staged-recipes``

3. Create ``recipes/<package-name>/meta.yaml`` Ex) ``recipes/diffpy.srreal/meta.yaml``

4. Copy and paste the content of ``meta.yaml`` from Step 1.

5. Create a new branch: ``git checkout -b <project_name>``

6. Add and commit the changes: ``git add . && git commit -m "Committing recipe for conda-forge release of <project_name>"``

7. Push the changes: ``git push -u origin <project_name>``

8. Visit https://github.com/conda-forge/staged-recipes and create a PR. 

9. Read through the pre-filled text in the PR message and follow the instructions.

10. After the CI passes, create a new comment: ``@conda-forge/help-python Hello Team, ready for review!``

Step 3. Wait for review and merge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Wait for a ``conda-forge`` reviewer to review your submission (may take up to one week)

2. Once the PR is merged by the reviewer (1) your package is available on conda-forge, and (2) a new repository will be created under https://github.com/conda-forge/package-name-feedstock/. Example: https://github.com/conda-forge/diffpy.structure-feedstock.

## conda-forge: pre-release

Generate ``meta.yaml`` by following ``Step 1`` and ``Step 2`` under ``conda-forge: release for the first time`` above. Here are two differences required for pre-release:

1. Create ``recipe/conda_build_config.yaml`` containing::

    channel_targets:
       - conda-forge <package-name>_rc

See an example here: https://github.com/conda-forge/diffpy.pdffit2-feedstock/blob/rc/recipe/conda_build_config.yaml

1. Make a PR into ``rc`` instead of ``main``. Re-render once the PR is created.

To install the pre-release build::

    conda install -c conda-forge/label/<package-name>_rc -c conda-forge <package-name>

For more, read the documentation for pre-release: https://conda-forge.org/docs/maintainer/knowledge_base/#pre-release-builds

Appendix 1. Background info on ``meta.yml``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``meta.yaml`` file contains information about dependencies, the package version, the license, the documentation link, and the maintainer(s) of the package.

In ``meta.yaml``, there are 3 important keywords under the ``requirements`` section: ``build``, ``host``, and ``run``.

- **Build dependencies** are used for compiling but are not needed on the host where the package will be used. Examples include compilers, CMake, Make, pkg-config, etc.

- **Host dependencies** are required during the building of the package. Examples include setuptools, pip, etc.

- **Run dependencies** are required during runtime. Examples include matplotlib-base, numpy, etc.

To avoid any confusion, there is a separate YAML section called ``build`` above the ``requirements`` section. This section is for setting up the entire operating system.

For more information, please refer to the official documentation: https://conda-forge.org/docs/maintainer/adding_pkgs/#build-host-and-run
