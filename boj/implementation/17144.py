from collections import deque 

DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_dust_pos(board):
    dust_queue = deque([])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0: # 미세먼지가 있다면 
                dust_queue.append((i, j, board[i][j]))
    return dust_queue

def spread_dust(board, R, C):
    dust_queue = get_dust_pos(board)
    while dust_queue: 
        i, j, dust = dust_queue.popleft()
        count = 0
        for di, dj in DIRECTION:
            ni = i + di 
            nj = j + dj 
            if 0 <= ni < R and 0 <= nj < C:
                if board[ni][nj] > -1: # 공기 청정기 자리가 아니라면 
                    count += 1
                    board[ni][nj] += (dust // 5)
        board[i][j] -= (dust // 5) * count

def get_machine_pos(board):
    for i in range(len(board)):
        if board[i][0] == -1:
            return i, i + 1

def get_upper_pos(mx1, R, C):
    # upper 
    pos1 = []
    for i in range(1,C):
        pos1.append((mx1, i))
    for i in range(mx1-1, -1, -1):
        pos1.append((i, C - 1))
    for i in range(C - 2, -1, -1):
        pos1.append((0, i))
    for i in range(1, mx1):
        pos1.append((i, 0))
    return pos1

def get_lower_pos(mx2, R, C):
    pos2 = [] 
    for i in range(1,C):
        pos2.append((mx2, i))
    for i in range(mx2 + 1, R):
        pos2.append((i, C - 1))
    for i in range(C - 2, -1, -1):
        pos2.append((R - 1, i))
    for i in range(R - 2, mx2, -1):
        pos2.append((i, 0))
    return pos2

def get_wind_pos(mx1, mx2, R, C):
    return get_upper_pos(mx1, R, C), get_lower_pos(mx2, R, C)

def work_machine(board, upper_pos, lower_pos):
    # upper machine 0 ~ mx1
    for i in range(len(upper_pos)):
        x, y = upper_pos[i]
        if i == 0:
            value = board[x][y]
            board[x][y] = 0
        else:            
            tmp = board[x][y]
            board[x][y] = value 
            value = tmp 
        
    # lower machine mx2 ~ R
    for i in range(len(lower_pos)):
        x, y = lower_pos[i]
        if i == 0:
            value = board[x][y]
            board[x][y] = 0
        else:            
            tmp = board[x][y]
            board[x][y] = value 
            value = tmp 

def solution(board, R, C, T):
    mx1, mx2 = get_machine_pos(board)
    upper_pos, lower_pos = get_wind_pos(mx1, mx2, R, C)
    # print(upper_pos)
    # print(lower_pos)

    for _ in range(T):
        spread_dust(board, R, C) # 미세먼지 확산 
       #  print(board)
        work_machine(board, upper_pos, lower_pos) # 공기청정기 확산 
        board[mx1][0] = -1
        board[mx1][1] = 0

    answer = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                answer += board[i][j]

    return answer

if __name__ == '__main__':
    R, C, T = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(R)]
    print(solution(board, R, C, T))