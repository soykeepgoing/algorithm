import heapq 
import sys 
INF = sys.maxsize
input = sys.stdin.readline 

def dijkstra(graph, states):
    queue = [] 
    heapq.heappush(queue, (0, 0))

    time_list = [INF for _ in range(N)]
    time_list[0] = 0 

    while queue:
        node, time = heapq.heappop(queue)
        # print(node, time)

        if time > time_list[node]: # 이미 더 작은 경우 갱신 하지 않음. 
            continue

        for new_node, new_time in graph[node]:
            # print(new_node, time, new_time, time_list[new_node])
            if time + new_time < time_list[new_node]:
                if (new_node < N - 1 and states[new_node] == 0) or (new_node == N - 1):
                    time_list[new_node] = time + new_time
                    heapq.heappush(queue, (new_node, time_list[new_node]))  

    return time_list


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    states = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, t = list(map(int, input().split()))
        graph[a].append((b, t))
        graph[b].append((a, t))
    
    time_list = dijkstra(graph, states)

    if time_list[N - 1] == INF:
        print(-1)
    else:
        print(time_list[N - 1])