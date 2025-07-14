import sys 
input = sys.stdin.readline 

def bin_search(target):
    global N, num_list
    start = 0; end = N - 1
    while start <= end: 
        mid = (start + end) // 2
        mid_num = num_list[mid]
        if mid_num == target:
            return True 
        elif mid_num < target:
            start = mid + 1
        elif mid_num > target:
            end = mid - 1
    return False 

if __name__ == '__main__':
    N = int(input())
    two_sum_set = set()
    num_list = []
    for _ in range(N):
        num = int(input())
        num_list.append(num)
    num_list.sort()

    for i in range(N):
        for j in range(i, N):
            two_sum_set.add(num_list[i] + num_list[j])
    
    two_sum_list = list(two_sum_set)
    two_sum_list.sort()
    
    for i in range(N - 1, -1, -1):
        for j in range(len(two_sum_list)):
            z = num_list[i] - two_sum_list[j]
            flag = bin_search(z)
            if flag:
                print(num_list[i])
                exit()
