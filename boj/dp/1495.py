import sys 
input = sys.stdin.readline 

def solution(dp, present_volumes):
    for i in range(1, N + 1):
        flag = False
        for present_volume in range(M + 1):
            if dp[i - 1][present_volume] == True: 
                if present_volume + volumes[i] in range(0, M + 1):
                    flag = True 
                    dp[i][present_volume + volumes[i]] = True 

                if present_volume - volumes[i] in range(0, M + 1):
                    flag = True 
                    dp[i][present_volume - volumes[i]] = True       

        if not flag:
            return -1

    for i in range(M, -1, -1):
        if dp[N][i] == True:
            return i 


if __name__ == '__main__':
    global N, S, M

    N, S, M = list(map(int, input().split()))
    volumes = [0] + list(map(int, input().split()))

    dp = [[False for _ in range(M + 1)] for _ in range(N + 1)] 
    dp[0][S] = True 
    present_volumes = [S]
    ans = solution(dp, present_volumes)

    print(ans)