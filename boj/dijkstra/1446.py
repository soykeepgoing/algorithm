import sys 

if __name__ == '__main__':
    INF = sys.maxsize
    N, D = list(map(int, input().split()))
   
    distance = [INF] * (D + 1)
    distance[0] = 0 

    shortcuts = []

    for _ in range(N):
        start, end, cost = list(map(int, input().split()))
        if start in range(D + 1) and end in range(D + 1):
            shortcuts.append([start, end, cost])

    
    for i in range(D + 1):
        if i >= 0:
            distance[i] = min(distance[i], distance[i - 1] + 1)

        for start, end, cost in shortcuts:
            if distance[start] + cost < distance[end]:
                distance[end] = distance[start] + cost
    
    print(distance[D])