# https://www.hackerrank.com/challenges/gem-stones


def get_number_of_gem_elements(rocks):
    gem_elements = 0
    min_rock = "".join(set(min(rocks)))  # remove char duplicated
    for char in min_rock:
        is_gem = all(map(lambda x: char in x, rocks))
        if is_gem:
            gem_elements += 1
    return gem_elements

if __name__ == "__main__":
    N = input()
    rocks = []
    for i in range(N):
        rock = raw_input()
        rocks.append(rock)
    print get_number_of_gem_elements(rocks)
