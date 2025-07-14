from collections import deque 
import sys 
input = sys.stdin.readline 

def bfs(q, board, N, M):
    '''
    BFS 탐색, O(N * M) : 모든 칸을 한 번씩 방문 가능
    '''
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q:  
        i, j = q.popleft() 
        for di, dj in direction:
            if (i + di) in range(N) and (j + dj) in range(M):
                if board[i + di][j + dj] == 0: 
                    q.append([i + di, j + dj])
                    board[i + di][j + dj] = 3 
    return board

def get_area(board, N, M):
    '''
    O(N * M) 
    '''
    q = deque([])
    area = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2: 
                q.append([i, j])
                board = bfs(q, board, N, M) # BFS 실행 => O(NM) : BFS 이후에 한번 방문한 칸은 다시 탐색하지 않는다. 

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: 
                area += 1
            elif board[i][j] == 3: 
                board[i][j] = 0

    return area

def backtrack(board, N, M, count): 
    '''
    K = 벽을 세울 수 있는 칸의 개수 
    K개의 빈 칸 중 3개를 선택하는 모든 조합 계산 => K^3 
    O(K ^ 3 * NM) : 각 조합마다 get_area를 실행하기 때문에 
    '''
    ans = -1 
    if count == 3: 
        area = get_area(board, N, M) # => O(NM)
        return area
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: 
                board[i][j] = 1
                area= backtrack(board, N, M, count + 1) # => O(K ^ 3): 3개가 되면 종료되므로 
                ans = max(ans, area)
                board[i][j] = 0 
    return ans

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    board = [] 
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    ans = backtrack(board, N, M, count = 0) # => O(K ^ 3 * N * M)
    print(ans)