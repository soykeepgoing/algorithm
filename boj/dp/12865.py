if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    data = [[]]
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for _ in range(N):
        W, V = list(map(int, input().split()))
        data.append([W, V])

    for i in range(1, N + 1):
        weight = data[i][0]; value = data[i][1] 
        for j in range(1, K + 1):
            if j >= weight: 
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[-1][-1])