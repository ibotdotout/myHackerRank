# https://www.hackerrank.com/challenges/halloween-party


def get_maximun_pieces(k):
    half_a = k / 2
    half_b = k - half_a
    return half_a * half_b

if __name__ == "__main__":
    T = input()
    for i in range(T):
        k = input()
        print get_maximun_pieces(k)
