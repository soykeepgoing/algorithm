import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().split())
    nums = input().rstrip()

    new_nums = [nums[0]]
    count = 0 
    for i in range(1, N):
        num = nums[i]
        while new_nums and count < K and new_nums[-1] < num: 
            new_nums.pop()
            count += 1
        new_nums.append(num)
        
    if count < K: 
        new_nums = new_nums[:-(K - count)]
    
    print(''.join(new_nums))