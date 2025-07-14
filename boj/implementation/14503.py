DIRECTIONS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
BACK_DIRECTIONS = [[1, 0], [0, -1], [-1, 0], [0, 1]] # 후진 방향
FORE_DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  #전진 
D_LIST = [3, 0, 1, 2] # 반시계 90도 

def get_rest_rooms(board, x, y):
    global N, M
    count = 0 
    for DX, DY in DIRECTIONS:
        x_new = x + DX; y_new = y+ DY 
        if x_new in range(N) and y_new in range(M):
            if board[x_new][y_new] == 0:
                count += 1
    return count 

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    r, c, d = list(map(int, input().split())) # 현재 좌표, 방향 
    room_states = [list(map(int, input().split())) for _ in range(N)]
    answer = 0 
    while 1: 
        # print(r, c, d, answer)

        # 1번 룰 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if room_states[r][c] == 0:
            room_states[r][c] = 2
            answer += 1

        count = get_rest_rooms(room_states, r, c)
        if count == 0: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
            r = r + BACK_DIRECTIONS[d][0]
            c = c + BACK_DIRECTIONS[d][1]
            if r in range(N) and c in range(M) and room_states[r][c] == 1:
                print(answer)
                exit()
        else: 
            for _ in range(4):
                d = D_LIST[d]
                new_r = r + FORE_DIRECTIONS[d][0]
                new_c = c + FORE_DIRECTIONS[d][1]

                if (new_r in range(N) and new_c in range(M)) and (room_states[new_r][new_c] == 0):
                    r = new_r 
                    c = new_c 
                    break 

    print(answer)