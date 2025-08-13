'''
이분탐색 + 누적합 

1. 중앙값에 가까우면서 
2. 사람의 수가 많은 곳에 우체국을 세워야 좋음. 

1. x의 위치를 sort로 정렬 
2. 사람의 수를 누적합으로 정리 
3. 누적합으로 정리하면서 mid 값을 기준으로 더 큰 범위를 찾기 

7
1 2 3 4 5 6 7
9 8 2 9 8 10 9

-40 -30 -20 -10 -5 -4 -3 
9 8 2 9 8 10 9

'''


def solution():
    left, right = 0, n - 1
    answer = 10e9
    while left <= right:
        mid = (left + right) // 2
        left_people = prefix[mid]
        right_people = prefix[n - 1] - prefix[mid]
        if left_people >= right_people: # 누적 인구가 절반 이상이 되는 경우 : 즉 중앙값과 가장 유사할때 
            right = mid - 1 
            answer = min(answer, villages[mid][0])
        else:
            left = mid + 1
    return answer


if __name__ == '__main__':
    n = int(input())
    villages = [] 
    # people = 0 
    # for __ in range(n):
    #     x, a = list(map(int, input().split()))
    #     people += a
    #     villages.append((x, people))

    for __ in range(n):
        x, a = list(map(int, input().split()))
        villages.append((x, a))
    villages.sort(key = lambda x: x[0])
    # print(villages)

    prefix = [0 for __ in range(n)]
    prefix[0] = villages[0][1]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + villages[i][1]

    answer = solution()
    print(answer)           
