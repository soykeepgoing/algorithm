def solution(nodes, depth):
    if len(nodes) == 1:
        trees[depth].append(nodes[0])
        return 
    
    half = len(nodes) // 2
    solution(nodes[0: half], depth + 1)
    trees[depth].append(nodes[half])
    solution(nodes[half + 1:], depth + 1)


if __name__ == '__main__':
    k = int(input())
    nodes = list(map(int, input().split()))
    trees = [[] for __ in range(k)]
    answer = solution(nodes, 0)
    for tree in trees:
        print(*tree)
