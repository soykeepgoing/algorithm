import sys 
INF = sys.maxsize

def bin_search(index):
    global nums, N
    l, r = 0, N - 1
    result = INF
    result_index = [0, 0, 0]
    while l < r: 
        if index == l:
            l += 1
            continue 
        if index == r:
            r -= 1
            continue

        tmp = nums[index] + nums[l] + nums[r]
        
        if abs(tmp - 0) < abs(result - 0):
            result = tmp
            result_index = [index, l, r]

        if tmp < 0: 
            l += 1
        elif tmp > 0:
            r -= 1
        else:
            return tmp, [index, l, r]
        

    return result, result_index
        
if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    answer = INF
    answer_list = [] 

    for i, num in enumerate(nums):
        result, index_list = bin_search(i)
        if abs(answer - 0) > abs(result - 0):
            answer_list = [nums[index_list[0]], nums[index_list[1]], nums[index_list[2]]]
            answer = result

    answer_list.sort()
    print(*answer_list)