import heapq 
import sys 
input = sys.stdin.readline 
INF = sys.maxsize

def dijkstra(graph, start_node, target_node):
    distances = [INF for _ in range(N + 1)]

    queue = [] 
    heapq.heappush(queue, (0, start_node)) # 도착 지점 1, 시간 0 
    distances[start_node] = 0 
    
    while queue: 
        time, start = heapq.heappop(queue)

        for end, end_time in graph[start]:
            if time + end_time < distances[end]:
                distances[end] = time + end_time
                heapq.heappush(queue, (distances[end], end))

    print(distances)

    return distances[target_node] 
    


if __name__ == '__main__':
    N, M, X = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    distances = [0 for _ in range(N + 1)]

    for _ in range(M):
        S,E,T = list(map(int, input().split()))
        graph[S].append([E, T])

    
    for start in range(1, N + 1):
        if start != X: 
            dist = dijkstra(graph, start, X)
            distances[start] += dist
    
    for end in range(1, N + 1):
        if end != X: 
            dist = dijkstra(graph, X, end)
            distances[end] += dist

    print(max(distances))

