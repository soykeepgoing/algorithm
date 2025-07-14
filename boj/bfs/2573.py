from collections import deque 
import sys 
input = sys.stdin.readline 

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def freeze(board, N, M):
    new_board = []

    for i in range(N):
        new_row = []
        for j in range(M):
            if board[i][j] > 0:
                new_value = board[i][j]
                for di, dj in directions:
                    ni = i + di 
                    nj = j + dj
                    if ni in range(N) and nj in range(M):
                        if board[ni][nj] == 0:
                            if new_value == 0:
                                break 
                            new_value -= 1
                new_row.append(new_value)
            else:
                new_row.append(0)
        new_board.append(new_row)
    
    return new_board

def bfs(board, visited, i, j, N, M):
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni = i + di 
            nj = j + dj 
            if ni in range(N) and nj in range(M):
                if board[ni][nj] > 0 and not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = True 

def count_ice(board, N, M):
    visited = [[False] * M for _ in range(N)]
    count = 0 
    has_ice = False 

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                if not visited[i][j]: 
                    bfs(board, visited, i, j, N, M)
                    count += 1
                    has_ice = True

    return count, has_ice

def main():
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]

    if count_ice(board, N, M)[0] >= 2: 
        print(0)
        return 
    
    year = 0 
    while True: 
        year += 1
        board = freeze(board, N, M)
        counts, has_ice = count_ice(board, N, M)

        if counts >= 2: 
            print(year)
            return 
        if not has_ice:
            print(0)
            return 

if __name__ == '__main__':
    main()