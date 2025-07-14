if __name__ == '__main__':
    N = int(input())
    nums = [0] + list(map(int, input().split()))

    dp = nums[:]

    for i in range(2, N + 1):
        for j in range(i // 2, 0, -1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])

    print(dp[N])

