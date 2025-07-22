import copy 
import sys 
input = sys.stdin.readline 

def is_possible(i, j, new_i, new_j, board):
    for tmp_i in range(i, new_i):
        for tmp_j in range(j, new_j):
            if tmp_i >= 10 or tmp_j >= 10 or board[tmp_i][tmp_j] == 0: # 0이 아니라면
                return False
    return True

def get_new_board(board, i, j, new_i, new_j):
    for tmp_i in range(i, new_i):
        for tmp_j in range(j, new_j):
            board[tmp_i][tmp_j] = 0
    return board

def solution(start_i, start_j, board, papers, paper_used_now, deleted):
    global answer 
    if deleted == total_one_count:
        answer = min(paper_used_now, answer)
        return
    
    for i in range(start_i, 10):
        for j in range(10):
            if board[i][j] == 1:
                for paper_size in range(5, 0, -1): # 탐색할 수 있는 색종이의 범위만큼
                    if papers[paper_size] > 0: # 사용할 수 있는 색종이가 존재한다면 
                        new_i, new_j = i + paper_size, j + paper_size  
                        if is_possible(i, j, new_i, new_j, board): # 색종이로 덮을 수 있다면 
                            new_board = get_new_board(copy.deepcopy(board), i, j, new_i, new_j) # 새로운 보드 정의
                            papers[paper_size] -= 1
                            solution(i, j, new_board, papers, paper_used_now + 1, deleted + paper_size * paper_size)
                            papers[paper_size] += 1
                return 


if __name__ == '__main__':
    o_board = [] 
    total_one_count = 0
    for _ in range(10):
        o_board.append(list(map(int, input().split())))
        for i in range(10):
            if o_board[-1][i] == 1:
                total_one_count += 1
    papers = [0, 5, 5, 5, 5, 5]
    paper_used_now = 0
    answer = 26
    solution(0, 0, o_board, papers, paper_used_now, deleted = 0)
    if answer == 26:
        answer = -1
    print(answer)
