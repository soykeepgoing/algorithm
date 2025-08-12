import sys 
input = sys.stdin.readline 

def solution():
    global s
    for i in range(n):
        max_num = max(nums[i:min(n, i + s + 1)])
        max_idx = nums.index(max_num)
        for j in range(max_idx, i, -1):
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        s -= (max_idx - i)
        if s <= 0: break 
    return nums

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    s = int(input())
    answer = solution()
    print(*answer)
