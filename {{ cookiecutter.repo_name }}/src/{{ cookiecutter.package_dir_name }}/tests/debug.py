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

"""
Convenience module for debugging the unit tests using

python -m {{ cookiecutter.project_name }}.tests.debug

Exceptions raised by failed tests or other errors are not caught.
"""


if __name__ == "__main__":
    import sys

    from {{cookiecutter.project_name}}.tests import testsuite

    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    suite = testsuite(pattern)
    suite.debug()


# End of file
