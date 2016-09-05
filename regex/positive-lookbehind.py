# https://www.hackerrank.com/challenges/positive-lookbehind

import re

Test_String = input()

Regex_Pattern = r"(?<=[13579])\d"

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
