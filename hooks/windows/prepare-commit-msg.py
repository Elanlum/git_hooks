"""
This script is designed in order to produce lightweight prefixing of commit message
depending on current branch name (e.g. Jira ticket number).

by Elanlum
"""

import re
import sys
from subprocess import check_output

commit_msg_filepath = sys.argv[1]
branch = (
    check_output(["git", "symbolic-ref", "--short", "HEAD"]).decode("utf-8").strip()
)

regex = r"^[A-Z]{1,9}-[0-9]{1,9}"

foundObj = re.match(regex, branch)

if foundObj:
    prefix = foundObj.group(0)
    with open(commit_msg_filepath, "r+") as f:
        commit_msg = f.read()
        if commit_msg.find(prefix) == -1:
            f.seek(0, 0)
            f.write(f"[{prefix}] {commit_msg}")
