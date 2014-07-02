# https://www.hackerrank.com/challenges/encryption


def encode(w):
    import math
    width = int(math.ceil(math.sqrt(len(w))))  # upper sqrt(len(w))
    encoded_word = ' '.join([w[i::width] for i in range(width)])
    return encoded_word

if __name__ == "__main__":
    print encode(raw_input())
