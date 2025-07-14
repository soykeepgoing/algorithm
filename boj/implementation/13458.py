N = int(input())
As = list(map(int, input().split()))
B, C = list(map(int, input().split()))

answer = 0
for A in As:
	answer += 1
	A = A - B 
	answer += A // C 
	if A % C > 0: 
		answer += 1

print(answer)
