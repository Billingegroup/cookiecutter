#!/usr/bin/env python3
import pexpect

# This assumes you are running this from a directory called scratch/diffpy.utils
# where scratch is at the same level as dev in your tree.
p = pexpect.spawn("cookiecutter ../../dev/cookiecutter")

p.expect("full_name .*")
p.sendline("diffpy")

p.expect("email .*")
p.sendline("sb2896@columbia.edu")

p.expect("github_username .*")
p.sendline("sbillinge")

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
