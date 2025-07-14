
def solution(strings, idx):
    total = 0 
    while idx < len(strings):
        if strings[idx] in [')', ']']: # 닫는 괄호 
            return total if total > 0 else 1, idx 
        elif strings[idx] in ['(', '[']: # 여는 괄호 
            inner, new_idx = solution(strings, idx + 1) # 다음 문자열 순회하면서 찾기 
            if new_idx == len(strings) or new_idx == -1:
                return 0, len(strings)
            
            # 괄호 쌍이 올바른 경우 
            if strings[idx] == '(' and strings[new_idx] == ')':
                total += 2 * inner 
            elif strings[idx] == '[' and strings[new_idx] == ']': 
                total += 3 * inner
            else:
                return 0, -1
            idx = new_idx + 1 # 다음 인덱스부터 
        
    return total, idx


if __name__ == '__main__':
    strings = list(input())
    if len(strings) % 2 == 1: # 홀수라면 
        print(0)
    else: 
        num, final_idx = solution(strings, 0)
        if num == 1 or final_idx < len(strings) - 1: 
            print(0)
        else: 
            print(num)