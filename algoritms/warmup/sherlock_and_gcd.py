# https://www.hackerrank.com/challenges/sherlock-and-gcd


def sherlock_gcd(l):
    import fractions
    gc = l[0]
    for i in l[1:]:
        gc = fractions.gcd(gc, i)
    if gc == 1:
        return True
    return False

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        l = map(int, raw_input().split())
        print('YES' if sherlock_gcd(l) else 'NO')
