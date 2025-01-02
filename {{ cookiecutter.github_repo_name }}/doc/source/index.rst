#######
|title|
#######

.. |title| replace:: {{ cookiecutter.project_name }} documentation

{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}.

| Software version |release|.
| Last updated |today|.

=======
Authors
=======

{{ cookiecutter.project_name }} is developed by Billinge Group
and its community contributors.

For a detailed list of contributors see
https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo_name }}/graphs/contributors.

============
Installation
============

See the `README <https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.github_repo_name }}#installation>`_
file included with the distribution.

=================
Table of contents
=================
.. toctree::
   :titlesonly:

   license
   release
   Package API <api/{{ cookiecutter.package_dir_name }}>

=======
Indices
=======

* :ref:`genindex`
* :ref:`search`
