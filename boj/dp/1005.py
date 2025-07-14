import sys 
input = sys.stdin.readline 

def search(child_nodes, parents_nodes):
    global times, parents, childs, dp  # res 제거

    if dp[child_nodes[0]] != -1:
            return dp[child_nodes[0]]

    if len(parents_nodes) == 0:
        dp[child_nodes[0]] = times[child_nodes[0]]
        return times[child_nodes[0]]

    max_time = 0

    for p_node in parents_nodes:
        new_p_node = parents[p_node]
        if dp[p_node] == -1:
             dp[p_node] = search([p_node], new_p_node) # 부모 노드 먼저 계산
        max_time = max(max_time, dp[p_node]) # 최대값 갱신
    dp[child_nodes[0]] = max_time + times[child_nodes[0]] # 자식 노드의 건설시간 추가: 게산 후 반드시 dp에 값 저장  
    return dp[child_nodes[0]]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split()))
        times = list(map(int, input().split()))
        childs = [[] for _ in range(N)]
        parents = [[] for _ in range(N)]
        dp = [-1 for _ in range(N)]
        for _ in range(K):
            p, c = list(map(int, input().split()))
            childs[p - 1].append(c - 1)
            parents[c - 1].append(p - 1)

        W = int(input()) - 1
        p_nodes = parents[W]
        res = search([W], p_nodes)
        print(res)