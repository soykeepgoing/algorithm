import sys
input = sys.stdin.readline 

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    coins = [] 
    for _ in range(n):
        coins.append(int(input()))
    coins.sort(reverse=True)

    max_coin = 10**5
    dp = [max_coin] * 10001
    dp[0] = 0 

    for coin in coins: 
        for value in range(coin, k + 1): 
            dp[value] = min(dp[value], dp[value - coin] + 1)
    
    if dp[k] == max_coin: 
        print(-1)
    else: 
        print(dp[k])
