import sys 
input = sys.stdin.readline

def custom_round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)
    
if __name__ == '__main__':
    N = int(input())
    if N == 0:
        print(0)
        exit()

    nums = []
    for _ in range(N):
        nums.append(int(input()))
    nums.sort()
    
    pick = custom_round(N * 0.15)
    first = pick; end = N
    if pick > 0:
        end = N - pick + 1
    ans = 0
    for i in range(0, N - 2 * pick, 1):
        ans += nums[i + pick]
    ans = custom_round(ans / (N - 2 * pick))
    print(ans)