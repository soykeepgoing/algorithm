import sys 
input = sys.stdin.readline 

def get_count(tables, M):
    count = 0
    for table in tables: 
        count += ( M // table)
    return count 

def search(tables, N,  M):
    start = tables[0]
    end = tables[-1] * M + 1
    ans = end
    while start < end: 
        mid = (start + end) // 2
        count = get_count(tables, mid)
        if count >= M: 
            ans = min(mid, ans)
            end = mid
        else:
            start = mid + 1
    return end 

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    tables = [] 
    for _ in range(N):
        tables.append(int(input()))
    tables.sort()
    time = search(tables, N, M)
    print(time)