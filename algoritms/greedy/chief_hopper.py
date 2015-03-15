# https://www.hackerrank.com/challenges/chief-hopper


def solve(l):
    req_energy = 0
    deep = pow(2, len(l))
    ddeep = deep
    for v in l:
        deep /= 2
        req_energy += (v * deep)
    init_energy = (req_energy / ddeep) + (1 if req_energy % ddeep else 0)
    return init_energy


if __name__ == '__main__':
    _ = input()
    l = map(int, raw_input().split())
    print int(solve(l))
