from collections import deque 
DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def check_board(board, melted, R, C):
    queue = deque([(0, 0)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[0][0] = True 
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIRECTION:
            nr = r + dr
            nc = c + dc 
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == 0:
                    queue.append((nr, nc))
                elif board[nr][nc] == 1:
                    melted.append((nr, nc))
    

def melt_cheese(board, melted):
    for r, c  in melted:
        board[r][c] = 0 # 치즈 녹이기 

def count_cheese(board, R, C):
    total_cheese = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                total_cheese += 1
    return total_cheese

def solution(board, R, C):
    total_cheese = count_cheese(board, R, C)
    time = 0 
    while 1: 
        melted = []
        check_board(board, melted, R, C)
        if total_cheese - len(melted) == 0:
            return time + 1, total_cheese 
        melt_cheese(board, melted)
        total_cheese -= len(melted)
        time += 1
        
if __name__ == '__main__':
    R, C = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(R)]

    time, left_count = solution(board, R, C)
    print(time)
    print(left_count)