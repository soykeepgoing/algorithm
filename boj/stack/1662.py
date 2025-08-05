'''

1. 문자열 앞에서 부터 순회
2. 괄호가 있으면 다른 방식으로 스택에 저장 
3. 이후 스택을 뒤에서 부터 팝하면서 전체 길이 확인 


33(562(71(9)))
[[0, 1], [1, 3], [0, 2], [1, 2], [0, 1], [1, 1], [0, 1]]

1 * 1 + 1 

반례 

3(5)
3

3(5)1
4

3(5(1))
15

3(5(1))1
16

4(3(5(1)))
60

4(3(5(1)))1
61

15(22)13(92(1111)42(222))
60

15(22)13(92(1111)42(222))123(1)45
67

15(22)13(92(1111)42(222))
60

'''
import sys 

if __name__ == '__main__':
    string = input()
    stack = [] 
    cnt = 0
    for i in range(len(string)):
        c = string[i]
        if c == '(':
            stack[-1] -= 1
            stack.append(int(string[i - 1]))
            stack.append('(')
            cnt = 0
        elif c == ')':
            tmp = 0 
            while stack:
                val = stack.pop() 
                if val == '(':
                    k = stack.pop() 
                    stack.append(k * tmp)
                    break 
                else: 
                    tmp += val
        else:
            if not stack or stack[-1] == '(':
                stack.append(1)
            else:
                stack[-1] += 1
            cnt += 1
    
    # print(stack)
    print(sum(stack))
