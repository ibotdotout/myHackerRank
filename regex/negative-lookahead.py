# https://www.hackerrank.com/challenges/negative-lookahead

import re

Test_String = input()

Regex_Pattern = r"(.)(?!\1)"Regex_Pattern# Do not delete 'r'.

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
