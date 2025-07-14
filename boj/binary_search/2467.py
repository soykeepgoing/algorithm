import sys 
INF = sys.maxsize

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    left = 0; right = N - 1
    ans = INF

    while left < right:
        value = nums[left] + nums[right]

        if abs(value) < ans:
            left_ans = left
            right_ans = right
            ans = abs(value)

        if value < 0:
            left += 1
        elif value > 0:
            right -= 1
        else:
            print(nums[left], nums[right])
            exit()

    print(nums[left_ans], nums[right_ans])
    