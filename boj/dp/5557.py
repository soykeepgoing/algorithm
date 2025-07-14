import sys 
INF = 21

if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    board = [[0 for _ in range(21)] for _ in range(N + 1)]
    
    for i, num in enumerate(nums[:-1]):
    
        if i == 0:
            board[i][num] += 1
        else:
            for num2 in range(0, 21):
                if board[i-1][num2] > 0: # 하나라도 있다면   

                    if num + num2 in range(0, 21):
                        board[i][num + num2] += board[i - 1][num2]
                    if num2 - num in range(0, 21):
                        board[i][num2 - num] += board[i - 1][num2]


    print(board[N - 2][nums[-1]])