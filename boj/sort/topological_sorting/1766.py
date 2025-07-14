import sys 
input = sys.stdin.readline 

def sort(graph, degree, q):
    ans = [] 
    while q: 
        vertex = q.pop()
        ans.append(vertex)
        # print(vertex)
        new_vertex_list = graph[vertex]

        for new_vertex in new_vertex_list:
            degree[new_vertex] -= 1
            if degree[new_vertex] == 0: 
                q.append(new_vertex)
                q.sort(reverse = True)
    return ans


    
if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    degree = [0 for _ in range(N + 1)]
    graph = {}
    for vertex in range(1, N + 1):
        graph[vertex] = []
    for _ in range(M):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        degree[b] += 1

    # print(degree)
    # print(graph)
    

    q = []
    for i in range(1, N + 1):
        if degree[i] == 0:
            q.append(i)
    q.sort(reverse = True)

    # print(q)

    ans = sort(graph, degree, q)
    if N == 1: 
        print(1)
    else: print(*ans)