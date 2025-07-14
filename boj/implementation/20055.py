if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    belts = list(map(int, input().split()))

    count_zero = 0 
    step = 0
    robots = [False for _ in range(N)]
    while count_zero < K: 
        # print(step)
        flag = False 

        # 1. 벨트 + 로봇 회전 
        belts = [belts[-1]] + belts[:-1]
        robots = [False] + robots[:-1]

        if robots[-1]:  # 내려질 위치에 있다면 미리 제거 
            robots[-1] = False 
        
        # 2. 로봇 이동 
        for index in range(N - 2, -1, -1):
            # print(index, robots[index], belts[index + 1])
            if robots[index] == True: 
                if not robots[index + 1] and belts[index + 1] >= 1: # 이동할 수 있다면 
                    robots[index] = False
                    if (index + 1) != (N - 1):
                        robots[index + 1] = True
                    belts[index + 1] -= 1
    
        # print(belts)

        if robots[-1]: 
            robots[-1] = False 

        # 3. 로봇 올리기 
        if not robots[0]:
            if belts[0] >= 1: 
                robots[0] = True 
                belts[0] -= 1
        
        # print(robots)
        
        step += 1
        count_zero = belts.count(0)
        # print(belts)

    print(step)