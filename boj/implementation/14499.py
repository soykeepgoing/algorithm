EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4
DIRECTION = {
    EAST: (0, 1), 
    WEST: (0, -1),
    NORTH: (-1, 0), 
    SOUTH: (1, 0)
}

def spin_dice(dice, order):
    top, north, east, west, south, bottom = dice
    if order == EAST: # 동쪽인 경우 
        return [west, north, top, bottom, south, east]
    elif order == WEST: # 서쪽인 경우 
        return [east, north, bottom, top, south, west]
    elif order == SOUTH: # 남쪽인 경우 
        return [south, top, east, west, bottom, north]
    elif order == NORTH: # 북쪽인 경우
        return [north, bottom, east, west, top, south]

def move(board, dice, x, y, direction):
    dx, dy = DIRECTION[direction]
    nx, ny = x + dx, y + dy 
    
    if not(0 <= nx < len(board) and 0 <= ny < len(board[0])):
        return x, y, dice

    dice = spin_dice(dice, direction)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0    

    print(dice[0])
    return nx, ny, dice

def solution(board, orders, x, y):
    dice = [0, 0, 0, 0, 0, 0]
    for direction in orders: 
        x, y, dice = move(board, dice, x, y, direction)


if __name__ == '__main__':
    N, M, X, Y, K = list(map(int, input().split()))
    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))
    orders = list(map(int, input().split()))
    solution(board, orders, X, Y)