# https://www.hackerrank.com/challenges/matching-x-y-repititions

import re

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
