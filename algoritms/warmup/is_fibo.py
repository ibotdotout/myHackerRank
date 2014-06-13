# https://www.hackerrank.com/challenges/is-fibo


def is_fibo(fibo_list, n):
    return n in fibo_list


def fibo_list(n):
    a, b = 0, 1
    fibo_list = [a, b]
    while a+b < n:
        fibo_list.append(a+b)
        a, b = b, a + b
    return fibo_list


if __name__ == "__main__":
    T = input()
    l = fibo_list(10**10)
    for i in range(T):
        n = input()
        print('IsFibo' if is_fibo(l, n) else 'IsNotFibo')
