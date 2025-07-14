import sys 
INF = sys.maxsize
input = sys.stdin.readline 

def search():
    global flag
    for i in range(1, N + 1): # N개의 라운드 
        for s_node in range(1, N + 1): # 전체 탐색 
            for e_node, time in graph[s_node]: 
                if result[s_node] != INF and result[e_node] > result[s_node] + time:
                    result[e_node] = result[s_node] + time 
                    
                    if i == N:
                        return False
    
    return True 


if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        graph[a].append((b, c))
    
    if N == 1: 
        print(0)
        exit() 

    flag = False
    result = [INF] * (N + 1)
    result[1] = 0

    if search():
        for node in range(2, N + 1):
            print(result[node] if result[node] != INF else -1)
    else:
        print(-1)