# https://www.hackerrank.com/challenges/time-conversion


def solve(t):
    is_pm = t[-2:] == "PM"
    hh = int(t[:2])
    hh = str(hh + 12) if is_pm and hh < 12 else hh
    hh = 0 if not is_pm and hh == 12 else hh
    return str(hh).rjust(2, '0') + t[2:-2]

if __name__ == '__main__':
    time = raw_input().strip()
    print(solve(time))
