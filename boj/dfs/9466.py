import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve_case():
    in_team = [False] * m 
    state = [0] * m 

    def dfs(node):
        state[node] = 1
        next_node = students[node]
        if state[next_node] == 0:
            dfs(next_node)
        elif state[next_node] == 1: # 순환을 발견 (처리 중인 상태이므로)
            cur = next_node
            while True:
                in_team[cur] = True 
                cur = students[cur]
                if cur == next_node:
                    break 
        state[node] = 2

    for i in range(m):
        dfs(i)

    return m - sum(in_team)

def minus(x):
    return x - 1

if __name__ == '__main__':
    n = int(input())
    for __ in range(n):
        m = int(input())
        students = list(map(int, input().split()))
        students = list(map(minus, students))
        answer = solve_case()
        print(answer)
