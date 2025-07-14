def bin_search(x, i):
    global N, nums
    l, r = 0, N - 1

    while l < r: 

        if l == i: 
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        tmp = nums[l] + nums[r]
        if tmp == x: 
            return 1 
        elif tmp < x:
            l += 1
        elif tmp > x: 
            r -= 1
    return 0 

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    count = 0 
    for i, num in enumerate(nums):
        count += bin_search(num, i)
    print(count)