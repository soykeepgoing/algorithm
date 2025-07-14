import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    mem_list = list(map(int, input().split()))
    cost_list = list(map(int, input().split()))
    
    max_cost = sum(cost_list)
    dp = [0] * (max_cost + 1) # 해당 비용으로 확보할 수 있는 최대 메모리 

    for i in range(N):
        mem = mem_list[i]; cost = cost_list[i]
        for j in range(max_cost, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + mem)

    for cost in range(max_cost + 1):
        if dp[cost] >= M:
            print(cost)
            break 