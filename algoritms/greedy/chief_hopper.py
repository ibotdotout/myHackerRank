# https://www.hackerrank.com/challenges/chief-hopper

import math


def solve(l):
    """"
    Start at the end and trace back
    We backtrack from the end and determine the energy needed to clear the
    buildings ahead.

    solution by https://www.hackerrank.com/ethan_t_sterling
    """

    init_energy = 0
    for v in reversed(l):
        init_energy = math.ceil((v + init_energy) / 2)
    return init_energy


if __name__ == '__main__':
    _ = input()
    l = map(int, raw_input().split())
    print int(solve(l))
