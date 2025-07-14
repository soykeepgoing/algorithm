if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    tmp_sum = sum(nums[:K])
    ans = tmp_sum
    start = 0 
    for end in range(K, N):
        tmp_sum = tmp_sum - nums[start] + nums[end]
        ans = max(tmp_sum, ans)
        start += 1
    
    print(ans)