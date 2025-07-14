if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 3 

    pre = 1
    for n in range(2, N + 1):
        dp[n] = (dp[n - 1] + (dp[n - 1] - pre) * 2) % 9901
        # print(n, dp[n])
        pre = dp[n - 1] - pre

    print(dp[N])