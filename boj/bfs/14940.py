'''
bfs로 탐색가능한 위치라면 이전에서 +1하면 된다. 

2를 출발점으로 하나씩 탐색하면서 1씩 더해준다. 

탐색이 끝나고 visited false인 부분에 대해서 원래 0이라면 0을, 1이라면 -1을 대입

'''
from collections import deque 
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy 
            if 0 <= new_x < n and 0 <= new_y < m:
                if board[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    distance_results[new_x][new_y] = distance_results[x][y] + 1
                    visited[new_x][new_y] = True 
                    queue.append((new_x, new_y))

def check_not_visited():
    for x in range(n):
        for y in range(m):
            if  board[x][y] == 0:
                distance_results[x][y] = 0 

def solution(queue):
    bfs(queue)
    check_not_visited()
    for i in range(n):
        print(*distance_results[i])

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    visited = [[False for __ in range(m)] for __ in range(n)]
    distance_results = [[-1 for __ in range(m)] for __ in range(n)]
    board = [] 
    for row in range(n):
        board.append(list(map(int, input().split())))
        if 2 in board[-1]:
            for col in range(m):
                if board[-1][col] == 2:
                    queue = deque([(row, col)])
                    visited[row][col] = True
                    distance_results[row][col] = 0

    solution(queue)'''
bfs로 탐색가능한 위치라면 이전에서 +1하면 된다. 

2를 출발점으로 하나씩 탐색하면서 1씩 더해준다. 

탐색이 끝나고 visited false인 부분에 대해서 원래 0이라면 0을, 1이라면 -1을 대입

'''
from collections import deque 
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy 
            if 0 <= new_x < n and 0 <= new_y < m:
                if board[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    distance_results[new_x][new_y] = distance_results[x][y] + 1
                    visited[new_x][new_y] = True 
                    queue.append((new_x, new_y))

def check_not_visited():
    for x in range(n):
        for y in range(m):
            if  board[x][y] == 0:
                distance_results[x][y] = 0 

def solution(queue):
    bfs(queue)
    check_not_visited()
    for i in range(n):
        print(*distance_results[i])

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    visited = [[False for __ in range(m)] for __ in range(n)]
    distance_results = [[-1 for __ in range(m)] for __ in range(n)]
    board = [] 
    for row in range(n):
        board.append(list(map(int, input().split())))
        if 2 in board[-1]:
            for col in range(m):
                if board[-1][col] == 2:
                    queue = deque([(row, col)])
                    visited[row][col] = True
                    distance_results[row][col] = 0

    solution(queue)
