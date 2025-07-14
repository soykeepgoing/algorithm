import sys 
input = sys.stdin.readline 
if __name__ == '__main__':
    r, c = list(map(int, input().split()))
    strings = []
    for _ in range(r):
        line = list(input())
        strings.append(line)

    result = 0 
    start, end = 0, r - 1
    
    while start <= end: 
        mid = (start + end)

        flag = False # 중복인가 아닌가
        dataset = set()

        for j in range(c):
            tmp = ''
            for i in range(mid, r):
                tmp += strings[i][j]
            if tmp not in dataset: 
                dataset.add(tmp)
            else:
                flag = True 
                break 
        
        if flag: # 중복이 있다면 
            end = mid - 1 # 
        else:
            result = mid 
            start = mid + 1

    print(result)