from collections import deque 

def rotate(states, index, direction):
    current_state = states[index][::]
    # print(current_state)
    if direction == -1: # 반시계 방향이라면 
        new_state = current_state[1:] + [current_state[0]]
        states[index] = new_state[::]
    elif direction == 1: # 시계 방향이라면
        new_state = [current_state[-1]] + current_state[:-1]
        states[index] = new_state[::]

def get_queue(states, index, direction):
    queue = deque()
    queue.append((index, direction))
    
    # 왼쪽 확인
    d = direction
    for i in range(index - 1, -1, -1):
        # 기준은 i + 1의 왼쪽, i의 오른쪽
        if states[i][2] != states[i + 1][6]:
            d *= -1
            queue.appendleft((i, d))  # 앞에 추가
        else:
            break
    
    # 오른쪽 확인
    d = direction
    for i in range(index + 1, 4):
        # 기준은 i - 1의 오른쪽, i의 왼쪽
        if states[i - 1][2] != states[i][6]:
            d *= -1
            queue.append((i, d))
        else:
            break
    
    return queue


def get_new_state(states, index, direction, queue):
    while queue: 
        index, direction = queue.popleft()
        rotate(states, index, direction)

if __name__ == '__main__':
    states = [] 
    for _ in range(4):
        states.append(list(input()))

    N = int(input())
    queue = deque([])

    for _ in range(N):
        index, direction = list(map(int, input().split()))
        index -= 1
        queue = get_queue(states, index, direction)
        get_new_state(states, index, direction, queue)

    answer = 0 
    for i in range(4):
        # print(states[i])
        if states[i][0] == '1':
            if i == 0:
                answer += 1
            elif i == 1:
                answer += 2
            elif i == 2:
                answer += 4
            elif i == 3: 
                answer += 8
    
    print(answer)