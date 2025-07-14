import itertools 
from collections import deque 
import sys 

input = sys.stdin.readline
DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = sys.maxsize

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    chicken_shops = []
    houses = []
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(N):
            if board[i][j] == 2:
                chicken_shops.append([i, j])
            if board[i][j] == 1:
                houses.append([i, j])

    sampled_chicken_shops = list(itertools.combinations(chicken_shops, M))

    ans = INF

    for sampled_chicken_shop in sampled_chicken_shops:
        dp = [[INF for _ in range(N)] for _ in range(N)]

        queue = deque(sampled_chicken_shop)

        for chicken_shop in sampled_chicken_shop:
            dp[chicken_shop[0]][chicken_shop[1]] = 0 

        while queue:
            i, j = queue.popleft()
            distance_now = dp[i][j]

            for di, dj in DIRECTION:
                new_i = i + di; new_j = j + dj 
                if new_i in range(N) and new_j in range(N):
                    if dp[new_i][new_j] > distance_now + 1:
                        queue.append([new_i, new_j])
                        dp[new_i][new_j] = distance_now + 1
        
        tmp = 0
        for house in houses:
            tmp += dp[house[0]][house[1]]

        ans = min(ans, tmp)
    
    print(ans)

    

