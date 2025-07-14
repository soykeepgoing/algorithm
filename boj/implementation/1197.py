import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parent(parents, a,b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a 
    else:
        parents[a] = b

if __name__ == '__main__':
    V, E = list(map(int, input().split()))
    graph = []
    for _ in range(E):
        a, b, c = list(map(int, input().split()))
        graph.append([a - 1, b - 1, c])

    graph.sort(key = lambda x: (x[2])) 

    answer = 0
    parents = [i for i in range(V)]

    # 가중치가 적은 노드부터 
    for a, b, weight in graph: 
        if find_parents(parents,a) != find_parents(parents, b): # 사이클 발생하지 않음
            union_parent(parents, a,b)
            answer += weight

    print(answer) 
    # print(parents)

