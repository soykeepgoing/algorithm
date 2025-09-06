'''
기존 풀이보다 10배 더 빠른 dp를 활용한 풀이 
dp는 (n, n, 3)으로 3가지 방향 (가로, 세로, 대각선)에 대한 방법의 경우의 수를 메모이제션한다음, 
조건분기들로 각 방법들의 경우의 수를 더해가는 방식으로 풀이하면 된다. 
'''
def solution():
    for x in range(n):
        for y in range(1, n):
            # 가로 더하기 
            if y + 1 < n and board[x][y + 1] == 0:
                dp[x][y + 1][0] += dp[x][y][0]
            if x + 1 < n and y + 1 < n: 
                if board[x + 1][y + 1] == 0 and board[x][y + 1] == 0 and board[x + 1][y] == 0:
                    dp[x + 1][y + 1][2] += dp[x][y][0]

            # 세로 더하기 
            if x + 1 < n and board[x + 1][y] == 0:
                dp[x + 1][y][1] += dp[x][y][1]
            if x + 1 < n and y + 1 < n: 
                if board[x + 1][y + 1] == 0 and board[x][y + 1] == 0 and board[x + 1][y] == 0:
                    dp[x + 1][y + 1][2] += dp[x][y][1]

            # 대각선 더하기 
            if y + 1 < n and board[x][y + 1] == 0:
                dp[x][y + 1][0] += dp[x][y][2]
            if x + 1 < n and board[x + 1][y] == 0:
                dp[x + 1][y][1] += dp[x][y][2]
            if x + 1 < n and y + 1 < n: 
                if board[x + 1][y + 1] == 0 and board[x][y + 1] == 0 and board[x + 1][y] == 0:
                    dp[x + 1][y + 1][2] += dp[x][y][2]

    return dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1] + dp[n - 1][n - 1][2]

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for __ in range(n)]
    dp = [[[0, 0, 0] for __ in range(n)]for __ in range(n)]
    dp[0][1][0] = 1 # 가로 파이프가 존재 
    if board[n - 1][n - 1] == 1: 
        print(0)
    else:
        ans = solution()
        print(ans)
