from collections import deque 
import sys 

input = sys.stdin.readline 
DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(queue):
    global board

    while queue:
        value, x, y, t = queue.popleft()

        for dx, dy in DIRECTIONS: # 사방 탐색 
            x_new = x + dx
            y_new = y + dy
            if x_new in range(N) and y_new in range(N):
                if board[x_new][y_new] == 0: # 바이러스가 퍼지지 않은 경우 
                    if t + 1 <= T: # T 시간까지 전파되는 경우에만 큐에 저장 
                        board[x_new][y_new] = value # 바이러스 전파 
                        queue.append([value, x_new, y_new, t + 1])



if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    position = [] 
    board = [] 
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(N):
            if board[i][j] > 0: # 바이러스가 존재하는 포지션의 경우 
                position.append([board[i][j], i, j, 0]) # 바이러스 번호, 좌표, 시간 정보 저장 

    T, X, Y = list(map(int, input().split()))

    position.sort(key = lambda x: [x[0], x[1], x[2]]) # 바이러스 번호, 좌표를 기준으로 오름차순 정렬
    queue = deque(position) # 큐 형태 저장 
    bfs(queue) # bfs 탐색 
    print(board[X - 1][Y - 1])
        
