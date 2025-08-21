'''
5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2

2 1 3
3 2 3

7(1) 8(1) 7 8 7
3(5,1) 8(1,1) 7(1) 8 7
7(1,1) 4(5, 1) 7(1) 8 7
7(1) 8(1) 7(1) 8 7 
7 8 7 8 7

100000


나무 위치를 기준으로 pop하면서 봄 여름 가을 겨울 ?



'''
from collections import deque 
import sys 
input = sys.stdin.readline

direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def solution():
    for _ in range(k):
        # 봄, 여름 
        for i in range(n):
            for j in range(n):
                if not trees[i][j]:
                    continue 
                alive = deque()
                dead_soil = 0
                original_trees = trees[i][j]
                while original_trees:
                    age = original_trees.popleft()
                    if soil_state[i][j] >= age:
                        soil_state[i][j] -= age
                        alive.append(age + 1)
                    else:
                        dead_soil += age // 2
                
                trees[i][j] = alive
                soil_state[i][j] += dead_soil
        
        for i in range(n):
            for j in range(n):
                if not trees[i][j]:
                    continue
                bread_cnt = 0
                for age in trees[i][j]:
                    if age % 5 == 0:
                        bread_cnt += 1
                
                if bread_cnt == 0: continue 

                for di, dj in direction:
                    ni, nj = i + di, j + dj 
                    if 0 <= ni < n and 0 <= nj < n:
                        trees[ni][nj].extendleft([1] * bread_cnt)

        for i in range(n):
            for j in range(n):
                soil_state[i][j] += a[i][j]

if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    soil_state = [[5] * n for __ in range(n)]
    trees = [[deque() for _ in range(n)] for __ in range(n)] 
    a = []
    for __ in range(n):
        a.append(list(map(int, input().split())))
    
    for __ in range(m):
        x, y, z = list(map(int, input().split()))
        trees[x - 1][y - 1].append(z)

    solution()
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += len(trees[i][j])
    
    print(answer)
