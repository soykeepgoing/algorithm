import sys 

INF = 100000
# INF = 30

if __name__ == '__main__':
    D, K = list(map(int, input().split()))

    dp = [[0, 0] for _ in range(D + 1)]
    dp[1] = [1, 0]
    dp[2] = [0, 1]
    dp[3] = [1, 1]

    for i in range(4, D + 1):
        a = dp[i - 1][0] + dp[i - 2][0]
        b = dp[i - 1][1] + dp[i - 2][1]
        dp[i] = [a, b]
        # print(a, b)

    a, b = dp[D]
    # print(a, b)

    for i in range(1, INF):
        K_ = K - a * i
        if K_ % b == 0:
            print(i)
            print(K_ // b)
            exit()