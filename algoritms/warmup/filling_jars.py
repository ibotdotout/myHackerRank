# https://www.hackerrank.com/challenges/filling-jars


def fill_jars(a, b, k):
    return (b - a + 1) * k

if __name__ == "__main__":
    N, M = map(int, raw_input().split())
    jar = 0
    for i in range(M):
        a, b, k = map(int, raw_input().split())
        jar += fill_jars(a, b, k)
    mean = jar/N
    print int(mean)
