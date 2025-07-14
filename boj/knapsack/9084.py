import sys 
input = sys.stdin.readline 

def knapsack(coins, M):
    dp = [0 for _ in range(10000 + 1)]
    dp[0] = 1

    for coin in coins:
        dp[coin] += 1
        for i in range(coin + 1, 10000 + 1):
            if dp[i - coin] > 0: 
                dp[i] += dp[i - coin]

    return dp[M]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = list(map(int, input().split()))
        M = int(input())
        ans = knapsack(coins, M)
        print(ans)