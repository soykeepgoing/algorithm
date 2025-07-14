def search(N, Nlist, M, Mlist):
    Nlist = sorted(Nlist, reverse= True)
    Mlist = sorted(Mlist, reverse= True)

    if max(Nlist) < max(Mlist): 
        return -1 
    
    time = 0
    n, m = 0, 0
    visited = [False for _ in range(M)]
    while not all(visited): 
        while n < N and m < M:
            if m == M: break 
            if not visited[m] and Nlist[n] >= Mlist[m]:
                visited[m] = True 
                m += 1
                n += 1
            else: 
                m += 1
        time += 1
        n, m = 0, 0
    return time

if __name__ == '__main__':
    N = int(input())
    Nlist = list(map(int, input().split()))
    M = int(input())
    Mlist = list(map(int, input().split()))

    time = search(N, Nlist, M, Mlist)
    print(time)