import sys 
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
    input_string = list(input())
    target_string = list(input())
    len_target_string = len(target_string)

    answer = []
    for letter in input_string:
        answer.append(letter)
        # print(answer[len(answer) - len_target_string: len(answer)], target_string)
        if answer[len(answer) - len_target_string: len(answer)] == target_string:
            for _ in range(len_target_string):
                answer.pop() 
    
    if answer:
        print(*answer, sep = '')
    else:
        print('FRULA')