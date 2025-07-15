INF = 10**10

def solve():
	answer = INF

	prefix_sum = [[0 for __ in range(N + 1)] for __ in range(N + 1)]
	
	for i in range(N):	
		for j in range(N):
			prefix_sum[i + 1][j + 1] = board[i][j] + prefix_sum[i + 1][j] + prefix_sum[i][j + 1] - prefix_sum[i][j]

	for i in range(N - K + 1):
		for j in range(N - K + 1):
			total = ( prefix_sum[i + K][j + K] +
								prefix_sum[i][j] -
								prefix_sum[i + K][j] -
								prefix_sum[i][j + K] )
			answer = min(total, answer)
	
	return answer 

if __name__ == '__main__':
	T = int(input())
	for __ in range(T):
		N, K = list(map(int, input().split()))
		board = [] 
		for __ in range(N):
			board.append(list(map(int, input().split())))
		answer = solve()
		print(answer)