from collections import deque 

def is_connected(from_node, to_node, computers):
    if from_node != to_node and computers[from_node][to_node] == 1:
        return True 
    else:
        return False 

def search(computers, queue, checked, n):
    while queue:
        from_node, to_node = queue.popleft()
        checked[to_node] = True
        for tmp_node in range(n):
            if is_connected(to_node, tmp_node, computers) and not checked[tmp_node]:
                    queue.append((to_node, tmp_node))
            
def solution(n, computers):
    answer = 0
    checked = [False for __ in range(n)]
    
    for from_node in range(n):
        queue = deque([])
        if not checked[from_node]:
            checked[from_node] = True 
            for to_node in range(n):
                if is_connected(from_node, to_node, computers) and not checked[to_node]:
                    queue.append((from_node, to_node))
            if queue:
                search(computers, queue, checked, n)
            answer += 1
        
    return answer