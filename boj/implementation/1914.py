answer = [] 

def solution(num, start, sub, end):
    global answer
    if num == 1:
        answer.append([start, end])
        return 
    
    solution(num - 1, start, end, sub) # 마지막 제외 전부 start => sub으로 이동 
    answer.append([start, end]) # 마지막 num을 start => end로 이동
    solution(num - 1, sub, start, end) # sub => end로 이동 

if __name__ == '__main__':
    n = int(input())
    if n > 20:
        print(2 ** n - 1)
    else:
        solution(n, 1, 2, 3)
        print(len(answer))
        for ans in answer:
            print(*ans)
