#!/usr/bin/env python
##############################################################################
#
# (c) {% now 'utc', '%Y' %} The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Billinge Group members and community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""{{ cookiecutter.project_short_description }}"""

# package version
from {{cookiecutter.package_dir_name}}.version import __version__

# silence the pyflakes syntax checker
assert __version__ or True

# End of file
