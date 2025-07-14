import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_dp = board[0][:] 
    min_dp = board[0][:]

    for i in range(1, N):
        prev_max_dp = max_dp[:]
        prev_min_dp = min_dp[:]

        max_dp[0] = board[i][0] + max(prev_max_dp[0], prev_max_dp[1])
        max_dp[1] = board[i][1] + max(prev_max_dp[0], prev_max_dp[1], prev_max_dp[2])
        max_dp[2] = board[i][2] + max(prev_max_dp[1], prev_max_dp[2])

        min_dp[0] = board[i][0] + min(prev_min_dp[0], prev_min_dp[1])
        min_dp[1] = board[i][1] + min(prev_min_dp[0], prev_min_dp[1], prev_min_dp[2])
        min_dp[2] = board[i][2] + min(prev_min_dp[1], prev_min_dp[2])

    print(max(max_dp), min(min_dp))