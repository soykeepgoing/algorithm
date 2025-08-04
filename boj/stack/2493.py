'''

N이 오십만

6 9 5 7 4

0 0 2 2 4

stack: 6 9 7

'''
import sys 
input = sys.stdin.readline 


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    stack = [] 
    answer = [] 
    for i in range(N):
        num = nums[i] 

        while stack: 
            index, value = stack[-1] 
            if value >= num:
                answer.append(index + 1)
                break 
            stack.pop()
        
        if not stack:
            answer.append(0)

        stack.append((i, num))
    
    print(*answer)
