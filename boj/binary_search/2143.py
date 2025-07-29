'''

부배열의 합 구하기 

    1 2 3 4
1   1 4 5 7
2     3 4 5
3       1 3
4         2

    1 2 3
1   1 4 6
2     3 5
3       2


1 1 2 3 3 4 4 5 5 7

1 2
2 1
3 2
4 2
5 2
7 1
================
1 2 3 4 5 6 < 이분 탐색 

-10000
4
-1000000 -1000000 -1000000 -1000000
6
-1000000 -1000000 -1000000 1000000 1000000 -1000000


4
3
7 8 5
2
-1 -2 1

'''
def get_sum(array):
    array_len = len(array)
    dp = [[0 for __ in range(array_len)] for __ in range(array_len)]
    dp = []
    for i in range(1, array_len):
        acc_sum = array[i]
        dp.append(acc_sum)
        for j in range(i + 1, array_len):
            acc_sum += array[j]
            dp.append(acc_sum)
    return dp

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid 
    return left

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid 
    return left

def search(array, target):
    upper = upper_bound(array, target)
    lower = lower_bound(array, target)
    return upper - lower

def solution():
    dp_A = get_sum(A_nums)
    dp_B = get_sum(B_nums)
    answer = 0
    # print(dp_A)
    # print(dp_B)

    dp_A.sort()
    dp_B.sort()

    for a in dp_A:
        target = T - a
        answer += 1 * search(dp_B, target)
    
    return answer

if __name__ == '__main__':
    T = int(input())
    N = int(input())
    A_nums = [0] + list(map(int, input().split()))
    M = int(input())
    B_nums = [0] + list(map(int, input().split()))
    answer = solution()
    print(answer)
