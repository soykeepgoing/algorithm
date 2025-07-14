import math 

def find_kth_permutation(N, k):
    nums = list(range(1, N + 1))
    result = []
    k -= 1
    for i in range(N):
        fact = math.factorial(N - i - 1)
        index = k // fact 
        result.append(nums.pop(index))
        k %= fact 
    return result 

def find_permutation_order(N, perm):
    nums = list(range(1, N + 1))
    order = 0 
    for i in range(N):
        index = nums.index(perm[i])
        order += index * math.factorial(N - i -1)
        nums.pop(index)
    return order + 1

if __name__ == '__main__':
    N = int(input())
    order = list(map(int, input().split()))

    if order[0] == 1:
        k = order[1]
        print(*find_kth_permutation(N, k))
    else:
        perm = order[1:]
        print(find_permutation_order(N, perm))
