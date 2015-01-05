# https://www.hackerrank.com/challenges/bus-station


def solve(l):
    x = []
    acc_l = []
    max_l = 0
    cum = 0
    for d in l:
        if d > max_l:
            max_l = d
        cum += d
        acc_l.append(cum)
    total = cum
    for i in acc_l:
        if i < max_l or total % i != 0:
            continue
        in_trip = 0
        for d in l:
            in_trip += d
            if in_trip > i:
                break
            elif in_trip == i:
                in_trip = 0
        else:
            if in_trip == 0:
                x.append(i)
    return x


if __name__ == '__main__':
    _ = input()
    l = tuple(int(i) for i in raw_input().split())
    print " ".join(tuple(str(i) for i in solve(l)))
