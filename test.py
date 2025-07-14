from collections import deque 

def bfs_matrix(graph, start):
    V = len(graph)
    visited = [False] * V
    queue = deque([start])
    visited[start] = True 

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # 방문한 노드 출력
        for neighbor in range(V):
            if graph[node][neighbor] == 1:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                

# 예제: 5개의 정점을 가진 그래프 (0-based index)
graph_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

bfs_matrix(graph_matrix, 0)  # 출력: 0 1 2 3 4