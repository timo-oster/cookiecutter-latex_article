#!/usr/bin/env python3

import sys
from subprocess import run, CalledProcessError

try:
    run(["git", "init"], check=True)
    run(["git" "config" "user.name" "{{cookiecutter.full_name}}"])
    run(["git" "config" "user.email" "{{cookiecutter.email}}"])
except CalledProcessError as e:
    sys.exit(1)
