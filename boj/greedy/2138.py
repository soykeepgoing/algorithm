'''

기본적으로 전구의 상태를 키고 끄면서 최적의 답을 찾기 

n개의 전구 스위치에 대해서 정답이 되기 위해서 몇 번 스위치를 키고 끄면 되는지 확인하면 됨 

단, 예외의 경우인 1번 스위치를 누르는 경우를 확인해야함. 

1번 스위치의 상태를 바꿀 수 있는 것은 두 가지 경우 밖에 없음 
    1. 1번 스위치 누르기   
    2. 2번 스위치 누르기 
이게 왜 중요한가?   
    1번 스위치를 누르면 2개만 바뀌지만 2번 스위치를 누르면 세 개가 바뀐다. 
    간단히 보면 전구에 영향을 주는 경우가 더 많다. 

'''

def turn_light(lights, index):
    if index > 0:
        lights[index - 1] = 0 if lights[index -1] == 1 else 1
    lights[index] = 0 if lights[index] == 1 else 1
    if index < n - 1:
        lights[index + 1] = 0 if lights[index + 1] == 1 else 1

def solution(press_first):
    global ans
    tmp_state = first_state[:]
    cnt = 0

    if press_first: 
        turn_light(tmp_state, 0)
        cnt += 1

    for index in range(1, n):
        if tmp_state[index - 1] != final_state[index - 1]:
            turn_light(tmp_state, index)
            cnt += 1
    
    return cnt if tmp_state == final_state else 10e9

if __name__ == '__main__':
    n = int(input())
    first_state = list(map(int, input()))
    final_state = list(map(int, input()))
    ans = min(
        solution(False),
        solution(True)
    )
    
    if ans == 10e9: print(-1)
    else: print(ans)
