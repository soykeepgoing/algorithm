import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    skills = list(map(int, input().split()))
    skills.sort()

    ans = 0 

    for i in range(N - 2): # 한 개의 수를 선택하므로 
        left, right = i + 1, N - 1
        target = skills[i] * (-1)
        max_index = N 
        while left < right: 
            tmp = skills[left] + skills[right]
            if tmp < target:
                left += 1
            elif tmp == target:
                if skills[left] == skills[right]:
                    ans += right - left 
                else:
                    if max_index > right: 
                        max_index = right 
                        while max_index >= 0 and skills[max_index - 1] == skills[right]:
                            max_index -= 1
                    ans += right - max_index + 1
                left += 1
            else:
                right -= 1
    
    print(ans)