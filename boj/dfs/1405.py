direction_list = ['E', 'W', 'N', 'S']

moves = {
    'E': (0, 1), 
    'W': (0, -1), 
    'N': (-1, 0), 
    'S': (1, 0)
}

def to_percent(num):
    return num * 0.01

def solution(pos, visited, turn, possibility):
    # turn이 N보다 크다면 종료 
    if turn > N:
        return possibility    

    total_possibility = 0
    for index, direction in enumerate(direction_list):
        new_pos = ( pos[0] + moves[direction][0], pos[1] + moves[direction][1])
        new_possibility = possibilities[index]
        if new_pos not in visited and new_possibility > 0.0: 
            visited.add(new_pos)
            total_possibility += solution(new_pos, visited, turn + 1, possibility * new_possibility)
            visited.remove(new_pos)
    return total_possibility

if __name__ == '__main__':
    inputs = list(map(int, input().split()))
    N = inputs[0]
    possibilities = list(map(to_percent, inputs[1:]))
    visited = set()
    pos = (0, 0)
    answer = solution(pos, visited, turn = 0, possibility = 1)
    print(answer)