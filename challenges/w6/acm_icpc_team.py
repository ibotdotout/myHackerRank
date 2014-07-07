# https://www.hackerrank.com/contests/w6/challenges/acm-icpc-team


def solve(l):
    ll = [int(a, 2) for a in l]  # covent binary form string to decimal
    from itertools import combinations
    two_team = [a | b for a, b in combinations(ll, 2)]  # pair two team
    know_topics = [bin(a).count('1') for a in two_team]  # count bit 1
    max_topic = max(know_topics)
    return [max_topic, know_topics.count(max_topic)]

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    team = []
    for i in range(n):
        team.append(raw_input())
    max_topic, max_team = solve(team)
    print max_topic
    print max_team
