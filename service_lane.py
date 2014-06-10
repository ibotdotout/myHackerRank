# https://www.hackerrank.com/challenges/service-lane

def get_largest_vehicle_type(lane, i, j):
    return min(lane[i:j+1])

if __name__ == "__main__":
    N, T = map(int, raw_input().split())
    lane = map(int, raw_input().split())
    for i in range(T):
        i, j = map(int, raw_input().split())
        print get_largest_vehicle_type(lane, i, j)
