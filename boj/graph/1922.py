'''
2 - 3 - 1 
    |
    4 - 5
    |
    6

2 + 4 + 6 + 3 + 8 = 23

- 컴퓨터를 연결하는 비용을 최소로 하여 
- 모든 컴퓨터를 연결 
- a - b - c는 a - c가 연결된다는 뜻 

=> 사이클이 존재하지 않는 최소 가중치를 갖는 그래프 만들기 

1. 가중치 오름차순으로 정렬: 최소 가중치 
2. 사이클이 존재하지 않는 경우에만 간선 연결 
- 사이클 존재 확인은 유니온 파인드

2 3 2
4 5 3
1 3 4
1 2 5
3 4 6
2 4 7
4 6 8
5 6 8 
3 5 11

1 2 3 4 5 6
1 1 2 1 4 1

'''
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(nodeA, nodeB):
    parent_nodeA = find(nodeA)
    parent_nodeB = find(nodeB)
    if parent_nodeA < parent_nodeB:
        parent[parent_nodeB] = parent_nodeA
    else:
        parent[parent_nodeA] = parent_nodeB
 
def solution():
    answer = 0 
    for nodeA, nodeB, weight in graph:
        parent_nodeA = find(nodeA)
        parent_nodeB = find(nodeB)
        if parent_nodeA != parent_nodeB:
            union(nodeA, nodeB)
            answer += weight 
    return answer

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    graph = [] 
    for __ in range(m):
        graph.append(list(map(int, input().split())))
    graph.sort(key = lambda x: x[2])
    # print(graph)
    parent = list(range(n + 1))
    answer = solution()
    print(answer)
