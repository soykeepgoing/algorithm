def search(char, x, y, dx, dy, visited, board, count):
    if count == 3: 
        return True
    x_new = x + dx 
    y_new = y + dy
    if x_new in range(0, N) and y_new in range(0, N): 
        if board[x_new][y_new] == char:
            if not visited[x_new][y_new]:
                visited[x_new][y_new] = True 
                if search(char, x_new, y_new, dx, dy, visited, board, count + 1):
                    return True
                visited[x_new][y_new] = False
    return False

if __name__ == '__main__':
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input()))

    direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] != '.':
                visited[x][y] = True 
                char = board[x][y]
                for dindex in range(4):
                    dx, dy = direction[dindex]
                    if search(char, x, y, dx, dy, visited, board, 1): 
                        print(char)
                        exit()
                visited[x][y] = False

    print('ongoing')