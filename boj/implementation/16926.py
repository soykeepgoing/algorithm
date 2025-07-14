def get_locations_depth(N, M, depth):
    locations = [] 

    for row in range(depth, N - depth): # 아래로 
        locations.append([row, depth])
    
    for col in range(depth + 1, M - depth): # 오른쪽 
        locations.append([row, col])
    
    for row in range(row - 1, depth - 1, -1): # 위쪽 
        locations.append([row, col])
    
    for col in range(col -1, depth, -1):
        locations.append([row, col])
    
    return locations 


if __name__ == '__main__':
    N, M, R = list(map(int, input().split()))

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    new_board = [[0 for _ in range(M)] for _ in range(N)]

    repeat = min(N, M) // 2

    for depth in range(repeat): # 몇 개의 depth가 나올까? 
        locations = get_locations_depth(N, M, depth)

        # swap하는 번호 
        swap_num = R % len(locations)

        # new_board 선언 후 새롭게 값 넣기 
        new_locations = locations[swap_num:] + locations[:swap_num]

        for i in range(len(locations)):
            x, y = locations[i]
            value = board[x][y]
            new_x, new_y = new_locations[i]
            new_board[new_x][new_y] = value
    
    for i in range(N):
        print(*new_board[i])