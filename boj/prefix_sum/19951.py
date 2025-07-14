import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    nums = [0] + list(map(int, input().split()))
    prefix_sums = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b, k = list(map(int, input().split()))
        prefix_sums[a] += k 
        if b + 1 in range(N + 1):
            prefix_sums[b + 1] += (-1) * k
    
    # print(prefix_sums)

    for i in range(1, N + 1):
        prefix_sums[i] = prefix_sums[i] + prefix_sums[i - 1]

    # print(prefix_sums)

    for i in range(1, N + 1):
        nums[i] += prefix_sums[i] 
    
    print(*nums[1:])