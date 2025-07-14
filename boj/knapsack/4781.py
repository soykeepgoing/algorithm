import sys 
input = sys.stdin.readline 

def knapsack(candies, money):
    global T 
    dp = [0] * (money + 1)
    for i in range(T):
        cal, value = candies[i]
        for v in range(value, money + 1): # 전체 코스트에 대해서 
            dp[v] = max(cal + dp[v - value], dp[v])
    return max(dp)


if __name__ == '__main__':
    while 1: 
        T, M = map(float, input().split())
        T = int(T); M = int(M * 100 + 0.5) 
        if T == 0 and M == 0:
            break 

        candies = [] 
        for _ in range(T):
            cal, value = map(float, input().split())
            cal = int(cal); value = int(value * 100 + 0.5)
            candies.append((cal, value))
        
        result = knapsack(candies, M)
        print(result)