import copy
INF = 10e9

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

possible_index = {
    0: [0, 2, 3], 
    1: [1, 2, 3], 
    2: [0, 1, 2], 
    3: [0, 1, 3]
}


def get_new_pos(red_pos, blue_pos, index, board_tmp):
    red_r, red_c = red_pos
    blue_r, blue_c = blue_pos
    dr, dc = direction[index]
    is_red_hole, is_blue_hole = False, False 
    # board_tmp = [row[:] for row in new_board]
    while True:
        new_red_r, new_red_c = red_r + dr, red_c + dc 
        new_blue_r, new_blue_c = blue_r + dr, blue_c + dc

        flag = False

        if board_tmp[new_red_r][new_red_c] not in ['#', 'R', 'B']:
            # print(new_red_r, new_red_c)
            if board_tmp[new_red_r][new_red_c] == 'O':
                is_red_hole = True 
            board_tmp[new_red_r][new_red_c] = 'R'
            board_tmp[red_r][red_c] = '.'
            red_r, red_c = new_red_r, new_red_c
            flag = True 

        if board_tmp[new_blue_r][new_blue_c] not in ['#', 'R', 'B']:
            if board_tmp[new_blue_r][new_blue_c] == 'O':
                is_blue_hole = True   
            board_tmp[new_blue_r][new_blue_c] = 'B'
            board_tmp[blue_r][blue_c] = '.'
            blue_r, blue_c = new_blue_r, new_blue_c
            flag = True
        
        if not flag: # 변화가 없었다면 
            if board_tmp[new_blue_r][new_blue_c] == 'R' and (is_red_hole == True):
                is_blue_hole = True 
            return is_red_hole, is_blue_hole, (red_r, red_c), (blue_r, blue_c), board_tmp

def solution(depth, red_pos, blue_pos, index_list, visited, board_tmp):
    if depth == 10:
        return 10e9
    
    if (red_pos, blue_pos) in visited:
        return 10e9
    
    visited.add((red_pos, blue_pos))
    min_moves = 10e9
    
    for index in index_list:
        copied_board = copy.deepcopy(board_tmp)
        is_red_hole, is_blue_hole, new_red_pos, new_blue_pos, new_board = get_new_pos(red_pos, blue_pos, index, copied_board)
        # print(index, is_red_hole, is_blue_hole, new_red_pos, new_blue_pos)

        if is_blue_hole: # 실패한 경로 
            continue

        if is_red_hole:
            min_moves = min(min_moves, depth + 1)
            continue 

        moves = solution(depth + 1, new_red_pos, new_blue_pos, possible_index[index], visited, new_board)
        min_moves = min(min_moves, moves)

    visited.remove((red_pos, blue_pos))

    return min_moves


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    board = [] 
    for row in range(N):
        board.append(list(input()))
        if 'R' in board[-1]:
            red_pos = (row, board[-1].index('R'))
        if 'B' in board[-1]:
            blue_pos = (row, board[-1].index('B'))
        if 'O' in board[-1]:
            hole = (row, board[-1].index('O'))

    visited = set()
    answer = solution(0, red_pos, blue_pos, [0, 1, 2, 3], visited, board)
    answer = -1 if answer == 10e9 else answer
    print(answer)