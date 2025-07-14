if __name__ == '__main__':
    N, M, L = list(map(int, input().split()))
    nums = [0] + list(map(int, input().split())) + [L]
    nums.sort()

    start = 1; end = L - 1
    result = 0
    while start <= end:
        count = 0
        mid = (start + end) // 2 # 세울 수 있는 휴게소의 최대 거리
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > mid: # 
                count += (nums[i] - nums[i - 1] - 1) // mid 
        
        if count > M: # 최댓값을 찾기 위해 값을 늘리기 
            start = mid + 1
        else: # 최댓값의 최솟값을 찾기 위해 값을 줄이기 
            end = mid - 1
            result = mid
    
    print(result)