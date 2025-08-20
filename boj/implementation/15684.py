def check():
    for start_pos in range(n):
        now_pos = start_pos
        for line in range(h):
            if board[line][now_pos]:
                now_pos += 1
            elif now_pos > 0 and board[line][now_pos - 1]:
                now_pos -= 1
            
        if now_pos != start_pos:
            return False
    return True 

def solution(cnt, x, y):
    global answer
    if check():
        answer = min(answer, cnt)
        return 
    elif cnt == 3 or answer <= cnt:
        return 
    
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0 

        for j in range(now, n - 1):
            if not board[i][j] and not board[i][j + 1]:
                if j > 0 and board[i][j - 1]:
                    continue 
                board[i][j] = True 
                solution(cnt + 1, i, j + 2) 
                board[i][j] = False 


if __name__ == '__main__':
    n, m, h = list(map(int, input().split()))
    board = [[False] * n for __ in range(h)]
    for __ in range(m):
        a, b = list(map(int, input().split()))  
        board[a - 1][b - 1] = True 
    
    answer = 4 
    solution(0, 0, 0)
    if answer >= 4:
        answer = -1 
    print(answer)
