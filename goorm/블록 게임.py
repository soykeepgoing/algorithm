directions = {
	'R': (0, 1),
	'L': (0, -1), 
	'U': (-1, 0), 
	'D': (1, 0)
}

def get_new_pos(position, order):
	return (position[0] + directions[order][0], position[1] + directions[order][1])

def solution():
	answer = 1
	infos = [(0, 0, 1)]
	history = set([(0, 0)])
	pos = (0, 0)
	
	for i in range(N):
		order = orders[i]
		score = scores[i]
		new_pos = get_new_pos(pos, order)
		info = (new_pos[0], new_pos[1], score)

		# print(history, infos)

		while new_pos in history:
			x, y, s = infos.pop()
			answer -= s
			history.remove((x,y))

		history.add(new_pos)
		infos.append(info)
		answer += score
		pos = new_pos

	return answer

if __name__ == '__main__':
	N = int(input())
	orders = input()
	scores = list(map(int, input().split()))
	answer = solution()
	print(answer)
