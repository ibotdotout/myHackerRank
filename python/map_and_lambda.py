# https://www.hackerrank.com/challenges/map-and-lambda-expression


def cube_fibo(n):
    fibo = [0, 1]
    while len(fibo) < n:
            fibo.append(fibo[-1] + fibo[-2])
    return map(lambda x: x**3, fibo)[:n]

if __name__ == '__main__':
    n = input()
    print cube_fibo(n)
