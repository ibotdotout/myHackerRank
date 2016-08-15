# https://www.hackerrank.com/challenges/matching-start-end

import re

Regex_Pattern = r"^\d\w{1,4}\.$"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
