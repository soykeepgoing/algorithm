from collections import deque 

def bfs(nodes, K):
    count = 0
    final_time = -1 
    visited = [0] * 100001

    while nodes:
        node, time = nodes.popleft()

        if node == K:
            if final_time == -1: 
                final_time = time 
                count = 1
            elif final_time == time:
                count += 1
            continue

        for next_node in (node + 1, node - 1, node * 2):
            if next_node in range(0, 100001):
                if visited[next_node] == 0 or visited[next_node] == time + 1:
                    visited[next_node] = time + 1
                    nodes.append((next_node, time + 1))
    
    return final_time, count

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    nodes = deque([[N, 0]])
    time, count = bfs(nodes, K)

    print(time)
    print(count)   