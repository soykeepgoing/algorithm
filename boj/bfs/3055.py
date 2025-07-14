from collections import deque 
import sys 
input = sys.stdin.readline 

INF = sys.maxsize
DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    answer = INF 

    # 물 확산 
    while water_pos:
        i, j, time = water_pos.popleft() 

        for di, dj in DIRECTION:
            new_i = i + di 
            new_j = j + dj
            
            if new_i in range(r) and new_j in range(c):
                    if board[new_i][new_j] == 0:
                        board[new_i][new_j] = time + 1

                        water_pos.append((new_i, new_j, board[new_i][new_j]))

    visited = [[False for _ in range(c)] for _ in range(r)]
    while now_pos:
        x, y, time = now_pos.popleft()
        new_time = time + 1

        visited[x][y] = True 

        for dx, dy in DIRECTION:
            new_x = x + dx 
            new_y = y + dy 

            if new_x in range(r) and new_y in range(c):
                if not visited[new_x][new_y]:

                    if board[new_x][new_y] == -1:
                        answer = min(answer, new_time)
                        continue 
    
                    if new_time < board[new_x][new_y] or board[new_x][new_y] == 0:
                        visited[new_x][new_y] = True 
                        now_pos.append((new_x, new_y, new_time))
    
    return answer

if __name__ == '__main__':
    r, c = list(map(int, input().split()))
    water_pos = deque([])
    now_pos = deque([]) 
    board = [] 
    for i in range(r):
        tmp = list(input())
        for j in range(c):
            if tmp[j] == '*': # 물이라면
                tmp[j] = 0 
                water_pos.append((i, j, 0)) # i, j, time 
            elif tmp[j] == 'S':
                x = i
                y = j 
                tmp[j] = 0 
            elif tmp[j] == 'D':
                tmp[j] = -1 
            elif tmp[j] == 'X':
                tmp[j] = -2 
            elif tmp[j] == '.':
                tmp[j] = 0 
                
        board.append(tmp)

    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[x][y] = True 

    now_pos.append((x, y, 0)) # i, j, time 
    answer = bfs()
    if answer == INF:
        answer = 'KAKTUS'
    print(answer)