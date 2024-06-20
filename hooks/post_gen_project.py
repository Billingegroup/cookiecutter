import shutil
from pathlib import Path

# All cookie-cutter hooks run on project root, but good to enforce
ROOT = Path.cwd()


def __gen_init__(module_name):
    __init__ = f"""#!/usr/bin/env python
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

\"\"\"Blank namespace package for module {module_name}.\"\"\"


from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

# End of file

"""
    return __init__


# Add module packages for each leading period
def add_supermodules(ROOT, name):
    src_dir = ROOT / "src"
    c_dir = src_dir  # Current directory

    package_dir_name = "{{ cookiecutter.package_dir_name }}"
    cp_dir = c_dir / package_dir_name  # Current package directory

    # Get the necessary modules given the period spacings
    module_names = name.split(".")
    for i, module in enumerate(module_names):
        module_names[i] = module.strip()

    # The last module is not a namespace module
    ns_module_names = module_names[:-1]

    # Create a subdirectory for each parsed module
    for ns_module_name in ns_module_names:
        # Create module directory and move files
        d_dir = c_dir / ns_module_name  # Destination directory
        try:
            d_dir.mkdir(parents=False, exist_ok=False)
        # Should never occur as the parent directory is tracked by c_dir
        except FileNotFoundError:
            print(f"Parent directory {c_dir} not found. This is likely an issue with cookiecutter.")
        # Should never occur from how we do our naming
        except FileExistsError:
            print(f"Duplicate directory names {d_dir} found. This is likely an issue with cookiecutter.")
        shutil.move(cp_dir, d_dir)

        # Make __init__.py file
        init_file = d_dir / "__init__.py"
        with open(init_file, "w") as ifile:
            ifile.write(__gen_init__(ns_module_name))
        c_dir = c_dir / ns_module_name
        cp_dir = c_dir / package_dir_name

    # Rename the final destination module
    cp_dir.rename(c_dir / module_names[-1])


add_supermodules(ROOT, "{{ cookiecutter.project_name }}")
