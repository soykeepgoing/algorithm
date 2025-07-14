import heapq
if __name__ == '__main__':
    N = int(input())
    min_data = []
    max_data = []

    for _ in range(N):
        P, L = list(map(int, input().split()))
        heapq.heappush(min_data, (L, P)) 
        heapq.heappush(max_data, (-L, -P)) 
        
    M = int(input())
    solved_list = [] 
    data = {}

    for _ in range(M):
        order = input()
        # print(data)
        if order[0] == 'r':
            nums = int(order.split()[1])
            if nums == 1:
                while 1: 
                    L, P = list(map(abs, max_data[0]))
                    if P in solved_list:
                        heapq.heappop(max_data)
                    elif abs(P) in data.keys() and abs(data[abs(P)]) != abs(L):
                        heapq.heappop(max_data)
                    else: 
                        print(P)
                        break 
            else:
                while 1:
                    L, P = min_data[0]
                    if P in solved_list:
                        heapq.heappop(min_data)
                    elif P in data.keys() and data[P] != L:
                        heapq.heappop(min_data)
                    else: # 제거되지 않았다면 
                        print(P)
                        break 

        elif order[0] == 'a':
            P, L = list(map(int, order.split()[1:]))
            data[P] = L
            if P in solved_list:
                solved_list.remove(P)

            heapq.heappush(min_data, (L, P))
            heapq.heappush(max_data, (-L, -P))
        else: 
            nums = order.split()[1]
            # 제거된 문제들 리스트에 저장 
            solved_list.append(int(nums))
            data[nums] = -1