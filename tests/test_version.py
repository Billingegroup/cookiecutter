"""Unit tests for __version__.py
"""

import bg_cookiecutter


def test_package_version():
    """Ensure the package version is defined and not set to the initial placeholder."""
    assert hasattr(bg_cookiecutter, "__version__")
    assert bg_cookiecutter.__version__ != "0.0.0"
