import sys 
input = sys.stdin.readline
if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    red_team = [] 
    for i in range(N - 1):
        if i == 0:
            max_num = nums[i]
        else:
            max_num = max(max_num, nums[i])
        red_team.append(max_num)

    blue_team = []
    for i in range(N - 1, 0, -1):
        if i == N - 1:
            max_num = nums[i]
        else:
            max_num = max(max_num, nums[i])
        blue_team.append(max_num)
    blue_team = blue_team[::-1]
    # print(red_team)
    # print(blue_team)
    red_count = 0 
    blue_count = 0

    for i in range(N - 1):
        if red_team[i] > blue_team[i]:
            red_count += 1
        elif blue_team[i] > red_team[i]:
            blue_count += 1
        else:
            red_count += 1
            blue_count+=1
    
    # print(red_count, blue_count)
    if red_count > blue_count:
        print('R')
    elif blue_count > red_count:
        print('B')
    else:
        print('X')