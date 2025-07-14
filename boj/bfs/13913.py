import sys 
from collections import deque 
INF = sys.maxsize

def solution():
    pos_list = [] 
    now_node = K 
    while now_node != INF: # 현재 노드가 INF가 아니라면, 즉 부모가 존재한다면
        pos_list.append(now_node)
        now_node = parents[now_node]
    return pos_list

def bfs():
    queue = deque([(N, 0)]) # 현재 노드, 시간 
    visited[N] = 0
    while queue:
        pos, time = queue.popleft()
        
        for new_pos in [pos - 1, pos + 1, 2 * pos]: # 현재 노드에서 탐색 가능한 노드 
            if new_pos in range(0, 100001): # 주어진 조건 내에 있고 
                if visited[new_pos] > time + 1: # 최소 시간에 해당한다면 
                    # 업데이트 후 큐 삽입 
                    visited[new_pos] = time + 1
                    parents[new_pos] = pos 
                    queue.append((new_pos, time + 1))
    return solution()

if __name__ == '__main__':
    N, K = list(map(int, input().split()))

    if N == K: # 같은 경우 탐색하지 않음.
        print(0)
        print(N)
    else: # 탐색 
        visited = [INF] * 100001 # 각 노드 별 최소 시간 배열 
        parents = [INF] * 100001 # 각 노드 별 부모노드 저장 배열 
        pos_list = bfs() # 탐색 
        print(visited[K]) 
        print(*pos_list[::-1])