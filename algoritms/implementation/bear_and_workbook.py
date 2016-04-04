# https://www.hackerrank.com/challenges/bear-and-workbook

import math


def solve(n, k, t):
    special, current = 0, 0
    for i in t:
        chapter_page = int(math.ceil(i/float(k)))
        problem_page = [0] + [min(p * k, i) for p in range(1, chapter_page+1)]
        special += sum([1 for p in range(1, len(problem_page))
                       if problem_page[p-1] < current + p <= problem_page[p]])
        current += chapter_page
    return special

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    t = map(int, raw_input().split())
    print solve(n, k, t)
