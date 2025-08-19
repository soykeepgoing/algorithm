def get_board_up(now_board):
    next_board = [[0] * n for __ in range(n)]

    for col in range(n):
        state = 0
        new_col = []
        for row in range(n):
            if now_board[row][col] == 0:
                continue 
            if state == 0:
                state = now_board[row][col]
            elif state > 0 and now_board[row][col] != state:
                new_col.append(state)
                state = now_board[row][col]
            elif state > 0 and now_board[row][col] == state:
                new_col.append(state * 2)
                state = 0
        
        if state > 0:
            new_col.append(state)

        for r in range(n):
            if r < len(new_col):
                next_board[r][col] = new_col[r]
            else:
                next_board[r][col] = 0

    return next_board

def get_board_down(now_board):
    next_board = [[0] * n for __ in range(n)]
    for col in range(n):
        state = 0
        new_col = []
        for row in range(n - 1, -1, -1):
            if now_board[row][col] > 0:
                if state == 0:
                    state = now_board[row][col]
                elif state > 0 and now_board[row][col] != state:
                    new_col.append(state)
                    state = now_board[row][col]
                elif state > 0 and now_board[row][col] == state:
                    new_col.append(state * 2)
                    state = 0
        
        if state > 0:
            new_col.append(state)

        for r in range(n - 1, -1, -1):
            if (n - 1) - r < len(new_col):
                next_board[r][col] = new_col[(n - 1) - r]
            else:
                next_board[r][col] = 0

    return next_board

def get_board_right(now_board):
    next_board = [[0] * n for __ in range(n)]
    for row in range(n):
        state = 0
        new_row = []
        for col in range(n - 1, -1, -1):
            if now_board[row][col] > 0:
                if state == 0:
                    state = now_board[row][col]
                elif state > 0 and now_board[row][col] != state:
                    new_row.append(state)
                    state = now_board[row][col]
                elif state > 0 and now_board[row][col] == state:
                    new_row.append(state * 2)
                    state = 0
        
        if state > 0:
            new_row.append(state)

        for c in range(n - 1, -1, -1):
            if (n - 1) - c < len(new_row):
                next_board[row][c] = new_row[(n - 1) - c]
            else:
                next_board[row][c] = 0

    return next_board

def get_board_left(now_board):
    next_board = [[0] * n for __ in range(n)]
    for row in range(n):
        state = 0
        new_row = []
        for col in range(n):
            if now_board[row][col] > 0:
                if state == 0:
                    state = now_board[row][col]
                elif state > 0 and now_board[row][col] != state:
                    new_row.append(state)
                    state = now_board[row][col]
                elif state > 0 and now_board[row][col] == state:
                    new_row.append(state * 2)
                    state = 0
        
        if state > 0:
            new_row.append(state)

        for c in range(n):
            if c < len(new_row):
                next_board[row][c] = new_row[c]
            else:
                next_board[row][c] = 0

    return next_board

def max_board_number(now_board):
    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(now_board[i][j], answer)
    return answer

def solution(depth, now_board):
    if depth == 5:
        return max_board_number(now_board)
    
    max_answer = 0

    up_board = get_board_up(now_board)
    answer = solution(depth + 1, up_board)
    max_answer = max(answer, max_answer)

    down_board = get_board_down(now_board)
    answer = solution(depth + 1, down_board)
    max_answer = max(answer, max_answer)

    right_board = get_board_right(now_board)
    answer = solution(depth + 1, right_board)
    max_answer = max(answer, max_answer)

    left_board = get_board_left(now_board)
    answer = solution(depth + 1, left_board)
    max_answer = max(answer, max_answer)

    return max_answer

if __name__ == '__main__':
    n = int(input())
    board = []
    for __ in range(n):
        board.append(list(map(int, input().split())))
    
    answer = solution(0, board)
    print(answer)
