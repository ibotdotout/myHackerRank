# https://www.hackerrank.com/challenges/cyclicquadruples
# solution
# http://hr-filepicker.s3.amazonaws.com/infinitum-may14/477-cyclicquadruples.pdf
# not implement yet


def overlap_range(p1, p2):
    if p1 and p2:
        p1, p2 = sorted((p1, p2))
        x, y = p1
        a, b = p2
        if a <= y and a >= x:
            return (a, min(y, b))
    return None


def overlap_set(prev_set, new_set):
    return [overlap_range(p, n) for p, n in zip(prev_set, new_set)]


def range_set(sets):
    return map(lambda x: (x[1] + 1) - x[0] if x else 0, sets)


def solve(seq):
    # mod = 10 ** 9 + 7
    sets = [seq[i*2: (i+1)*2] for i in range(len(seq)//2)]

    overlap = [sets]
    for i in range(3):
        new_sets = sets[i+1:] + sets[0:i+1]
        ov = overlap_set(overlap[-1], new_sets)
        overlap.append(ov)


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        seq = map(int, raw_input().split())
        print solve(seq)
