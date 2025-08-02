'''
1차원 배열로 표현 

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 
*       1           *              *      3              x        *        2    *

1 => 위치 그대로 
2 => row + col + (row - 위치) = 10 + 5 + (10 - 8) = 17 
3 => row + 위치 그대로 
4 => row + col + row + (col - 위치) = 10 + 5 + 10 + (5 - 2) = 28 

모듈러 연산으로 순회하면서 구하기 

22 - 4 = 18
(4 - 22) % 30 = 

'''

def get_store_location(dir, loc):
    if dir == 1:
        return loc 
    elif dir == 2: 
        return r + c + (r - loc)
    elif dir == 3:
        return r + c + r + (c - loc)
    elif dir == 4:
        return r + loc 
        

def solution():
    answer = [] 
    # print(stores)
    for store in stores: 
        if store > my_position:
            min_distance = min((store - my_position), (my_position - store) % (2*r + 2 * c))
        else: 
            min_distance = min((my_position - store), (store - my_position) % (2*r + 2 * c))
        answer.append(min_distance)
    # print(answer)
    return sum(answer)

if __name__ == '__main__':
    r, c = list(map(int, input().split()))
    num = int(input())
    stores = []
    for __ in range(num):
        dir, loc = list(map(int, input().split()))
        stores.append(get_store_location(dir, loc))
    
    dir, x = list(map(int, input().split())) 
    my_position = get_store_location(dir, x)
    answer = solution()
    print(answer)
