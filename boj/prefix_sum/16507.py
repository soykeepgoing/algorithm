import sys 
input = sys.stdin.readline 
if __name__ == '__main__':
    R, C, Q = list(map(int, input().split()))
    board = [[0 for _ in range(C + 1)]]
    for _ in range(R):
        board.append([0] + list(map(int, input().split())))
    
    # 누적합 구하기 
    for r in range(1, R + 1):
        for c in range(2, C + 1):
            board[r][c] += board[r][c - 1]

    for _ in range(Q):
        r1, c1, r2, c2 = list(map(int, input().split()))
        answer = 0 
        for r in range(r1, r2 + 1):
            answer += board[r][c2]
            answer -= board[r][c1 - 1]
        count = (r2 - r1 + 1) * (c2 - c1 + 1)
        print(answer // count)