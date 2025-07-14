import heapq 
import sys 
INF = sys.maxsize
input = sys.stdin.readline 

def dijkstra(start_node):

    # 최단 거리 
    # 1번부터 N번 정점까지 
    # 임의의 두 정점은 반드시 통과 
    
    distances = [INF for _ in range(N)]
    distances[start_node] = 0 
    queue = [] 
    heapq.heappush(queue, (start_node, 0)) # node, dist

    while queue:
        node, dist = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            if dist + next_dist < distances[next_node]: # 최단 거리라면 
                distances[next_node] = dist + next_dist
                heapq.heappush(queue, (next_node, distances[next_node]))

    return distances

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        a, b = a-1, b-1
        graph[a].append((b, c))
        graph[b].append((a, c))

    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1

    distances = dijkstra(start_node = u)
    node0_u = distances[0]
    nodeu_v = distances[v]
    nodeu_N = distances[N - 1]

    distances = dijkstra(start_node = v)
    node0_v = distances[0]
    nodev_u = distances[u]
    nodev_N = distances[N - 1]

    ans1 = node0_u + nodeu_v + nodev_N 
    ans2 = node0_v + nodev_u + nodeu_N 

    if INF in (node0_u, nodeu_v, nodev_N):
        ans1 = INF 

    if INF in (node0_v, nodev_u, nodeu_N):
        ans2 = INF 

    ans = min(ans1, ans2)

    if ans == INF:
        print(-1)
    else:
        print(ans)