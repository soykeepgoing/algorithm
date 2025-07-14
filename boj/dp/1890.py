import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))

    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            value = board[i][j]
            
            if i == N - 1 and j == N - 1: 
                print(dp[i][j])
                break 

            if (j + value) < N : 
                # print(value, i, j + value, dp[i][j])
                dp[i][j + value] += dp[i][j]
            
            if (i + value) < N: 
                # print(value, i + value, j, dp[i][j])
                dp[i + value][j] += dp[i][j]
    
    # print(dp)
    # print(dp[N - 1][N - 1])

#########################################################


# from collections import deque 
# import sys 
# input = sys.stdin.readline 

# if __name__ == '__main__':
#     N = int(input())
#     board = [] 
#     for _ in range(N):
#         board.append(list(map(int, input().split())))

#     dp = [[0 for _ in range(N)] for _ in range(N)]
#     queue = deque([(0, 0)])
    
#     while queue:
#         i, j = queue.popleft()
#         value = board[i][j]
#         if value > 0: 
#             if (j + value) in range(N): # 오른쪽 
#                 dp[i][j + value] += 1
#                 queue.append((i, j + value))
            
#             if (i + value) in range(N): # 아래쪽 
#                 dp[i + value][j] += 1
#                 queue.append((i + value, j))
#         elif (i, j) == (0, 0):
#             dp[i][j] += 1

#     print(dp[N - 1][N - 1])