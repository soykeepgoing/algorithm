if __name__ == '__main__': 
    time_arr = [True for _ in range(12 * 60)] # 12시간 * 60분 
    N = int(input())
    for _ in range(N): 
        start, end = input().split()
        start = int(start[:2]) * 60 + int(start[2:]) - 600
        end = int(end[:2]) * 60  + int(end[2:]) - 600
        for t in range(start - 10, end + 10, 1): 
            if t in range(0, 12 * 60):
                if time_arr[t]: 
                    time_arr[t] = False

    ans = 0
    ans_list = [] 
    flag = True
    for i in range(720): 
        t = time_arr[i]
        if t: 
            ans += 1
            flag = True 
        else: 
            if flag:
                ans_list.append(ans)
                ans = 0 
                flag = False
    
    if flag and ans > 0:
        ans_list.append(ans)

    if ans_list:
        print(max(ans_list))        
    else: 
        print(0)
