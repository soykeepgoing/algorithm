def get_sorted_array(array):
    new_array = []
    for i in range(len(array)):
        new_array.append((i, array[i]))
    new_array.sort(key = lambda x: (-x[1], x[0])) # 내림차순, 오름차순 
    return new_array

def print_array(array):
    new_array = []
    for i in range(len(array)):
        new_array.append(array[i][2])
    print(*new_array)

def solution():
    A_sorted = get_sorted_array(A)
    B_sorted = get_sorted_array(B)

    # print(A_sorted)
    # print(B_sorted)

    pointer_A, pointer_B = 0, 0
    nums = [] 

    while pointer_A < A_len and pointer_B < B_len:
        index_A, value_A = A_sorted[pointer_A]
        index_B, value_B = B_sorted[pointer_B]

        if value_A > value_B:
            pointer_A += 1 
        elif value_A < value_B:
            pointer_B += 1
        else: ## 값이 같다면 
            if len(nums) == 0:
                nums.append((index_A, index_B, value_A))
                pointer_A += 1
                pointer_B += 1
            else:
                pre_index_A, pre_index_B, pre_value = nums[-1]
                if pre_index_A < index_A and pre_index_B < index_B:
                    nums.append((index_A, index_B, value_A))
                    pointer_A += 1
                    pointer_B += 1
                if pre_index_A > index_A:
                    pointer_A += 1
                if pre_index_B > index_B:
                    pointer_B += 1

    return len(nums), nums


if __name__ == '__main__':
    A_len = int(input())
    A = list(map(int, input().split()))
    B_len = int(input())
    B = list(map(int, input().split()))

    K, array = solution()
    print(K)
    if K != 0:
        print_array(array)
