# import sys 
# input = sys.stdin.readline 

def get_key(board, N):
    key = set()
    data = dict()
    for rindex in range(3):
        row = ''.join(sorted(board[rindex]))
        if len(set(row)) == N:
            if row not in data.keys():
                data[row] = 1
            else:
                data[row] += 1
    # print(data)
    for k, v in data.items():
        if v >= 2:
            key = k 
    return key         

def search(board, N):
    key = get_key(board, N)
    wrong_row, wrong_col = -1, -1
    ans = ''

    for r_index in range(N):
        for c_index in range(N):
            tshirt = board[r_index][c_index]
            for pre_c_index in range(c_index):
                if wrong_row == -1:
                    if tshirt == board[r_index][pre_c_index]: # 같은 행 검사 
                        wrong_row = r_index
                        for other_r_index in range(N): # 같은 열 검사 
                            if other_r_index != r_index: # 현재 행이 아닌 경우 
                                if tshirt == board[other_r_index][c_index]: # 중복되는 열이 있다면 
                                    wrong_col = c_index
                        if wrong_col == -1:
                            wrong_col = pre_c_index
            if tshirt not in key:
                wrong_row = r_index
                wrong_col = c_index

    for k in key:
        if k not in board[wrong_row]:
            ans = k 
    return wrong_row, wrong_col, ans

if __name__ == '__main__':
    while True:
        try:
            N = int(input())
        except:
            break

        board = [] 
        for _ in range(N):
            board.append(list(input()))

        wrong_row, wrong_col, ans = search(board, N)
        print(wrong_row + 1, wrong_col + 1, ans)
