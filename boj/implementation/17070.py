directions = {
    0: [(0, 0, 1), (2, 1, 1)], 
    1: [(1, 1, 0), (2, 1, 1)], 
    2: [(0, 0, 1), (1, 1, 0), (2, 1, 1)], 
}

count = 0 

def find_wall(x, y):
    if x + 1 < n and board[x + 1][y] == 1: return True 
    if y + 1 < n and board[x][y + 1] == 1: return True 
    return False 

def solution(type, x, y):
    global count 
    if (x, y) == (n - 1, n - 1): # 종료 지점에 다다랐다면 리턴 
        count += 1
        return 
    
    for dtype, dx, dy in directions[type]:
        new_x, new_y = x + dx, y + dy 
        if new_x >= n or new_y >= n: continue
        if board[new_x][new_y] == 1: continue # 파이프는 빈칸에만 존재한다. 
        if dtype == 2 and find_wall(x, y): continue # 파이프를 밀때 벽에 안 부딪히도록 해야 한다. 
        solution(dtype, new_x, new_y)

if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for __ in range(n)]
    if board[n - 1][n - 1] == 1: # 도착지점에 벽이 있다면 탐색할 수 있는 방법이 존재하지 않는다. 
        print(0)
    else: 
        solution(0, 0, 1)
        print(count)
