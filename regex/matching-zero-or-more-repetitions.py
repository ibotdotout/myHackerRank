# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions

import re

Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
