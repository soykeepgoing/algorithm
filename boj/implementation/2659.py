def find_num(nums):
    num = 9999
    for i in range(-4, 0, 1): 
        tmp_num = nums[i % 4] * 1000 + nums[(i + 1) % 4] * 100 + nums[(i + 2) % 4] * 10 + nums[(i + 3) % 4] 
        num = min(tmp_num, num)
    return num


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    cnt = 1

    num = find_num(nums)

    for  tmp_num in range(1111, num):
        tmp_num_list = list(map(int, str(tmp_num)))
        if 0 not in tmp_num_list:
            tmp_num2 = find_num(tmp_num_list)
            # print(tmp_num, tmp_num2)
            if tmp_num == tmp_num2: 
                cnt += 1
    
    print(cnt)