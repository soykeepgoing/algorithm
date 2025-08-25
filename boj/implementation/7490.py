from collections import deque 

def compute_result(results):
    str_results = ''.join(results)
    str_results = str_results.replace(' ', '')
    answer = eval(str_results)
    if answer == 0:
        print(''.join(results))

def solution(results, now_num):
    global final_answer

    results.append(str(now_num))

    if now_num == num:
        compute_result(results)
        results.pop()
        return 

    # for compute_type in ['+', '-', ' ']:
    for compute_type in [' ', '+', '-']:
        results.append(compute_type)
        solution(results, now_num + 1)
        results.pop()
    results.pop()
    return

if __name__ == '__main__':
    N = int(input())
    for __ in range(N):
        num = int(input())
        final_answer = []
        solution([], 1)
        print()
