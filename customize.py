import os

# Manually modify following parameters to customize the structure of your project
path = os.path.abspath(os.path.dirname(__file__)).split("/")
USERNAME = "patel-zeel"
REPO_HOME_PATH = "/".join(path[:-1])
REPO_NAME = path[-1]
PACKAGE_NAME = REPO_NAME
BRANCH = "main"
VERSION = "0.1.0"
AUTHOR = "Zeel B Patel"
AUTHOR_EMAIL = "patel_zeel@iitgn.ac.in"
description = "example description"
URL = "https://github.com/patel-zeel/" + REPO_NAME
LICENSE = "MIT"
LICENSE_FILE = "LICENSE"
LONG_DESCRIPTION = "file: README.md"
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

full_path = os.path.join(REPO_HOME_PATH, REPO_NAME)

# Modify setup.cfg

with open(os.path.join(full_path, "setup.cfg"), "w") as f:
    f.write(f"[metadata]\n")
    f.write(f"name = {PACKAGE_NAME}\n")
    f.write(f"version = {VERSION}\n")
    f.write(f"author = {AUTHOR}\n")
    f.write(f"author-email = {AUTHOR_EMAIL}\n")
    f.write(f"description = {description}\n")
    f.write(f"url = {URL}\n")
    f.write(f"license = {LICENSE}\n")
    f.write(f"long_description_content_type = {LONG_DESCRIPTION_CONTENT_TYPE}\n")
    f.write(f"long_description = {LONG_DESCRIPTION}\n")

# Modify CI

with open(os.path.join(full_path, ".github/workflows/CI.template"), "r") as f:
    content = f.read()

with open(os.path.join(full_path, ".github/workflows/CI.yml"), "w") as f:
    content = content.replace("<reponame>", REPO_NAME)
    f.write(content)

# Modify README.md
with open(os.path.join(full_path, "README.md"), "w") as f:
    f.write(f"# {PACKAGE_NAME}\n")
    f.write(
        f"[![Coverage Status](https://coveralls.io/repos/github/{USERNAME}/{PACKAGE_NAME}/badge.svg?branch={BRANCH})](https://coveralls.io/github/{USERNAME}/{PACKAGE_NAME}/?branch={BRANCH}\n"
    )
    f.write(f"\n## Description\n")
    f.write(f"* Run `customize.py` to customize this template.\n")
    f.write(
        f"* Add PYPI_USERNAME and PYPI_PASSWORD to your secrets using GitHub GUI.\n"
    )
    f.write(f"* Manually change requirements.txt to your needs.\n")

print("Successful")
