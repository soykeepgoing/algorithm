from collections import deque 

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
rows, cols = 12, 6

def pop(x, y, visited):
    queue = deque([(x, y)])
    positions = [(x, y)]
    puyo = board[x][y]
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy 
            if 0 <= new_x < rows and 0 <= new_y < cols:
                if board[new_x][new_y] == puyo and not visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    positions.append((new_x, new_y))
                    visited[new_x][new_y] = True 
    
    return positions 


def flow_down(positions):
    for position in positions:
        x, y = position
        for row_index in range(x, 0, -1):
            board[row_index][y] = board[row_index - 1][y]
        board[0][y] = '.'

def solution():
    pop_num = 0 
    
    while True:
        visited = [[False] * cols for __ in range(rows)]
        possible_pop_positions = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != '.':
                    visited[i][j] = True 
                    new_position = pop(i, j, visited)
                    if len(new_position) >= 4:
                        possible_pop_positions.append(new_position)
        
        if not possible_pop_positions:
            break 

        for pop_position in possible_pop_positions:
            flow_down(pop_position)

        pop_num += 1 
    
    return pop_num

if __name__ == '__main__':
    board = [] 
    for __ in range(rows):
        board.append(list(input()))
    answer = solution()
    print(answer)
