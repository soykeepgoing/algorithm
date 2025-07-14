import sys
input = sys.stdin.readline 

if __name__ == '__main__':
    n, b, a = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    nums.sort()

    count =  0
    total = 0
    for i in range(n):
        total += nums[i] // 2 # 반값 더하기 
        if i + 1 > a: # 반값 할 수 없다면 반값 더해주기  
            total += nums[count] // 2
            count += 1
        if total > b: 
            break 

    if total > b: 
        print(i)
    else:
        print(n)