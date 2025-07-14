import sys 
input = sys.stdin.readline 

def get_installed(homes, distance):
    for index, value in enumerate(homes):
        if index == 0: 
            pre_value = value
            count = 1
        else: 
            if value - pre_value >= distance: 
                count += 1
                pre_value = value
    return count

def search(homes, C):
    start = 1 
    end = homes[-1] - homes[0] + 1
    ans = 1
    while start < end: 
        mid = (start + end) // 2
        tmp_installed_home = get_installed(homes, mid)
        if tmp_installed_home >= C: 
            ans = max(ans, mid)
            start = mid + 1
        elif tmp_installed_home < C: 
            end = mid
    return ans 

if __name__ == '__main__':
    N, C = list(map(int, input().split()))
    homes = []
    for _ in range(N):
        homes.append(int(input()))
    homes.sort()

    distance = search(homes, C)
    print(distance)

