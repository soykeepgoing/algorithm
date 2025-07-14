def solution(n):
    if n[0] == '0':
        return 0

    dp = [0] * (len(n) + 1)
    dp[0] = 1
    dp[1] = 1

    for index in range(2, len(n) + 1): # dp index
        n_index = index - 1
        
        # 한자리로 붙는 경우 
        if n[n_index] != '0': 
            dp[index] += dp[index - 1]

        # 두자리로 붙는 경우 
        if (int(n[n_index - 1]) * 10 + int(n[n_index])) in range(10, 27):
            dp[index] += dp[index - 2]

    return dp[-1]


if __name__ == '__main__':
    num  = list(input())
    ans = solution(num)
    print(ans % 1000000)