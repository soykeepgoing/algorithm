if __name__  == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    answer = 0 
    tmp = 0 
    if N == 1: 
        nums.sort()
        answer = sum(nums) - nums[5]
    else:
        min_nums = [] 
        min_nums.append(min(nums[0], nums[5]))
        min_nums.append(min(nums[1], nums[4]))
        min_nums.append(min(nums[2], nums[3]))
        min_nums.sort()

        for i in range(3):
            tmp += min_nums[i]
            if i == 0:
                count = ((N - 2) * (N - 1) * 4) + ((N - 2) * (N - 2))
            elif i == 1: 
                count = 4 * (N - 1) + 4 * (N - 2)
            elif i == 2: 
                count = 4

            answer += count * tmp
    
    print(answer)