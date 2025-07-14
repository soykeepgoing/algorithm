import sys 
input = sys.stdin.readline 

def dfs(node):
    global graph, visited, parents
    for next_node in graph[node]:
        if parents[node] == next_node: 
            continue 

        if visited[next_node]:
            return True 
        
        parents[next_node] = node 
        visited[next_node] = True 

        if dfs(next_node):
            return True 
        
    return False

if __name__ == '__main__':
    case = 0
    while True:
        N, M = list(map(int, input().split()))
        
        if N == 0 and M == 0:
            break

        case += 1

        graph = [[] for _ in range(N + 1)]
        for _ in range(M):
            a, b = list(map(int, input().split()))
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False for _ in range(N + 1)]
        parents = [node for node in range(N + 1)]
        ans = 0
        for node in range(1, N + 1):
            if not visited[node]:
                visited[node] = True 
                if not dfs(node):
                    ans += 1

        if ans == 0:
            print(f'Case {case}: No trees.')
        elif ans == 1:
            print(f'Case {case}: There is one tree.')
        else:
            print(f'Case {case}: A forest of {ans} trees.')