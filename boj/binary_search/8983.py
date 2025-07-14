import sys 
input=  sys.stdin.readline 

def bin_search(a, b):
    global spot, M, N, L
    start, end = 0, M - 1
    left = a - (L - b)
    right = a + (L - b)

    while start <= end: 
        mid = (start + end) // 2
        spot = spots[mid]

        if left <= spot <= right:
            return 1 
        elif spot < left:
            start = mid + 1
        elif spot > right : 
            end = mid -1
    return 0

if __name__ == '__main__':
    M, N, L = list(map(int, input().split()))
    spots = list(map(int, input().split()))
    spots.sort()

    targets = [] 
    for _ in range(N):
        a, b = list(map(int, input().split()))
        targets.append((a, b))
 
    ans = 0
    for a, b in targets: 
        ans += bin_search(a, b)

    print(ans)