#!/usr/bin/env python
##############################################################################
#
# (c) 2024 The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: {{ cookiecutter.author_name }}
#
# See AUTHORS.rst for a list of people who contributed.
# See LICENSE.rst for license information.
#
##############################################################################

"""Smaller shared functions for use by other diffpy packages.
"""

# package version
from {{ cookiecutter.project_name }}.version import __version__

# silence the pyflakes syntax checker
assert __version__ or True

# End of file
