import sys 
input = sys.stdin.readline 

def find(node):
    global parents
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(a, b):
    global parents 
    a_root = find(a)
    b_root = find(b)

    if a_root < b_root:
        parents[b_root] = a_root 
    else:
        parents[a_root] = b_root 


if __name__ == '__main__': 
    n, m = list(map(int, input().split()))

    parents = [i for i in range(n + 1)]

    for _ in range(m):
        a, b = list(map(int, input().split()))
        union(a, b)

    times = list(map(int, input().split()))
    ans = 0 

    for i in range(1, n):
        lecture_root = find(times[i])
        pre_lecture_root = find(times[i - 1])

        if lecture_root != pre_lecture_root:
            ans += 1
    
    print(ans)