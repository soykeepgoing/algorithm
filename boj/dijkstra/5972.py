import heapq
INF = 10e9

def dijkstra(N):
    distance = [INF for _ in range(N + 1)]

    queue = [] 
    heapq.heappush(queue, (0, 1)) # 거리, 노드 

    distance[1] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        for new_dist, new_node in graph[node]:
            if dist + new_dist < distance[new_node]:
                distance[new_node] = dist + new_dist
                heapq.heappush(queue, (distance[new_node], new_node))
    
    return distance

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        v1, v2, d = list(map(int, input().split()))
        graph[v1].append((d, v2))
        graph[v2].append((d, v1))
    
    distance = dijkstra(N)
    print(distance[N])  