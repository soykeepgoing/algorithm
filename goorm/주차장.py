from collections import deque 

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
scores = { 0: 1, 2: -2}

def bfs(queue, score):
	while queue:
		x, y = queue.popleft()
		for dx, dy in direction:
			new_x, new_y = x + dx, y + dy
			if 0 <= new_x < N and 0 <= new_y < M:
				if not visited[new_x][new_y] and board[new_x][new_y] != 1:
					visited[new_x][new_y] = True 
					queue.append((new_x, new_y))
					score += scores[board[new_x][new_y]]
	return score 

def solution():
	score = -10e9
	for i in range(N):
		for j in range(M):
			if board[i][j] != 1 and not visited[i][j]:
				queue = deque([(i, j)])
				visited[i][j] = True 
				score = max(score, bfs(queue, scores[board[i][j]]))
	return score 
				

if __name__ == '__main__':
	N, M = list(map(int, input().split()))
	board = [list(map(int, input().split())) for __ in range(N)]
	visited = [[False for __ in range(M)] for __ in range(N)]
	answer = solution()
	if answer < 0: answer = 0
	print(answer)