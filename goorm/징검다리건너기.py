def solution():
	if N <= 3:
		return 0 
	
	dp = [0 for _ in range(N)]
	dp[0] = potion[0]
	dp[1] = potion[1]
	dp[2] = potion[2]

	for i in range(3, N):
		dp[i] = potion[i] + min(dp[i - 1], dp[i - 2], dp[i - 3])

	return min(dp[N - 1], dp[N - 2], dp[N - 3])

	
if __name__ == '__main__':
	N = int(input())
	potion = list(map(int, input().split()))
	answer = solution()
	print(answer)