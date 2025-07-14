import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    data = list(map(int, input().split()))

    ans = 0 
    sum = []
    sum.append(data[0])

    for i in range(1, N):
        sum.append(sum[i - 1] + data[i])
    
    # 벌통 - 1벌 - 2벌 
    # 이 경우, 벌통은 무조건 제일 왼쪽, 2벌은 무조건 제일 오른쪽
    # i는 1벌의 위치
    for i in range(1, N - 1):  
        bee1 = sum[i - 1]
        bee2 = sum[N - 2] - data[i]
        ans = max(ans, bee1 + bee2)
    
    # 1벌 - 2벌 - 벌통 
    # 이 경우, 벌통은 무조건 제일 오른쪽, 1벌은 무조건 제일 왼쪽
    # i는 2벌의 위치
    for i in range(1, N - 1):
        bee1 = sum[N - 1] - data[0] - data[i]
        bee2 = sum[N - 1] - sum[i]
        ans = max(ans, bee1 + bee2)

    # 1벌 - 벌통 - 2벌 
    # 1벌과 2벌은 무조건 제일 왼쪽 - 오른쪽 
    # i는 벌통의 위치
    for i in range(1, N - 1):
        # ans = max(ans, sum[N - 2] - data[0] + data[i])
        bee1 = sum[i] - data[0]
        bee2 = sum[N - 2] - sum[i] + data[i]
        ans = max(ans, bee1 + bee2)
    
    print(ans)