import sys
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def backtrack(count, total):
    global answer

    if count == K: 
        answer = max(answer, total)
        return 

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                bad = False 
                for di, dj in DIR:
                    ni, nj = i + di, j + dj 
                    if ni in range(N) and nj in range(M):
                        if visited[ni][nj]:
                            bad = True 
                            break 
            
                if bad:
                    continue 
                
                visited[i][j] = True 
                backtrack(count + 1, total + board[i][j])
                visited[i][j] = False


if __name__ == '__main__':
    N, M, K = list(map(int, input().split()))
    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = -float('inf')
    visited = [[False for _ in range(M)] for _ in range(N)]

    backtrack(0, 0)

    print(answer)
