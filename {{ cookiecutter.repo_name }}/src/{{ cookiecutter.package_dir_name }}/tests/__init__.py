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

"""Unit tests for {{ cookiecutter.project_name }}.
"""

import unittest


def testsuite(pattern=""):
    """Create a unit tests suite for {{ cookiecutter.project_name }} package.

    Parameters
    ----------
    pattern : str, optional
        Regular expression pattern for selecting test cases.
        Select all tests when empty.  Ignore the pattern when
        any of unit test modules fails to import.

    Returns
    -------
    suite : `unittest.TestSuite`
        The TestSuite object containing the matching tests.
    """
    import re
    from importlib.resources import as_file, files
    from itertools import chain
    from os.path import dirname

    loader = unittest.defaultTestLoader
    ref = files(__package__)
    with as_file(ref) as thisdir:
        depth = __name__.count(".") + 1
        topdir = thisdir
        for i in range(depth):
            topdir = dirname(topdir)
        suite_all = loader.discover(str(thisdir), top_level_dir=topdir)
    # always filter the suite by pattern to test-cover the selection code.
    suite = unittest.TestSuite()
    rx = re.compile(pattern)
    tsuites = list(chain.from_iterable(suite_all))
    tsok = all(isinstance(ts, unittest.TestSuite) for ts in tsuites)
    if not tsok:  # pragma: no cover
        return suite_all
    tcases = chain.from_iterable(tsuites)
    for tc in tcases:
        tcwords = tc.id().split(".")
        shortname = ".".join(tcwords[-3:])
        if rx.search(shortname):
            suite.addTest(tc)
    # verify all tests are found for an empty pattern.
    assert pattern or suite_all.countTestCases() == suite.countTestCases()
    return suite


def test():
    """Execute all unit tests for the {{ cookiecutter.project_name }} package.

    Returns
    -------
    result : `unittest.TestResult`
    """
    suite = testsuite()
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result


# End of file
