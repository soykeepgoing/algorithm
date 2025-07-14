import sys
import heapq

def dijkstra_heap(n, graph, start):
    INF = sys.maxsize

    distance = [INF] * (n + 1)
    distance[start] = 0 
    queue = [] 

    heapq.heappush(queue, (0, start)) # 거리과 노드 번호 삽입 

    while queue: 
        dist, node = heapq.heappop(queue) 

        if distance[node] < dist: # 최단 거리에 해당한다면 
            continue 

        for v, cost in graph[node]: # 갱신 
            new_cost = dist + cost
            if new_cost < distance[v]:
                distance[v] = new_cost
                heapq.heappush(queue, (new_cost, v)) # 추가 탐색할 노드 삽입 
    
    return distance

 
# 동일한 그래프 예제
n = 6
graph = {1: [(2, 2), (3, 5), (4, 1)],
         2: [(3, 3), (4, 2)],
         3: [(2, 3), (6, 5)],
         4: [(3, 3), (5, 1)],
         5: [(3, 1), (6, 2)],
         6: []}

start_node = 1
result = dijkstra_heap(n, graph, start_node)

print("최단 거리 결과:", result[1:])