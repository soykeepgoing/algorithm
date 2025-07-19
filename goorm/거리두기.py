def solution():
	dp = [[0, 0, 0, 0, 0] for __ in range(N + 1)]
	if (N == 1): return 5
	dp[1] = [1, 1, 1, 1, 1]
	dp[2] = [5, 3, 4, 3, 2]
	pre_sum = 17
	for i in range(3, N + 1):
		dp[i][0] = pre_sum % 100000007
		dp[i][1] = (pre_sum - dp[i - 1][1] - dp[i - 1][4]) % 100000007
		dp[i][2] = (pre_sum - dp[i - 1][2]) % 100000007
		dp[i][3] = (pre_sum - dp[i - 1][3] - dp[i - 1][4]) % 100000007
		dp[i][4] = (pre_sum - dp[i - 1][1] - dp[i - 1][3] - dp[i - 1][4]) % 100000007

		pre_sum = sum(dp[i])
		
	return sum(dp[N]) % 100000007
	
if __name__ == '__main__':
	N = int(input())
	answer = solution()
	print(answer)
