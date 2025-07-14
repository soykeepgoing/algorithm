import heapq 

if __name__ == '__main__':
    N = int(input())
    nums = [] 
    for _ in range(N):
        M = int(input())
        heapq.heappush(nums, M)

    ans = 0 

    while len(nums) >= 2: 
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        ans += a + b 
        heapq.heappush(nums, a + b)

    print(ans)

