from collections import deque 
import sys 
input = sys.stdin.readline 

def search(board, visited, q): 
    global M, N
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while q: 
        x, y = q.popleft()
        for dx, dy in direction: 
            x_new = x + dx; y_new = y + dy 
            if x_new in range(M) and y_new in range(N):
                if not visited[x_new][y_new]:
                    if board[x_new][y_new] == 1: 
                        q.append([x_new, y_new])
                        visited[x_new][y_new] = True 

if __name__ == '__main__': 
    T = int(input())
    for _ in range(T):
        M, N, K = list(map(int, input().split()))
        board = [[0 for _ in range(N)] for _ in range(M)]
        for _ in range(K):
            X, Y = list(map(int, input().split()))
            board[X][Y] = 1

        visited = [[False for _ in range(N)] for _ in range(M)]

        q = deque([])
        total_cnt = 0
        for x in range(M):
            for y in range(N): 
                if not visited[x][y]: 
                    if board[x][y] == 1:
                        visited[x][y] = True 
                        q.append([x, y])
                        search(board, visited, q)
                        total_cnt += 1 
        print(total_cnt)