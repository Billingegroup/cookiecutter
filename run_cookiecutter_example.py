#!/usr/bin/env python3
import pexpect

full_name = 'Simon J.L. Billinge group'
email = 'simon.billinge@gmail.com'
github_username = 'diffpy'
project_name = 'diffpy.utils'

project_short_name = project_name.rsplit('.', 1)[-1]
p = pexpect.spawn('cookiecutter .')

p.expect('full_name .*')
p.sendline(full_name)

p.expect('email .*')
p.sendline(email)

p.expect('github_username .*')
p.sendline(github_username)

p.expect('project_name .*')
p.sendline(project_name)

p.expect('project_slug .*')
p.sendline('')

p.expect('project_short_name .*')
p.sendline(project_short_name)

p.expect('package_dist_name .*')
p.sendline('')

p.expect('package_dir_name .*')
p.sendline('')

p.expect('repo_name .*')
p.sendline('')

p.expect('project_short_description .*')
p.sendline('Shared utilities for diffpy packages.')

p.expect('Select minimum_supported_python_version.*')
p.sendline('')

# Runs until the cookiecutter is done; then exits.
p.interact()
