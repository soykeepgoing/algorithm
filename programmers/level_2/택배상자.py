'''
보조컨테이너벨트는 스택 (LIFO)

1. 1부터 n까지 순회 
2. 순서가 아니라면 스택에 넣기 
3. 순서가 맞다면 스택에서 pop 또는 컨테이너에서 싣기
4. 순서가 맞는데 실을수없다면 종료 

3 5 4 1 2 

1 4 3 2 5
1 2 3 4 5 9 8 7 6 

1 2 3 4 5 6 7 8 9
'''
def solution(order):
    answer = 0
    side_belt = [] 
    o_index = 0
    container_belt = list(range(1, len(order) + 1))

    for box in container_belt:
        side_belt.append(box)
        while side_belt and side_belt[-1] == order[o_index]:
            side_belt.pop()
            answer += 1
            o_index += 1
          
    return answer
