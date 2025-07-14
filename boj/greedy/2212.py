import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    locations = list(map(int, input().split()))
    locations.sort()

    distances = [] 
    for i in range(1, N):
        distances.append(locations[i] - locations[i - 1])
    distances.sort(reverse = True)
    ans = 0
    for i in range(K - 1, N - 1):
        ans += distances[i]
    print(ans)