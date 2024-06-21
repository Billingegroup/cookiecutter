#!/usr/bin/env python3
from pathlib import Path

import pexpect

# This assumes you are running this from a directory called scratch/diffpy.utils
# where scratch is at the same level as dev in your tree.
cc_path = (Path.cwd() / ".." / ".." / "cookiecutter").resolve()
p = pexpect.spawn(f"cookiecutter {cc_path}")

p.expect("github_org .*")
p.sendline("diffpy")

p.expect("keyword_1 .*")
p.sendline("")

p.expect("keyword_2 .*")
p.sendline("")

p.expect("keyword_3 .*")
p.sendline("")

p.expect("project_name .*")
p.sendline("diffpy.utils")

p.expect("package_dist_name .*")
p.sendline("")

p.expect("package_dir_name .*")
p.sendline("")

p.expect("repo_name .*")
p.sendline("")

p.expect("project_short_description .*")
p.sendline("")

p.expect("Select minimum_supported_python_version.*")
p.sendline("3")

# Runs until the cookiecutter is done; then exits.
p.interact()
