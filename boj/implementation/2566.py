if __name__ == '__main__':
    board = []
    for _ in range(9):
        board.append(list(map(int, input().split())))

    max_num = -1 

    for i in range(9):
        for j in range(9):
            max_num = max(max_num, board[i][j])
            if max_num == board[i][j]:
                max_num_i = i
                max_num_j = j

    print(max_num)
    print(max_num_i + 1, max_num_j + 1)