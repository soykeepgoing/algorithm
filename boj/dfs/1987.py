import sys 
input = sys.stdin.readline 

def  search(board, visited, R, C, x, y, count):
    global ans
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dx, dy in direction:
        x_new = x + dx; y_new = y + dy
        if x_new in range(R) and y_new in range(C):
            visited_index = ord(board[x_new][y_new]) - 65
            if not visited[visited_index]:
                visited[visited_index] = True
                new_count = search(board, visited, R, C, x_new, y_new, count + 1)
                ans = max(ans, new_count)
                visited[visited_index] = False
    return count
            
if __name__ == '__main__':
    R, C = list(map(int, input().split()))
    board = [] 
    for _ in range(R):
        board.append(list(input()))
    ans = 1
    visited = [False for _ in range(26)]
    visited[ord(board[0][0]) - 65] = True
    count = search(board, visited, R, C,  x = 0, y = 0, count = 1)
    print(ans)