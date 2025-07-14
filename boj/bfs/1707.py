from collections import deque 
import sys 
input = sys.stdin.readline 

def bfs(graph):
    V = len(graph)
    levels = [0] * (V)

    for start in range(1, V):
        if levels[start] == 0:
            queue = deque([start])
            levels[start] = 1 

            while queue:
                node = queue.popleft()
                # print(node)
                flag = levels[node]

                for neighbor in graph[node]:
                    new_level = (-1) * flag 
                    if levels[neighbor] == 0:
                        levels[neighbor] = new_level
                        queue.append(neighbor)
                    else:
                        if levels[neighbor] != new_level:
                            return 'NO'
        
    return 'YES'

if __name__ == '__main__':
    K = int(input())

    for _ in range(K):
        V, E = list(map(int, input().split()))
        graph = [[] for _ in range(V + 1)]
        for _ in range(E):
            u, v = list(map(int, input().split()))
            graph[u].append(v)
            graph[v].append(u)

        ans = bfs(graph)
        print(ans)