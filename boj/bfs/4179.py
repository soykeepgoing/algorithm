from collections import deque 
import sys 
# input = sys.stdin.readline 
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = sys.maxsize
INF = 10


def bfs_fire(fire_map, visited, R, C, queue):
    queue = deque(queue)

    while queue:
        r, c, time = queue.popleft()

        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            if new_r in range(R) and new_c in range(C):
                if not visited[new_r][new_c] and fire_map[new_r][new_c] == 0: 
                    visited[new_r][new_c] = True 
                    fire_map[new_r][new_c] = time + 1
                    queue.append([new_r, new_c, time + 1])

def bfs_j(J_map, fire_map, visited, R, C, queue):
    queue = deque([queue])

    while queue:
        r, c, time = queue.popleft()
        
        if r in [0, R -1] or c in [0, C - 1]:
            if J_map[r][c] < fire_map[r][c]:
                return time 

        for dr, dc in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            if new_r in range(R) and new_c in range(C):
                if not visited[new_r][new_c] and J_map[new_r][new_c] == 0: 
                    visited[new_r][new_c] = True 
                    J_map[new_r][new_c] = time + 1
                    queue.append([new_r, new_c, time + 1])
    
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    R, C = list(map(int, input().split()))
    fire_map = []
    J_map = [] 
    F_INIT_LIST = [] 

    for r in range(R):
        info = list(input())
        fire_info = [] 
        J_info = [] 
        for c in range(C):
            if info[c] == '#':
                fire_info.append(INF)
                J_info.append(INF)
            elif info[c] == 'F':
                F_INIT_LIST.append([r, c])
                fire_info.append(1)
                J_info.append(INF)
            elif info[c] == 'J':
                j_init = [r, c]
                fire_info.append(0)
                J_info.append(1)
            elif info[c] == '.':
                fire_info.append(0)
                J_info.append(0)            

        fire_map.append(fire_info)
        J_map.append(J_info)


    # fire map bfs 탐색 

    # print(F_INIT_LIST)

    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = []
    for r, c in F_INIT_LIST:
        queue.append([r, c, 1])
        visited[r][c] = True 
    bfs_fire(fire_map, visited, R, C, queue)

    for r in range(R):
        for c in range(C):
            if fire_map[r][c] == 0:
                fire_map[r][c] = INF

    # print(fire_map)

    # J map bfs 탐색 
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = [j_init[0], j_init[1], 1] 
    visited[j_init[0]][j_init[1]] = True
    ans = bfs_j(J_map, fire_map,  visited, R, C, queue)
    # print(J_map)
    # print(fire_map)
    
    print(ans)