# https://www.hackerrank.com/challenges/runningtime


def get_shifted_number(l):
    result = 0
    for i in range(1, len(l)):
        val = l[i]
        k = i - 1
        while k >= 0 and l[k] > val:
            l[k+1] = l[k]
            k -= 1
            result += 1
        l[k+1] = val
    return result

if __name__ == "__main__":
    n = input()
    print get_shifted_number(map(int, raw_input().split()))
