import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    left = 0; right = N - 1
    min_value = 1e12
    ans1, ans2 = 0,0

    while left < right:
        tmp_value = abs(nums[left] + nums[right])
        if tmp_value <= min_value:
            min_value = tmp_value
            ans1 = nums[left]
            ans2 = nums[right]

        # print(left, right, tmp_value, min_value)

        if abs(nums[left]) < abs(nums[right]):
            right -= 1
        else:
            left += 1

    print(ans1, ans2)

