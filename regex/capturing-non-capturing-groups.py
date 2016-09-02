# https://www.hackerrank.com/challenges/capturing-non-capturing-groups

import re

Regex_Pattern = r'(ok){3,}'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
