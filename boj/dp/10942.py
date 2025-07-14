import sys 
input = sys.stdin.readline 

if __name__ == '__main__': 
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    
    dp = [[False for _ in range(N)] for _ in range(N)]

    # 자기 자신 True로 설정 
    for i in range(N): 
        dp[i][i] = True 

    for i in range(N - 2, -1, -1): 
        for j in range(N - 1, i, -1): 
            # print(i, j)
            if nums[i] == nums[j]:
                if dp[i + 1][j - 1] == True or (j - i == 1): 
                    dp[i][j] = True 

    for _ in range(M): 
        S, E = list(map(int, input().split()))
        if dp[S - 1][E - 1] == True: 
            print(1)
        else:
            print(0)
