import sys
input = sys.stdin.readline 

if __name__ == '__main__':
    N, H = list(map(int, input().split()))
    
    up = [0] * (H + 1)
    down = [0] * (H + 1)

    for i in range(N): # 단순 카운팅 
        tmp = int(input())
        if i%2 == 0 :
            down[tmp] += 1
        else:
            up[tmp] += 1
    
    for i in range(H - 1, 0, -1): # 누적합 계산 
        up[i] += up[i + 1]
        down[i] += down[i + 1]
    
    min_value = 10e9 
    min_count = 0
    for i in range(1,H+1):
        tmp = up[H-i+1] + down[i]
        if min_value == tmp :
            min_count += 1
            continue
        if min_value > tmp :
            min_value = tmp
            min_count = 1
    
    print(min_value, min_count)
