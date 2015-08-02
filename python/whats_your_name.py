# https://www.hackerrank.com/challenges/whats-your-name


def into_python(name, lastname):
    return "Hello {0} {1}! You just delved " \
           "into python.".format(name, lastname)


if __name__ == "__main__":
    name = raw_input()
    lastname = raw_input()
    print into_python(name, lastname)
