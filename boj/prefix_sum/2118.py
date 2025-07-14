if __name__ == '__main__':
    N = int(input())
    dists = [] 
    prefix_sums = [0] * (N + 1) # 누적합 
    for i in range(N):
        dists.append(int(input()))
        prefix_sums[i + 1] = prefix_sums[i] + dists[i] # 시계 방향 거리 누적합 

    total = prefix_sums[N] # 모든 지점 사이의 거리 합 
    ans = 0

    for i in range(1, N + 1):
        start, end = i, N
        while start <= end: 
            mid = (start + end) // 2
            length1 = prefix_sums[mid] - prefix_sums[i - 1]
            length2 = total - length1
            if length1 < length2:
                start = mid + 1
            else:
                end = mid - 1
            ans = max(ans, min(length1, length2))

    print(ans)