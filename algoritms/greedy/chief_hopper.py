# https://www.hackerrank.com/challenges/chief-hopper


def solve(l):
    req_energy = 0
    deep = pow(2, len(l))
    for v in l:
        deep /= 2
        req_energy += (v * deep)
    q, r = divmod(req_energy, pow(2, len(l)))
    init_energy = q + (1 if r else 0)
    return init_energy


if __name__ == '__main__':
    _ = input()
    l = map(int, raw_input().split())
    print int(solve(l))
