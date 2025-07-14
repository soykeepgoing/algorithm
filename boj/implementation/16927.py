def get_locations_depth(N, M, depth):
    locations = [] 
    
    for row in range(depth, N - depth): # 아래로
        locations.append([row, depth])
    
    for col in range(depth + 1, M - depth): # 오른쪽
        locations.append([row, col])
    
    for row in range(N - depth - 2, depth - 1, -1): # 위쪽
        locations.append([row, col])
    
    for col in range(M - depth - 2, depth - 1, -1):
        locations.append([row, col])

    locations.pop()
    return locations
    

if __name__ == '__main__':
    N, M, R = list(map(int, input().split()))

    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))

    total_depth = min(N, M) // 2
    new_board = [[0 for _ in range(M)] for _ in range(N)]

    for depth in range(total_depth):
        locations = get_locations_depth(N, M, depth)
        new_R = R % len(locations)
        print(new_R)

        new_locations = locations[new_R:] + locations[:new_R]
        print(locations)

        for i in range(len(locations)):
            x, y = locations[i]
            value = board[x][y]
            new_x, new_y = new_locations[i]
            new_board[new_x][new_y] = value

    for i in range(N):
        print(*new_board[i])