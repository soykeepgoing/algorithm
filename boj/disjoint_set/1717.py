import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**5)

def find(node):
    if parents[node] != node: # 루트 노드가 아니라면 
        parents[node] = find(parents[node])
    return parents[node]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    parents = [i for i in range(0, n + 1)]

    for _ in range(m):
        order, a, b = list(map(int, input().split()))

        a_root = find(a)
        b_root = find(b)
    
        if order == 0: # 합치는 연산 
            if a_root < b_root:
                parents[b_root] = a_root 
            else:
                parents[a_root] = b_root
        else:
            # 루트 노드 찾기 
            if a_root == b_root:
                print('YES')
            else:
                print('NO')