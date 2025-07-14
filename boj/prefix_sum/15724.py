import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    board = [[0 for _ in range(M + 1)]] 
    for _ in range(N):
        people = [0] + list(map(int, input().split()))

        for j in range(2, M + 1):
            people[j] += people[j - 1]

        board.append(people)
    
    # print(board)

    K = int(input())
    for _ in range(K):
        x1, y1, x2, y2 = list(map(int, input().split()))
        people_sum = 0 
        for x in range(x1, x2 + 1):
            people_sum += board[x][y2]
        for x in range(x1, x2 + 1):
            people_sum -= board[x][y1 - 1]
        
        print(people_sum)