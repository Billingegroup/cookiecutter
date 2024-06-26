#!/usr/bin/env python3
from pathlib import Path

import pexpect

# This assumes you are running this from a directory called scratch/diffpy.utils
# where scratch is at the same level as dev in your tree.
cc_path = (Path.cwd() / ".." / ".." / "cookiecutter").resolve()
p = pexpect.spawn(f"cookiecutter {cc_path}")

p.expect("github_org .*")
p.sendline("diffpy")

p.expect("keywords .*")
p.sendline("text data parsers, wx grid, diffraction objects")

p.expect("project_name .*")
p.sendline("diffpy.utils")

p.expect("package_dist_name .*")
p.sendline("")

p.expect("package_dir_name .*")
p.sendline("")

p.expect("repo_name .*")
p.sendline("")

p.expect("project_short_description .*")
p.sendline("general purpose shared utilities for the diffpy libraries")

p.expect("minimum_supported_python_version.*")
p.sendline("3.10")

p.expect("maximum_supported_python_version.*")
p.sendline("3.12")

# Runs until the cookiecutter is done; then exits.
p.interact()
