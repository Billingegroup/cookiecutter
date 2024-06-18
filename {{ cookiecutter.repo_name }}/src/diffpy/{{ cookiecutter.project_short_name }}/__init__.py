#!/usr/bin/env python
##############################################################################
#
# diffpy.utils      by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2010 The Trustees of Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Chris Farrow, Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE_DANSE.txt for license information.
#
##############################################################################

"""Smaller shared functions for use by other diffpy packages.
"""

# package version
package_name = '{{ cookiecutter.project_name }}'
version = getattr(__import__(package_name+".version", fromlist=["__version__"]), "__version__")

# silence the pyflakes syntax checker
assert version or True

# End of file
