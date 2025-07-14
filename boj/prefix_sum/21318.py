if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    prefix_sum_list = [0 for _ in range(N)]

    for n in range(0, N):
        if n < N - 1:
            if nums[n] > nums[n + 1]:
                prefix_sum_list[n + 1] += 1
        if n > 0: 
            prefix_sum_list[n] += prefix_sum_list[n - 1]
    
    # print(prefix_sum_list)

    Q = int(input())
    for _ in range(Q):
        x, y = list(map(int, input().split()))
        x -= 1; y -= 1
        print(prefix_sum_list[y] - prefix_sum_list[x])