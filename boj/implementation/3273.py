if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    first, end = 0, N-1
    cnt = 0
    nums.sort()

    while first < end:
        sum_tmp = nums[first] + nums[end]
        if sum_tmp == x:
            cnt += 1
        
        if sum_tmp > x:
            end -= 1
        else:
            first += 1
    
    print(cnt)