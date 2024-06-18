#!/usr/bin/env python
##############################################################################
#
# diffpy.utils      Complex Modeling Initiative
#                   (c) 2016 Brookhaven Science Associates,
#                   Brookhaven National Laboratory.
#                   All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

"""
Convenience module for debugging the unit tests using

python -m diffpy.utils.tests.debug

Exceptions raised by failed tests or other errors are not caught.
"""


if __name__ == "__main__":
    import sys
    package_name = '{{ cookiecutter.project_name }}'
    testsuite = getattr(__import__(package_name+".tests", fromlist=["testsuite"]), "testsuite")

    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    suite = testsuite(pattern)
    suite.debug()


# End of file
