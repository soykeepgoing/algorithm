'''
8 9
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 1 1 0 0 0 1 1 0 
0 1 0 1 1 1 0 1 0 
0 1 0 0 1 0 0 1 0 
0 1 0 1 1 1 0 1 0 
0 1 1 0 0 0 1 1 0 
0 0 0 0 0 0 0 0 0 

'''

from collections import deque 
import sys 
input = sys.stdin.readline
four_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_possible_to_melt(row, col):
    count = 0
    for drow, dcol in four_directions:
        new_row, new_col = row + drow, col + dcol
        if 0 <= new_row < N and 0 <= new_col < M:
            if board[new_row][new_col] == 3:
                count += 1
    return True if count >= 2 else False

def melt_cheese(cheese):
    for row, col in cheese:
        board[row][col] = 3

def check_edge_air():
    visited = [[False for __ in range(M)] for __ in range(N)]
    row, col = 0, 0
    queue = deque([(row, col)])
    visited[row][col] = True
    board[row][col] = 3
    while queue:
        row, col = queue.popleft()
        for dr, dc in four_directions:
            new_row, new_col = row + dr, col + dc 
            if 0 <= new_row < N and 0 <= new_col < M:
                if board[new_row][new_col] != 1 and not visited[new_row][new_col]:
                    board[new_row][new_col] = 3
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = True

def solution():
    time = 0
    while True:
        
        going_to_melt = set()

        check_edge_air() # 외부 공기 표시 

        # print()
        # for i in range(N):
        #     print(board[i])

        for row in range(N):
            for col in range(M):
                if board[row][col] == 1:
                    if is_possible_to_melt(row, col):
                        going_to_melt.add((row, col))

        if len(going_to_melt) == 0:
            return time 
        else:
            melt_cheese(going_to_melt)

        time += 1


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    board = [] 
    for __ in range(N):
        board.append(list(map(int, input().split())))
    time = solution()
    print(time)