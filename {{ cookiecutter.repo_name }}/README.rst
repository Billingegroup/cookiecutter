|Icon| `{{ cookiecutter.package_dist_name }} <https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.repo_name }}>`_
=========================================================

.. |Icon| image:: https://avatars.githubusercontent.com/{{ cookiecutter.github_org }}
        :target: https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.repo_name }}
        :height: 100px
   
|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black
   
.. |CI| image:: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/actions/workflows/main.yml/badge.svg
        :target: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/actions/workflows/main.yml

.. |Codecov| image:: https://codecov.io/gh/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}
   
.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.package_dist_name }}
        :target: https://anaconda.org/conda-forge/{{ cookiecutter.package_dist_name }}

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_dist_name }}
        :target: https://pypi.org/project/{{ cookiecutter.package_dist_name }}/
   
.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_dist_name }}
        :target: https://pypi.org/project/{{ cookiecutter.package_dist_name }}/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/issues

{{ cookiecutter.project_short_description }}

* LONGER DESCRIPTION HERE

For more information about the {{ cookiecutter.package_dist_name }} library, please consult our `online documentation <https://{{ cookiecutter.github_org }}.github.io/{{ cookiecutter.repo_name }}>`_.

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``{{ cookiecutter.package_dist_name }}_env`` ::

        conda create -n {{ cookiecutter.package_dist_name }}_env python=3
        conda activate {{ cookiecutter.package_dist_name }}_env

Then, to fully install ``{{ cookiecutter.package_dist_name }}`` in our active environment, run ::

        conda install {{ cookiecutter.package_dist_name }}

Another option is to use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``{{ cookiecutter.package_dist_name }}_env`` environment, we will also have to install dependencies ::

        pip install -r https://raw.githubusercontent.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/main/requirements/run.txt

and then install the package ::

        pip install {{ cookiecutter.package_dist_name }}

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/>`_. Once installed, ``cd`` into your ``{{ cookiecutter.repo_name }}`` directory
and run the following ::

        pip install .

Support and Contribute
----------------------

`Diffpy user group <https://groups.google.com/g/diffpy-users>`_ is the discussion forum for general questions and discussions about the use of {{ cookiecutter.package_dist_name }}. You can join the {{ cookiecutter.package_dist_name }} users community by joining the Google group. The {{ cookiecutter.package_dist_name }} project welcomes your expertise and enthusiasm!

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/issues>`_ and/or `submit a fix as a PR <https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/pulls>`_. You can also post it to the `Diffpy user group <https://groups.google.com/g/diffpy-users>`_. 

Feel free to fork the project and contribute. To install {{ cookiecutter.package_dist_name }}
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

Improvements and fixes are always appreciated.

To learn more about how to successfully get involved and contributing to {{ cookiecutter.package_dist_name }}, please see our `Code of Conduct <https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact and Citation
--------------------

For more information on {{ cookiecutter.package_dist_name }} please visit the project `web-page <https://{{ cookiecutter.github_org }}.github.io/>`_ or email Prof. Simon Billinge at sb2896@columbia.edu.

If you use {{ cookiecutter.package_dist_name }} in a scientific publication, we would appreciate `citations [ADD LINK] <LINK HERE>`_.  

.. ADD LINK IN <LINK HERE> and delete [ADD LINK]
