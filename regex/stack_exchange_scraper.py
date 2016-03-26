# https://www.hackerrank.com/challenges/stack-exchange-scraper

import re
import sys


def solve(text):
    regex = r'(?s)<h3><a href="/questions/(\d+)/.*?"' \
            ' class="question-hyperlink">(.+?)</a></h3>' \
            '.*?class="relativetime">(.*?)</span>'
    id_topic = re.findall(regex, text)
    return "\n".join([";".join(i) for i in id_topic])

if __name__ == "__main__":
    print solve(sys.stdin.read())
