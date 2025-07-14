import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

def search(maps, x, y):
    global dp 

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    N = len(maps); M = len(maps[0])

    if x == (M - 1) and y == (N - 1):
        return 1
    
    if dp[y][x] == -1:
        dp[y][x] = 0 
        for dx, dy in directions: 
            x_new = x + dx 
            y_new = y + dy

            if x_new in range(M) and y_new in range(N):
                if maps[y_new][x_new] < maps[y][x]:
                    dp[y][x] += search(maps, x_new, y_new)
    return dp[y][x]

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    maps = [] 
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    dp = [[-1  for _ in range(M)] for _ in range(N)]
    count = search(maps, 0, 0)
    print(count)