# https://www.hackerrank.com/challenges/maximizing-xor


def maximun_xor(l, r):
    maximun = 0
    r += 1
    for i in range(l, r):
        for j in range(i, r):
            maximun = max(maximun, i ^ j)  # ^ is xor
    return maximun

if __name__ == "__main__":
    L = input()
    R = input()
    print maximun_xor(L, R)
