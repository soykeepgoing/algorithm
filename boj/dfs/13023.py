'''

5 4
0 1
1 2
2 3 
4 5

8 8
1 7 
3 7 
4 7 
3 4 
4 6
3 5 
0 4
2 7 
'''
    
def solution():
    def dfs(visited, cnt):

        if cnt == 5:
            # print(visited)
            print(1)
            exit(0)

        me = visited[-1]
        for friend in relationship[me]:
            # print(me, friend)
            if checked[friend]: continue
            checked[friend] = True  
            dfs(visited + [friend], cnt + 1)
            checked[friend] = False

    checked = [False] * n
    for me in range(n):
        checked[me] = True 
        dfs([me], 1)
        checked[me] = False
    
    return 0 
            

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    # relationship = [[False] * n for __ in range(n)]
    relationship = [[] for __ in range(n)]
    for __ in range(m):
        a, b = list(map(int, input().split()))
        relationship[a].append(b)
        relationship[b].append(a)

    if m < 4:
        answer = 0
    else:
        answer = solution()
    print(answer)
