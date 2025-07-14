import math 
def check(x, y):
    distance = y - x
    max_distance = int(math.sqrt(distance))

    if max_distance == math.sqrt(distance):
        print(2 * max_distance - 1)
    elif distance <= max_distance * max_distance + max_distance:
        print(2* max_distance)
    else:
        print(2 * max_distance + 1)

if __name__ == '__main__':
    t = int(input())
 
    for _ in range(t):
        x, y = list(map(int, input().split()))
        check(x, y)
