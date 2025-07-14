import heapq
import sys 
input = sys.stdin.readline 
INF = sys.maxsize
def dijkstra():
    global graph, from_node, end_node

    queue = [] 
    heapq.heappush(queue, [0, from_node]) # cost, node

    parents = [i for i in range(N + 1)]
    results = [INF for _ in range(N + 1)]
    results[from_node] = 0

    while queue:
        cost, node = heapq.heappop(queue)

        if cost > results[node]:
            continue 

        for new_node, new_cost in graph[node]:
            if cost + new_cost < results[new_node]:
                results[new_node] = cost + new_cost
                parents[new_node] = node 
                heapq.heappush(queue, [results[new_node], new_node])

    return results, parents

if __name__ == '__main__':
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, cost = list(map(int, input().split()))
        graph[start].append([end, cost])

    from_node, end_node = list(map(int, input().split()))
    results, parents = dijkstra()

    print(results[end_node])

    path = [] 
    len_count = 0
    temp = end_node 
    while True:
        path.append(temp)
        if temp == parents[temp]:
            break
        temp = parents[temp]
        len_count += 1
    
    print(len_count + 1)
    path.reverse()
    print(*path)