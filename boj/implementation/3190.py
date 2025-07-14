from collections import deque 

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def snake():
    x = 0
    y = 0 
    snake = deque([[x, y]]) 
    d = 1 # 현재 방향 
    time = 0

    while True: 
        # print(snake)
        # 새 머리 
        new_x = x + dx[d]
        new_y = y + dy[d]

        if (new_x not in range(N) or new_y not in range(N)) or ([new_x, new_y] in snake): # 벽이나 자기자신의 몸과 부딪히는 경우 
            return time     
        
        if board[new_x][new_y] == 1: 
            board[new_x][new_y] = 0 
        else: # 사과가 없다면 
            snake.popleft() # 꼬리 위치 빼기 

        # print(time, new_x, new_y, history, board[new_x][new_y])

        snake.append([new_x, new_y]) 
        time += 1 

        if history:
            if time == int(history[0][0]): # 방향을 바꿔야 한다면 
                t, new_d = history.popleft()
                if new_d == 'D':
                    d = (d + 1) % 4
                else:
                    nd = 3 if d == 0 else d - 1
                    d = nd
    
        x = new_x; y = new_y


if __name__ == '__main__':
    N = int(input())
    K = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        x, y = list(map(int, input().split()))
        board[x - 1][y - 1] = 1 # 사과 

    L = int(input())
    history = deque([])
    for _ in range(L):
        history.append(input().split())

    answer = snake()
    print(answer + 1)
    