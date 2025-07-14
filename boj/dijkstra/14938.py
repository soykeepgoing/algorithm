import heapq 
import sys 
input = sys.stdin.readline 
INF = sys.maxsize

def dijkstra(node):
    queue = [] 
    visited = [False for _ in range(n)]
    # distance = [INF for _ in range(n)]
    heapq.heappush(queue, (node, 0))
    visited[node] = True 
    # distance[node] = 0 

    while queue: 
        node, dist = heapq.heappop(queue)

        for next_node, next_dist in graph[node]:
            if dist + next_dist <= m: # 수색 범위보다 작거나 같다면
                if not visited[next_node]:
                    visited[next_node] = True 
                    heapq.heappush(queue, (next_node, dist + next_dist)) 

    tmp = 0 
    for i in range(n):
        if visited[i]: 
            tmp += items[i]
    
    return tmp 

if __name__ == '__main__':
    n, m, r = list(map(int, input().split()))
    items = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(r):
        a, b, i = list(map(int, input().split()))
        a, b = a - 1, b - 1
        graph[a].append((b, i))
        graph[b].append((a, i))
    
    answer = -1
    for i in range(n): # 어디 떨어질지 
        tmp = dijkstra(i)
        answer = max(answer, tmp)

    print(answer)