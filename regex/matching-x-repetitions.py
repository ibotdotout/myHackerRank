# https://www.hackerrank.com/challenges/matching-x-repetitions

import re

Regex_Pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
