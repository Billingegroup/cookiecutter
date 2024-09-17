import re
import shutil
from pathlib import Path

import requests

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


def __gen_setuppy__():
    base_module_name = "{{ cookiecutter.project_name }}".split('.')[-1].strip()
    setuppy = """#!/usr/bin/env python

# Extensions script for {{ cookiecutter.project_name }}

import os
import re
import sys
import glob
from setuptools import setup
from setuptools import Extension

# Define extension arguments here
ext_kws = {
        'libraries' : [],
        'extra_compile_args' : [],
        'extra_link_args' : [],
        'include_dirs' : [],
}
""" + f"""# Figure out the tagged name of boost_python library.
def get_boost_libraries():
    \"\"\"Check for installed boost_python shared library.

    Returns list of required boost_python shared libraries that are installed
    on the system. If required libraries are not found, an Exception will be
    thrown.
    \"\"\"
    baselib = \"boost_python\"
    major, minor = (str(x) for x in sys.version_info[:2])
    pytags = [major + minor, major, '']
    mttags = ['', '-mt']
    boostlibtags = [(pt + mt) for mt in mttags for pt in pytags] + ['']
    from ctypes.util import find_library
    for tag in boostlibtags:
        lib = baselib + tag
        found = find_library(lib)
        if found: break

    # Show warning when library was not detected.
    if not found:
        import platform
        import warnings
        ldevname = 'LIBRARY_PATH'
        if platform.system() == 'Darwin':
            ldevname = 'DYLD_FALLBACK_LIBRARY_PATH'
        wmsg = (\"Cannot detect name suffix for the %r library. \"
                \"Consider setting %s.\") % (baselib, ldevname)
        warnings.warn(wmsg)

    libs = [lib]
    return libs


def create_extensions():
    \"Initialize Extension objects for the setup function.\"
    blibs = [n for n in get_boost_libraries()
            if not n in ext_kws['libraries']]
    ext_kws['libraries'] += blibs
    ext = Extension('{{ cookiecutter.package_dir_name }}.{base_module_name}_ext',
                    glob.glob('src/extensions/*.cpp'),
                    **ext_kws)
    return [ext]


# Extensions not included in pyproject.toml
setup_args = dict(
    ext_modules = [],
)


if __name__ == '__main__':
    setup_args['ext_modules'] = create_extensions()
    setup(**setup_args)

"""
    return setuppy


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

def wrapper_setup():
    src_dir = ROOT / "src"
    ext_dir = src_dir / "extensions"
    try:
        ext_dir.mkdir(parents=False, exist_ok=False)
    # Should never occur as the parent directory is src
    except FileNotFoundError:
        print(f"Parent directory {src_dir} not found. This is likely an issue with cookiecutter.")
    # Can occur if user names the package extensions
    except FileExistsError:
        print(f"Duplicate directory names {src_dir} found. You cannot name your project 'extensions*'.")

    # Make __init__.py file
    setuppy_file = ROOT / "setup.py"
    with open(setuppy_file, "w") as spfile:
        spfile.write(__gen_setuppy__())

def update_workflow():

    CENTRAL_REPO_ORG = "Billingegroup"
    CENTRAL_REPO_NAME = "release-scripts"
    CENTRAL_WORKFLOW_DIR = ".github/workflows/templates"
    LOCAL_WORKFLOW_DIR = ROOT / ".github" / "workflows"

    workflow_input = {"PROJECT": "{{ cookiecutter.project_name }}",
                      "C_EXTENSION": str("{{ cookiecutter.is_boost_wrapper }}"=="y").lower(),
                      "HEADLESS": input(f"Enter value for workflow 'HEADLESS' (default: {'false'}): ").strip().lower() or 'false',
                      "VERSION": input(f"Enter value for workflow 'VERSION' (default: {'v0'}): ").strip() or "v0"}

    def get_central_workflows():
        base_url = f"https://api.github.com/repos/{CENTRAL_REPO_ORG}/{CENTRAL_REPO_NAME}/contents/{CENTRAL_WORKFLOW_DIR}"
        response = requests.get(base_url, timeout=5)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch central workflows: {response.status_code}")

        workflows = {}
        for file in response.json():
            if file['type'] == 'file' and file['name'].endswith('.yml'):
                content_response = requests.get(file['download_url'], timeout=5)
                if content_response.status_code == 200:
                    workflows[file['name']] = content_response.text
        return workflows


    def update_workflow_params(content):

        def replace_match(match):
            key = match.group(1)
            return str(workflow_input[key])

        pattern = re.compile(r"\{\{\s*(\w+)\s*/\s*([^\s\}]+)\s*\}\}")
        return pattern.sub(replace_match, content)


    def update_local_workflows(central_workflows):
        local_workflows = set(f.name for f in LOCAL_WORKFLOW_DIR.glob("*.yml"))
        central_workflow_names = set(central_workflows.keys())

        for name, content in central_workflows.items():
            local_file = LOCAL_WORKFLOW_DIR / name

            content = update_workflow_params(content)

            with open(local_file, "w", encoding="utf-8") as file:
                file.write(content)

        for name in local_workflows - central_workflow_names:
            (LOCAL_WORKFLOW_DIR / name).unlink()
            print(f"Removed workflow {name}")


    try:
        LOCAL_WORKFLOW_DIR.mkdir(parents=True, exist_ok=True)
        central_workflows = get_central_workflows()
        update_local_workflows(central_workflows)
        print("Workflow synchronization completed successfully")
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    add_supermodules(ROOT, "{{ cookiecutter.project_name }}")
    if "{{ cookiecutter.is_boost_wrapper }}" == "y":
        wrapper_setup()
    update_workflow()

if __name__ == '__main__':
    main()
