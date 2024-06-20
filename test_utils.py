#!/usr/bin/env python3
from pathlib import Path

import pexpect

# This assumes you are running this from a directory called scratch/diffpy.utils
# where scratch is at the same level as dev in your tree.
cc_path = (Path.cwd() / ".." / ".." / "cookiecutter").resolve()
p = pexpect.spawn(f"cookiecutter {cc_path}")

p.expect("full_name .*")
p.sendline("diffpy")

p.expect("project_name .*")
p.sendline("diffpy.utils")

p.expect("author_name .*")
p.sendline("Simon Billinge")

p.expect("github_username .*")
p.sendline("sbillinge")

p.expect("email .*")
p.sendline("sb2896@columbia.edu")

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
