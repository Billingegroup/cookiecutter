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

"""Definition of __version__."""

#  We do not use the other three variables, but can be added back if needed.
#  __all__ = ["__date__", "__git_commit__", "__timestamp__", "__version__"]

# obtain version information
from importlib.metadata import version

__version__ = version("{{ cookiecutter.project_name }}")

# End of file
