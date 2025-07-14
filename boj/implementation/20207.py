if __name__ == '__main__':
    N = int(input())
    days = [0 for _ in range(365 + 1)]

    for _ in range(N):
        S, E = list(map(int, input().split()))
        for day in range(S, E + 1):
            days[day] += 1

    flag = False
    max_height = -1
    width = 0
    area = 0 
    for day in range(1, 366): 
        if days[day] > 0: # 일정이 있는 날 발견 & flag off 
            if not flag: 
                flag = True 
            width += 1
            max_height = max(days[day], max_height)
        elif days[day] == 0 and flag: 
            area += (max_height * width)
            max_height = -1
            width = 0 
            flag = False 

    if flag: 
        area += (max_height * width)

    print(area)