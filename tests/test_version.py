"""Unit tests for __version__.py."""

import scikit_package


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr(scikit_package, "__version__")
    assert scikit_package.__version__ != "0.0.0"
    print(scikit_package.__version__)
