'''

1 3 
2 1
3 1
4 5
5 5
6 4
7 6

1, 3, 5
3, 1, 5

N 최대 100 

'''
import sys 
input = sys.stdin.readline 

def dfs(n):
    if not visited[n]:
        visited[n] = True 
        up.add(n)
        down.add(nums[n])
        if up == down:
            answer.extend(list(down))
            return 
        dfs(nums[n])

if __name__ == '__main__':
    N = int(input())
    nums = [-1] 
    for _ in range(N):
        nums.append(int(input()))

    answer = [] 

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        up, down = set(), set()
        dfs(i)

    answer = list(set(answer))
    answer.sort()

    print(len(answer))
    for num in answer:
        print(num)
