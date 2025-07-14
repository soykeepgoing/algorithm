from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    if N > 1022: 
        print(-1)
        exit()

    nums = [] 
    for r in range(1, 11):
        for comb in combinations(range(10), r):
            nums.append(int("".join(map(str, reversed(comb)))))
    
    nums.sort()
    print(nums[N])