# import sys 
# import heapq
# INF = sys.maxsize
# input = sys.stdin.readline 

# def bin_search(target_index, target_num):
#     start = 0; end = N - (target_index + 1)
#     ans = INF 

#     while start < end:
#         mid = (start + end) // 2
#         tmp_index, tmp_num = nums_sort[mid]

#         # print(target_index, target_num, tmp_index, tmp_num)

#         if tmp_num <= target_num:
#             end = mid - 1
#         else:
#             start = mid + 1
#             ans = min(tmp_num, ans)
    
#     if ans == INF:
#         ans = -1

#     return ans 
        

# if __name__ == '__main__':
#     N = int(input())
#     nums = list(map(int, input().split()))

#     nums_sort = [] 
#     for i, num in enumerate(nums):
#         nums_sort.append((i, num))
#     heapq.heapify(nums_sort)

#     res_list = [] 
#     for i in range(N):
#         heapq.heappop(nums_sort)
#         nums_sort.sort(key = lambda x: x[1])
#         res = bin_search(i, nums[i])
#         res_list.append(res)

#     print(*res_list)

import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    results = [-1] * n 
    stack = [] # 인덱스 저장  

    for i in range(n):
    
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop() 
            results[idx] = nums[i]

        stack.append(i)
    
    print(*results)


    # stack = [] 
    # stack_len = 0
    # results = [] 

    # while len(nums) > 0: 
    #     tmp = nums.pop()
    #     if len(results) == 0: # 마지막인 경우 
    #         stack.append(tmp)
    #         results.append(-1)
    #     else:
    #         flag = False
    #         for i in range(stack_len, -1, -1):
    #             stack_num = stack[i] 
    #             if stack_num > tmp:
    #                 results.append(stack_num)
    #                 flag = True 
    #                 break 
            
    #         if not flag:
    #             results.append(-1)
            
    #         stack.append(tmp)
    #         stack_len += 1

    # print(*results[::-1])