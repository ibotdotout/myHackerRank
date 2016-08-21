# https://www.hackerrank.com/challenges/excluding-specific-characters

import re

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.,]$' # Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, input()))).lower())
