'''
0 <-> 5 
1 <-> 4
2 <-> 3 
'''
def get_new_board_one(board):
    global N,M
    for m in range(M):
        for n in range(N // 2):
            tmp = board[(N - 1) - n][m]
            board[(N - 1) - n][m] = board[n][m]
            board[n][m] = tmp 

def get_new_board_two(board):
    global N,M
    for n in range(N):
        for m in range(M // 2):
            tmp = board[n][(M - 1) - m]
            board[n][(M - 1) - m] = board[n][m]
            board[n][m] = tmp

def get_new_board_three(board):
    global N,M
    new_board = [] 
    for m in range(M):
        new_row = [] 
        for n in range(N):
            new_row.append(board[n][m])
        new_row = new_row[::-1]
        new_board.append(new_row)
    return new_board

def get_new_board_four(board):
    global N,M
    new_board = [] 
    for m in range(M - 1, -1, -1):
        new_row = [] 
        for n in range(N):
            new_row.append(board[n][m])
        new_board.append(new_row)
    return new_board

def get_new_board_five(board):
    global N,M
    new_board = []
    for m in [0, M//2]:
        for n in range(N//2):
            new_row = []
            for value in board[n + N//2][m:(m + M//2)]:
                new_row.append(value)
            for value in board[n + 0][m:(m + M//2)]:
                new_row.append(value)
            new_board.append(new_row)
    return new_board

def get_new_board_six(board):
    global N,M
    new_board = []
    for m in [M//2, 0]:
        for n in range(N//2):
            new_row = []
            for value in board[n + 0][m:(m + M//2)]:
                new_row.append(value)
            for value in board[n + N//2][m:(m + M//2)]:
                new_row.append(value)
            new_board.append(new_row)
    return new_board

if __name__ == '__main__':
    N, M, R = list(map(int, input().split()))
    
    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))

    orders = list(map(int, input().split()))

    for r in range(R):
        order = orders[r]
        if order == 1: 
            get_new_board_one(board)
        elif order == 2: 
            get_new_board_two(board)
        elif order == 3: 
            board = get_new_board_three(board)
        elif order == 4:
            board = get_new_board_four(board)
        elif order == 5: 
            board = get_new_board_five(board)
        elif order == 6:
            board = get_new_board_six(board)
        
        N = len(board)
        M = len(board[0])

    for n in range(N):
        print(*board[n])