# 구름 스퀘어 
# 그리디 
# 2025-07-14

def solution():
	stages = [0]

	for i in range(1, N):
		last_index = stages[-1]
		last_start, last_ending = times[last_index]
		start, ending = times[i]
		if last_ending <= start:
			stages.append(i)
		else:
			if last_ending > ending:
				stages.pop()
				stages.append(i)
	return len(stages)
	
if __name__ == '__main__':
	N = int(input())
	times = [] 
	for _ in range(N):
		s, e = list(map(int, input().split()))
		times.append([s, e + 1])
	times.sort(key = lambda x: [x[0], x[1]])
	answer = solution()
	print(answer)