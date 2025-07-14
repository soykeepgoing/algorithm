from collections import deque
import sys 
input = sys.stdin.readline 

DIRECTION = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(queue):
    distance = 0
    
    while queue:
        x, y, d = queue.popleft()
        # print(x, y, d)
        flag = False
        for i in range(4):
            x_new = x + DIRECTION[i][0]
            y_new = y + DIRECTION[i][1]

            if x_new in range(N) and y_new in range(M):
                if not visited[x_new][y_new] and board[x_new][y_new] == 'L':
                    queue.append([x_new, y_new, d + 1])
                    visited[x_new][y_new] = True 
                    flag = True 
        
        if not flag: 
            distance = max(distance, d)

    return distance

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    board = []
    for _ in range(N):
        board.append(list(input()))
    
    # print(board)
    answer = 0 
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'L': # 탐색 시작 
                queue = deque([[i, j, 0]])
                visited = [[False for _ in range(M)] for _ in range(N)]
                visited[i][j] = True
                tmp = bfs(queue)
                answer = max(answer, tmp)

    print(answer)