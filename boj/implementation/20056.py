'''
1. 이동하는 함수 
=> 순환되도록 모듈러 연산 
2. 동시에 같이 있으면 흩어지도록 하는 연산 
'''
def print_board(b):
    for i in range(N):
        print(b[i])
    print()

def get_new_location(i, j, s, d):
    if d == 0:
        new_i, new_j = (i - s) % N, j
    elif d == 1:
        new_i, new_j = (i - s) % N, (j + s) % N
    elif d == 2:
        new_i, new_j = i, (j + s) % N 
    elif d == 3:
        new_i, new_j = (i + s) % N, (j + s) % N
    elif d == 4:
        new_i, new_j = (i + s) % N, j 
    elif d == 5:
        new_i, new_j = (i + s) % N, (j - s) % N 
    elif d == 6:
        new_i, new_j = i, (j - s) % N 
    elif d == 7:
        new_i, new_j = (i - s) % N, (j - s) % N 
    return new_i, new_j

def get_total_mass():
    total_mass = 0 
    for i in range(N):
        for j in range(N):
            for m, s, d, k in board[i][j]:
                total_mass += m 
    return total_mass

def move_ball(now_k):
    for i in range(N):
        for j in range(N):
            new_balls = []
            for m, s, d, k in board[i][j]:
                if k == now_k + 1:
                    new_balls.append((m, s, d, k))
                    continue 
                new_i, new_j = get_new_location(i, j, s, d)
                board[new_i][new_j].append((m, s, d, k + 1))
            board[i][j] = new_balls
    # print_board(board)
    return board

def spread_balls():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) <= 1:
                continue

            new_balls = []
            total_mass = 0
            total_speed = 0 
            directions = 0
            count = 0 
            for m, s, d, k in board[i][j]:
                total_mass += m 
                total_speed += s 
                directions += d % 2
                count += 1
            
            if directions == 0 or directions == count:
                total_directions = [0, 2, 4, 6]
            else:
                total_directions = [1, 3, 5, 7]
            
            if total_mass // 5 == 0:
                board[i][j] = new_balls
                continue 

            for index in range(4):
                new_balls.append((total_mass // 5, total_speed // count, total_directions[index], k))
            board[i][j] = new_balls
            
def solution():
    # print_board(board)
    for k in range(K):
        move_ball(k)
        spread_balls()
    # print_board(board)
    total_mass = get_total_mass()
    return total_mass 

if __name__ == '__main__':
    N, M, K = list(map(int, input().split()))
    board = [[[] for __ in range(N)] for __ in range(N)]

    for __ in range(M):
        r, c, m, s, d = list(map(int, input().split()))
        board[r - 1][c - 1].append((m, s, d, 0))

    answer = solution()
    print(answer)
