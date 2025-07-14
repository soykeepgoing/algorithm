if __name__ == '__main__':
    N = int(input())
    power_list = list(map(int, input().split()))
    joy_list = list(map(int, input().split()))

    max_joy = sum(joy_list)
    dp = [100 for _ in range(max_joy + 1)]
    dp[0] = 0

    for i in range(N):
        power = power_list[i]
        joy = joy_list[i]
        for j in range(max_joy, joy - 1, -1):
            if j >= joy:
                dp[j] = min(dp[j], dp[j - joy] + power)

    for i in range(max_joy, -1, -1):
        if dp[i] in range(0, 100):
            print(i)
            break 
    # print(dp)
