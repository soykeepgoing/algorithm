import sys
import heapq 

input = sys.stdin.readline 

if __name__ == '__main__':

    INF = sys.maxsize
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상하좌우 인덱스 
    case = 0

    while 1: 
        N = int(input())

        if N == 0: 
            break 

        case += 1

        board = [] 
        for _ in range(N):
            board.append(list(map(int,input().split())))

        distance = [[INF for _ in range(N)] for _ in range(N)] # 최소 비용 저장 리스트 
        distance[0][0] = board[0][0]

        queue = []
        heapq.heappush(queue, (board[0][0], 0, 0))

        while queue: 
            cost, x, y = heapq.heappop(queue)

            for dx, dy in direction:
                x_new = x + dx; y_new = y + dy 
                if x_new in range(N) and y_new in range(N):
                    new_cost = cost + board[x_new][y_new]
                    if new_cost < distance[x_new][y_new]: # new cost가 기존의 비용보다 작다면 갱신 및 추가 탐색 
                        distance[x_new][y_new] = new_cost 
                        heapq.heappush(queue, (new_cost, x_new, y_new))

        print(f"Problem {case}: {distance[N-1][N-1]}")