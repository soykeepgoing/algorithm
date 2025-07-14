from collections import deque 
import sys 
input = sys.stdin.readline 
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j, board, visited, N, L, R):
    queue = deque([[i, j]])

    sum_people = board[i][j] 
    count_country = 1
    mem_country = [] 

    while queue:
        i, j = queue.popleft()
        mem_country.append([i, j])
        value = board[i][j]

        for di, dj in DIRECTIONS:
            ni = i + di 
            nj = j + dj 
            if ni in range(N) and nj in range(N):
                if not visited[ni][nj]:
                    if abs(value - board[ni][nj]) in range(L, R + 1):
                        queue.append([ni, nj])
                        visited[ni][nj] = True 
                        count_country += 1    
                        sum_people += board[ni][nj] 

    new_value = sum_people // count_country

    for i, j in mem_country: 
        board[i][j] = new_value

    return count_country


def has_more(board, N, L, R):
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    flag = False 

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True 
                count_country = bfs(i, j, board, visited, N, L, R)
                if count_country > 1: 
                    flag = True
    return flag


def main():
    N, L, R = list(map(int, input().split()))

    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))

    day = 0 
    while 1: 
        flag = has_more(board, N, L, R)
        if not flag: 
            return day 
        day += 1
    
if __name__ == '__main__':
    ans = main()
    print(ans)

    
