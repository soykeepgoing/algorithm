if __name__ == '__main__':
    C, N = list(map(int, input().split()))
    data = [] 
    for _ in range(N):
        data.append(list(map(int, input().split())))
    C_max = C + 100
    dp = [[1e9] * (C_max) for _ in range(N + 1)]
    
    for i in range(N + 1):
        dp[i][0] = 0

    for i in range(1, N + 1): 
        cost, human = data[i - 1]
        for j in range(1, C_max):
            dp[i][j] = dp[i - 1][j]
            if j >= human: 
                dp[i][j] = min(dp[i][j], dp[i][j - human] + cost)

    print(min(dp[N][C:]))
   