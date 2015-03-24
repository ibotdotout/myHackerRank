# https://www.hackerrank.com/challenges/cyclicquadruples


def solve(seq):
    mod = 10 ** 9 + 7
    possible_seq = [[i] for i in range(seq[0], seq[1]+1)]
    for i in range(1, len(seq)//2):
        l, r = seq[i*2: (i+1)*2]
        tmp_seq = []
        for i in possible_seq:
            for j in range(l, r+1):
                if i[-1] != j:
                    tmp_seq.append(i + [j])
        possible_seq = tmp_seq
    return sum(i[3] != i[0] for i in possible_seq) % mod


if __name__ == '__main__':
    t = input()
    for _ in range(t):
        seq = map(int, raw_input().split())
        print solve(seq)
