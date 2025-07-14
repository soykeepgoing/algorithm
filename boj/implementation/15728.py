import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    share = list(map(int, input().split()))
    team = list(map(int, input().split()))

    for _ in range(K):
        tmp = -int(1e9)
        pop_index = -1
        for i in range(len(share)):
            for j in range(len(team)):
                if tmp <= share[i] * team[j]:
                    tmp = share[i] * team[j]
                    pop_index = j 
        team.pop(pop_index)
    
    ans = -int(1e9)
    for i in range(len(share)):
        for j in range(len(team)):
            ans = max(ans, share[i] * team[j])
    print(ans)