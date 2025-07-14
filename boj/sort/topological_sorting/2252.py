import sys 
input = sys.stdin.readline 

def dfs(node, graph, visited, stack, N):
    visited[node] = True 
    for neighbor in graph[node]: 
        if not visited[neighbor]: # neighbor를 방문하지 않은 경우 
            dfs(neighbor, graph, visited, stack, N)
    stack.append(node)
    return stack

def sort(graph, N):
    visited = [False for _ in range(N + 1)]
    stack =  []

    for node in range(1, N + 1):
        if not visited[node] and len(graph[node]) > 0:
            stack = dfs(node, graph, visited, stack, N)
    
    stack = stack[::-1]

    # 관계가 없는 노드에 대해서 스택에 추가 
    for node in range(1, N + 1): 
        if node not in stack:
            stack.append(node)

    print(*stack)

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    
    graph = {}
    for i in range(N + 1):
        graph[i] = []

    for _ in range(M):
        A, B = list(map(int, input().split()))
        graph[A].append(B)

    sort(graph, N)