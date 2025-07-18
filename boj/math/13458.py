import math 

N = int(input())
aplies = list(map(int, input().split()))
b, c = list(map(int, input().split()))
answer = 0
answer += N

aplies = [a - b for a in aplies]

for a in aplies:
    if a > 0:
        answer += math.ceil(a / c)

print(answer)