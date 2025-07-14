if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    coins = [] 
    for _ in range(n):
        coins.append(int(input()))
    coins.sort()

    dp = [0 for _ in range(k + 1)]
    dp[0] = 1
    for coin in coins: 
        for value in range(coin, k + 1): 
            dp[value] += dp[value - coin]

    print(dp[k])