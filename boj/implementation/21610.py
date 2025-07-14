import sys 
input = sys.stdin.readline 

DIRECTION = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
DIAG_DIRECTION = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def main(board, moves, clouds, N): 
    # 1. 구름 이동 
    for d, s in moves:
        d -= 1
        moved_clouds = []
        for r, c in clouds: 
            nr, nc = (r+ DIRECTION[d][0] * s) % N, (c + DIRECTION[d][1] * s) % N
            board[nr][nc] += 1 # 2. 구름 위치에서 물의 양 추가 
            moved_clouds.append((nr, nc))
    
        # 4. 물복사버그 마법 
        for r, c in moved_clouds:
            cnt = 0 
            for i in range(4):
                nr, nc = r + DIAG_DIRECTION[i][0], c + DIAG_DIRECTION[i][1]
                if (nr in range(N) and nc in range(N)) and (board[nr][nc] > 0): 
                    cnt += 1
            board[r][c] += cnt 

        # 구름 배열 업데이트 
        new_clouds = [] 
        for r in range(N):
            for c in range(N):
                # if [r, c] in moved_clouds or board[r][c] < 2: continue 
                if (r, c) not in moved_clouds and board[r][c] >= 2: 
                    new_clouds.append([r, c])
                    board[r][c] -= 2
    
        clouds = new_clouds
    
    # 물의 양의 합 구하기 
    answer = 0 
    for r in range(N):
        for c in range(N):
            answer += board[r][c]
    
    return answer

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
    moves = [list(map(int, input().split())) for _ in range(M)]
    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
    answer = main(board, moves, clouds, N)
    # print(board)
    print(answer)