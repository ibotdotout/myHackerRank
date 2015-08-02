# https://www.hackerrank.com/challenges/ip-address-validation

import re


def is_ipv4(text):
    return True if \
        re.match("((2[0-5][0-5]|2[0-4]\d|1\d{2}|[1-9]\d?)\.?){4}$", text) \
        else False


def is_ipv6(text):
    return True if \
        re.match("^([0-9Aa-f]{1,4}:?){8}$", text) else False


def solve(text):
    if is_ipv6(text):
        return "IPv6"
    elif is_ipv4(text):
        return "IPv4"
    return "Neither"

if __name__ == "__main__":
    n = input()
    for i in range(n):
        print(solve(raw_input()))
