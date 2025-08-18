import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution():
    def dfs(x, y):
        if dp[x][y] > 0:
            return dp[x][y]
        dp[x][y] = 1 
        for dx, dy in direction:
            new_x, new_y = x + dx, y + dy 
            if 0 <= new_x < n and 0 <= new_y < n:
                if board[x][y] < board[new_x][new_y]:
                    dp[x][y] = max(dp[x][y], dfs(new_x, new_y) + 1)
        return dp[x][y]

    max_answer = 0 
    dp = [[0] * n for __ in range(n)]
    for x in range(n):
        for y in range(n):
            if not dp[x][y]:
                max_answer = max(max_answer, dfs(x, y))
    return max_answer


if __name__ == '__main__':
    n = int(input())
    board = [] 
    for __ in range(n):
        board.append(list(map(int, input().split())))
    answer = solution()
    print(answer)
