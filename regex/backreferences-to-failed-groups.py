# https://www.hackerrank.com/challenges/backreferences-to-failed-groups

import re

Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"

print(str(bool(re.search(Regex_Pattern, input()))).lower())
