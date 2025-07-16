direction = {
	'L': [0, -1], 
	'R': [0, 1], 
	'U': [-1, 0], 
	'D': [1, 0]
}
def get_order(x, y):
	order = list(board[x][y])
	command = order.pop()
	count = int(''.join(order))
	return count, command
		
def search(start):
	position = [start[0] - 1, start[1] - 1]
	visited = [[False for __ in range(N)] for __ in range(N)]
	score = 1
	while 1:
		x, y = position
		visited[x][y] = True 
		count, command = get_order(x, y)
		dx, dy = direction[command]
		for __ in range(count):
			new_x = (x + dx) % N 
			new_y = (y + dy) % N 
			if not visited[new_x][new_y]:
				visited[new_x][new_y] = True
				x, y = new_x, new_y
				score += 1
			else:
				return score
		position = [x, y]
			

if __name__ == '__main__':
	N = int(input())
	goorm = list(map(int, input().split()))
	player = list(map(int, input().split()))

	board = [input().split() for __ in range(N)]

	goorm_score = search(goorm)
	player_score = search(player)

	if goorm_score > player_score:
		print(f"goorm {goorm_score}")
	else:
		print(f"player {player_score}")