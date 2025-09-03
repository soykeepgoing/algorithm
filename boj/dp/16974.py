'''

레벨-L
햄버거번 - L - 1 버거 - 패티 - L - 1버거 - 햄버거번 

N = 2  X = 7 

레벨 0 : P 
레벨 1 : B - P - P - P - B 
레벨 2 : B - BPPPB - P - BPPPB - B 
레벨 3 : B - BBPPPBPBPPPBB - P - BBPPPBPBPPPBB - B 

b[0] = 0 p[0] = 1
b[1] = 2 p[1] = 2 * p[0] + 1
b[2] = 1 + b[1] + b[1] + 1 p[2] = 2 * p[1] + 1
'''
def make_burger(n):
    bun, patty = [1], [1]
    for i in range(1, n + 1):
        bun.append(1 + bun[i - 1] + bun[i - 1] + 1 + 1)
        patty.append(2 * patty[i - 1] + 1)
    return bun, patty 

def get_answer(n, x):
    if n == 0: return x 
    if x == 1: return 0 
    elif (x <= 1 + bun[n - 1]): return get_answer(n - 1, x - 1)
    elif (x == 1 + bun[n - 1] + 1): return patty[n - 1] + 1
    elif (x <= 1 + bun[n - 1] + 1 + bun[n - 1]): return patty[n - 1] + 1 + get_answer(n - 1, x - (1 + bun[n - 1] + 1))
    else: return patty[n - 1] + 1 + patty[n - 1]

if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    bun, patty = make_burger(n)
    # print(bun, patty)
    answer = get_answer(n, x)
    print(answer)
