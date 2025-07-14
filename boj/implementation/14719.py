if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    blocks = list(map(int, input().split()))

    board = [[False for _ in range(W)] for _ in range(H)]

    for i, block in enumerate(blocks): 
        for j in range(H - 1, (H - 1) - block, -1):
            board[j][i] = True 

    total = 0
    for i in range(H):
        for j in range(W):
            if j == 0:
                tmp = 0
                if board[i][j] == True: state = True 
                else: state = False
            else:
                if board[i][j] == True and state == True: 
                    total += tmp
                    tmp = 0 
                elif board[i][j] == False and state == True:
                    tmp += 1
                elif board[i][j] == True and state == False:
                    state = True
                

    print(total)