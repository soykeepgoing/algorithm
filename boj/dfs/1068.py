'''
-1
0 
1 1

-1 0 0 2 2 4 4 6 6 
'''

def get_count(tree, node, depth):
    ans = 0
    flag = False 

    if not tree[node]: 
        # print(node)
        return 1 # 리프 노드라면 
    
    for child_node_index in tree[node]:
        if child_node_index == erased_node_index: # 지워야 한다면 
            flag = True 
            continue
        ans += get_count(tree, child_node_index, depth + 1)

    if flag and len(tree[node]) == 1:
        ans = 1
    return ans 

def solution():

    tree = [[] for __ in range(n)]
    for node_index in range(n):
        if nodes[node_index] == -1:
            root_node = node_index
            continue 
        parent_node = nodes[node_index]
        tree[parent_node].append(node_index)
        
    # print(tree)
    if root_node == erased_node_index:
        return 0 
    
    answer = 0
    for child_node_index in tree[root_node]:
        # print(child_node_index)
        if child_node_index != erased_node_index:
            answer += get_count(tree, child_node_index, 0)
    if answer == 0: # 루트노드만 남은 경우 
        return 1
    return answer

    
if __name__ == '__main__':
    n = int(input())
    nodes = list(map(int, input().split()))
    erased_node_index = int(input())
    answer = solution()
    print(answer)
