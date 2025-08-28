'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
==============
21
'''
other_side = {
    0: 5, 
    1: 3, 
    2: 4, 
    3: 1, 
    4: 2, 
    5: 0
}

def calculate(num):
    result = 0
    for i in range(n):
        for j in range(6):
            if dices[i][j] == num:
                other_num = dices[i][other_side[j]]
                if 6 in [num, other_num]:
                    if 5 in [num, other_num]:
                        result += 4 
                    else:
                        result += 5 
                else:
                    result += 6 
                num = other_num 
                break
    return result 
                
def solution():
    result = 0 
    for num in range(1, 7):
        result = max(result, calculate(num))
    return result

if __name__ == '__main__':
    n = int(input())
    dices = [list(map(int, input().split())) for __ in range(n)]
    answer = solution()
    print(answer)
