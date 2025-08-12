'''
세준이는 0에 있고 사람들이 마구 놓은 책도 전부 0에 있다. 
책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다. 

7 2
-39 -37 -29 -28 -6 0 2 11
-34 -32 4 2 34

-34 -32 

'''

import sys 
import heapq
input = sys.stdin.readline 

def clear_heap(h):
    for __ in range(m):
        if not h: break 
        heapq.heappop(h)

def get_new_answer(answer, value):
    value *= (-1)
    if answer == 0:
        answer = value 
    else:
        answer += value * 2
    return answer 

def solution():
    answer = 0 
    while True:
        # print(pos_nums, neg_nums)
        if not pos_nums and not neg_nums:
            break 

        max_pos_num, max_neg_num = 10e9, 10e9 
        if pos_nums:
            max_pos_num = pos_nums[0][0]
        if neg_nums:
            max_neg_num = neg_nums[0][0]
        
        # print(max_pos_num, max_neg_num)

        if max_pos_num != 10e9 and max_neg_num != 10e9:
            if max_pos_num < max_neg_num:
                answer = get_new_answer(answer, max_pos_num)
                clear_heap(pos_nums)
            else:
                answer = get_new_answer(answer, max_neg_num)
                clear_heap(neg_nums)
        elif max_pos_num == 10e9 and max_neg_num != 10e9:
            answer = get_new_answer(answer, max_neg_num)
            clear_heap(neg_nums)
        elif max_pos_num != 10e9 and max_neg_num == 10e9:
            answer = get_new_answer(answer, max_pos_num)
            clear_heap(pos_nums)

    return answer


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    pos_nums, neg_nums = [], [] 
    for num in nums: 
        if num > 0: 
            heapq.heappush(pos_nums, (-num, num))
        else:
            heapq.heappush(neg_nums, (num, num))

    answer = solution()
    print(answer)
