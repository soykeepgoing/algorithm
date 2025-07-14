from collections import deque 
import sys 
input = sys.stdin.readline 

def search(start, end):
    dp = [0 for _ in range(start, end)]
    dp[0] = 1
    
    if len(dp) == 1: 
        return 1

    dp[1] = 1
    for n in range(2, (end - start)):
        dp[n] = dp[n - 1] + dp[n - 2]

    return dp[-1]

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    
    vips = deque([]) 
    for _ in range(M):
        vips.append(int(input()))
    
    if N == 1: 
        print(1)
        exit()
    
    s = 0
    ans = 1
    while vips: 
        vip = vips.popleft()
        value = search(s, vip)
        ans = ans * value
        s = vip

    # 마지막 차례 
    if s != N:
        value = search(s, N + 1)
        ans = ans * value 

    print(ans)