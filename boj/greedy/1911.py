'''

1 6 => 2
13 17 => 2
8 12 => 2

111222..333444555....
.mmmmm..mmmm.mmmm....
012345678901234567890

0부터 주어진 마지막 위치까지 순회 
널빤지를 두면 좋을지 아닐지 확인하기 
널빤지를 두면 좋겟다 => 현재 위치를 pos + 널빤지 길이로 바꾸기 
- 널빤지를 두는 조건 
1. 해당 지점을 기준으로 물 웅덩이가 존재한다면 무조건 두기?
-> 반례가 없을까? 

.111..222..333444555666
.m.m..mmm..m..mm.m..m
012345678901234567890

1. 출발점을 기준으로 소트 
2. 웅덩이에 있으면 추가하기 
3. pos 바꾸기 


'''
import sys 
import math
input = sys.stdin.readline 

def solution():
    index = 0  
    pos = locations[index][0]
    count = 0 
    while True: 
        if index == n: break 
        s, e = locations[index]

        if pos < s:
            pos = s
            continue 
        
        if pos >= e:
            index += 1
            continue 

        distance = e - pos 
        k = math.ceil(distance / l)
        count += k 
        pos += k * l

    return count 

if __name__ == '__main__':
    n, l = list(map(int, input().split()))
    locations = [] 
    for __ in range(n):
        locations.append(list(map(int, input().split())))
    
    locations.sort()
    answer = solution() 
    print(answer)
