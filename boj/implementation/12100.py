'''
같은 값을 갖는 블록은 하나로 합쳐진다 

보드를 최대 5번 이동 
각 방향에서 합쳐지는 경우가 있으면 이동 아니면 이동 안함 
이동안하면 최대 값 반환 

방향 
상 - 위 아래로 같은 값을 갖는지 
하 - 위 아래로 같은 값을 갖는지 
좌 - 좌우로 같은 값을 갖는지 
우

위 / 오른쪽 이거 두개의 경우를 생각하면 되는가?
'''

def get_max_of_board(b):
    max_number = 0 
    for i in range(N):
        for j in range(N):
            max_number = max(b[i][j], max_number)
    return max_number

def get_new_board_up(b): 
    board = [[0] * N for __ in range(N)]
    for col in range(N):
        new_col = [] 
        num = 0 
        for row in range(N):
            if b[row][col] == 0:
                continue 
            if num == 0:
                num = b[row][col]
            elif b[row][col] != num:
                new_col.append(num)
                num = b[row][col]
            elif b[row][col] == num:
                new_col.append(num * 2)
                num = 0 
        if num > 0:
            new_col.append(num)
        for row in range(N):
            if row < len(new_col):
                board[row][col] = new_col[row]
            else:
                board[row][col] = 0
    return board

def get_new_board_down(b): 
    board = [[0] * N for __ in range(N)]
    for col in range(N):
        new_col = [] 
        num = 0 
        for row in range(N - 1, -1, -1):
            if b[row][col] == 0:
                continue 
            if num == 0:
                num = b[row][col]
            elif b[row][col] != num:
                new_col.append(num)
                num = b[row][col]
            elif b[row][col] == num:
                new_col.append(num * 2)
                num = 0 
        if num > 0:
            new_col.append(num)
        
        for row in range(N -1 , -1, -1):
            if (N - 1) - row < len(new_col):
                board[row][col] = new_col[(N - 1) - row]
            else:
                board[row][col] = 0
    return board

def get_new_board_right(b):
    board = [] 
    for row in range(N):
        new_row = [] 
        num = 0 
        for col in range(N-1, -1, -1):
            if b[row][col] == 0:
                continue 
            if num == 0:
                num = b[row][col]
            elif b[row][col] != num:
                new_row.append(num)
                num = b[row][col]
            elif b[row][col] == num:
                new_row.append(num * 2)
                num = 0 
        if num > 0:
            new_row.append(num)
        
        board.append([])
        
        for col in range(N - 1, -1 , -1):
            if col < len(new_row):
                board[-1].append(new_row[col])
            else:
                board[-1].append(0)

    return board

def get_new_board_left(b):
    board = [] 
    for row in range(N):
        new_row = [] 
        num = 0 
        for col in range(N):
            if b[row][col] == 0:
                continue 
            if num == 0:
                num = b[row][col]
            elif b[row][col] != num:
                new_row.append(num)
                num = b[row][col]
            elif b[row][col] == num:
                new_row.append(num * 2)
                num = 0 
        if num > 0:
            new_row.append(num)
        
        board.append([])
        
        for col in range(N):
            if col < len(new_row):
                board[-1].append(new_row[col])
            else:
                board[-1].append(0)

    return board

def solution(depth, board):
    if depth == 5:
        return get_max_of_board(board) 
    
    max_answer = get_max_of_board(board)
    for dir in range(4):
        if dir == 0:
            new_board = get_new_board_up(board)
        elif dir == 1:
            new_board = get_new_board_down(board)
        elif dir == 2:
            new_board = get_new_board_right(board)
        elif dir == 3:
            new_board = get_new_board_left(board)
        answer = solution(depth + 1, new_board)
        max_answer = max(answer, max_answer)
    return max_answer

if __name__ == '__main__':
    N = int(input())
    given_board = [] 
    for __ in range(N):
        given_board.append(list(map(int, input().split())))
    answer = solution(0, given_board)
    print(answer)
