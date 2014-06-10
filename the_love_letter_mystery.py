# https://www.hackerrank.com/challenges/the-love-letter-mystery


def get_reduce_number_to_palindrome(text):
    reduced = 0
    for p in range(len(text)/2):
        reduced += abs(ord(text[p]) - ord(text[-p-1]))
    return reduced

if __name__ == "__main__":
    T = input()
    for i in range(T):
        text = raw_input()
        print get_reduce_number_to_palindrome(text)
