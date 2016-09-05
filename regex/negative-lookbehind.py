# https://www.hackerrank.com/challenges/negative-lookbehind

import re

Test_String = input()

Regex_Pattern = r"(?<![aeiouAEIOU])."

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
