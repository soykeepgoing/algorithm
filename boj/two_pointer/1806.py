import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N, S = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    start = 0 
    total = 0 # 누적합
    ans = N + 1 # 최단 수열의 길이 
    for end in range(N):
        total += nums[end]
        while total >= S: # 누적합이 주어진 S 이상인 경우
            ans = min(ans, end - start + 1) # 최단 수열의 길이 업데이트
            total -= nums[start] 
            start += 1 # start 포인터 이동 

    if ans == N + 1:
        print(0)
    else: 
        print(ans)