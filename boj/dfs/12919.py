def solution(t):
    if s == t:
        return 1 
    
    if len(s) >= len(t):
        return 0

    if t[-1] == 'A':
        if solution(t[:-1]):
            return 1 
    
    if t[0] == 'B':
        if solution(t[1:][::-1]):
            return 1 
    return 0

if __name__ == '__main__':
    s = list(input())
    t = list(input())
    ans = solution(t)
    print(ans)
