'''

i, j 돌면서 순회 
만약 0이라면 가능한 num 넣기 
그다음에 또 순회하다가
가능한 num이 없다면 가지치기 => 다음 num 넣기 
'''

def check_row(num, row):
    for i in range(9):
        if board[row][i] == num:
            return False
    return True 

def check_col(num, col):
    for i in range(9):
        if board[i][col] == num:
            return False
    return True 

def check_part(num, row, col):
    start_i, start_j = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_i, start_i + 3):
        for j in range(start_j, start_j + 3):
            if board[i][j] == num:
                return False 
    return True 

def get_next_pos(i, j):
    next_j = j + 1
    next_i = i
    if next_j == 9:
        next_j = 0 
        next_i += 1
    return next_i, next_j

def get_next_num(num, i, j):
    if check_row(num, i) and check_col(num, j) and check_part(num, i, j):
        return num 
    return False 

def solution(index):
    if index == len(blanks):
        for i in range(9):
            print(''.join(list(map(str, board[i]))))
        exit(0)
    
    i, j = blanks[index]

    for num in range(1, 10):
        if check_row(num, i) and check_col(num, j) and check_part(num, i, j):
            board[i][j] = num 
            solution(index + 1)
            board[i][j] = 0


if __name__ == '__main__':
    board = [] 
    blanks = []
    for i in range(9):
        board.append(list(map(int, list(input()))))
        for j in range(9):
            if board[-1][j] == 0:
                blanks.append((i, j))

    solution(0) 
