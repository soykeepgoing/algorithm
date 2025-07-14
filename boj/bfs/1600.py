from collections import deque 
import sys 
input = sys.stdin.readline 

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
knight_direction = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]

def bfs(board, K, W, H):

    queue = deque([])
    counts = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    queue.append([0, 0, K])
    
    while queue:
        x, y, K = queue.popleft()

        if x == (H -1) and y == (W - 1):
            return counts[x][y][K]
        
        if K > 0:
            for k in range(8):
                x_new = x + knight_direction[k][0]
                y_new = y + knight_direction[k][1]

                if x_new in range(0, H) and y_new in range(0, W):
                    if board[x_new][y_new] == 0 and counts[x_new][y_new][K - 1] == 0: 
                        counts[x_new][y_new][K - 1] = counts[x][y][K] + 1
                        queue.append((x_new, y_new, K - 1))
        
        for k in range(4):
            x_new = x + direction[k][0]
            y_new = y + direction[k][1]

            if x_new in range(0, H) and y_new in range(0, W):
                if board[x_new][y_new] == 0 and counts[x_new][y_new][K] == 0: 
                    counts[x_new][y_new][K] = counts[x][y][K] + 1 
                    queue.append((x_new, y_new, K))

    return -1
        

if __name__ == '__main__':
    K = int(input())
    W, H = list(map(int, input().split()))
    
    board = [] 
    for _ in range(H):
        board.append(list(map(int, input().split())))

    ans = bfs(board, K, W, H)
    print(ans)
