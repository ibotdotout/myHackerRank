# https://www.hackerrank.com/challenges/utopian-tree

def growth(num):
    result = 1
    for i in range(num):
        if i % 2 == 0:
            result = result*2
        else:
            result = result+1
    return result

if __name__ == "__main__":
    T = input()
    for i in range(T):
        N = input()
        print(growth(N))
