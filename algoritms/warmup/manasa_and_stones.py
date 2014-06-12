# https://www.hackerrank.com/challenges/manasa-and-stones


def manasa_stones(_input):
    level = _input[0]
    a, b = _input[1:]
    result = [(i * a + (level - i - 1) * b) for i in range(level)]
    return sorted(set(result))

if __name__ == "__main__":
    T = input()
    for i in range(T):
        n = input()
        a = input()
        b = input()
        print ' '.join(map(str, manasa_stones([n, a, b])))
