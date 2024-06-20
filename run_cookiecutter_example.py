#!/usr/bin/env python3
import pexpect

p = pexpect.spawn("cookiecutter .")

p.expect("github_org .*")
p.sendline("diffpy")

p.expect("project_name .*")
p.sendline("diffpy.my_project")

p.expect("package_dist_name .*")
p.sendline("")

p.expect("package_dir_name .*")
p.sendline("")

p.expect("repo_name .*")
p.sendline("")

p.expect("project_short_description .*")
p.sendline("")

p.expect("Select minimum_supported_python_version.*")
p.sendline("")

# Runs until the cookiecutter is done; then exits.
p.interact()
