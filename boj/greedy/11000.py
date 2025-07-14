import heapq
import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    time_list = [] 
    for _ in range(N):
        S, T = list(map(int, input().split()))
        time_list.append((S, T))
    time_list.sort(key = lambda x: (x[0], x[1]))

    classes = [] 
    heapq.heappush(classes, time_list[0][1])

    for i in range(1, N):
        start, end = time_list[i]
        if start >= classes[0]:
            heapq.heappop(classes)
        heapq.heappush(classes, end)
    
    print(len(classes))