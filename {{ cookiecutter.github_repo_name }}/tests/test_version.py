"""Unit tests for __version__.py."""

import {{ cookiecutter.package_dir_name }}


def test_package_version():
    """Ensure the package version is defined and not set to the initial
    placeholder."""
    assert hasattr({{ cookiecutter.package_dir_name }}, "__version__")
    assert {{ cookiecutter.package_dir_name }}.__version__ != "0.0.0"
