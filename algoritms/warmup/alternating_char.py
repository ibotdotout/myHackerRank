# https://www.hackerrank.com/challenges/alternating-characters


def solve(text):
    return sum([1 if p == c else 0 for p, c in zip(text[:-1], text[1:])])

if __name__ == "__main__":
    t = input()
    for i in range(t):
        print solve(raw_input())
