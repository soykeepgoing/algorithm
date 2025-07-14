# import sys 
# input = sys.stdin.readline 

# if __name__ == '__main__':
#     T = int(input())
#     nums = []
#     for _ in range(T):
#         nums.append(int(input()))
    
#     # max_num = max(nums)

#     dp = [0] * (100000 + 1)
#     dp[0] = (1, 0, 0, 0, 1)
#     dp[1] = (0, 1, 0, 0, 1)
#     dp[2] = (0, 0, 1, 0, 1)
#     dp[3] = (0, 1, 1, 1, 3)

#     start = 4
#     for i in range(start, 100000 + 1):
#         one = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
#         two = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
#         three = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009

#         total = one + two + three

#         dp[i] = (0, one, two, three, total)
        
#     for num in nums:
#         print(dp[num][4] % 1000000009)


import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    T = int(input())
    nums = []
    for _ in range(T):
        nums.append(int(input()))
    
    # max_num = max(nums)

    dp = [0] * (100000 + 1)
    dp[0] = (1, 0, 0, 0, 1)
    dp[1] = (0, 1, 0, 0, 1)
    dp[2] = (0, 0, 1, 0, 1)
    dp[3] = (0, 1, 1, 1, 3)

    start = 4
    for i in range(start, 100000 + 1):
        one = dp[i - 1][2] + dp[i - 1][3] 
        two = dp[i - 2][1] + dp[i - 2][3] 
        three = dp[i - 3][1] + dp[i - 3][2] 

        total = one + two + three
        total = total % 1000000009

        dp[i] = (0, one, two, three, total)
        
    for num in nums:
        print(dp[num][4])