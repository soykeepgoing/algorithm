'''
백트래킹 
임의의 길이의 인접한 두 개의 부분 수열이 동일 => 나쁜 수열 
1. 이전의 수랑 같은 수는 안되고 
2. 부분수열이 있는지 확인 
- 1번 인덱스부터 순회 
- 순회하면서 동일한 숫자가 나오면 길이만큼 slice해서 같은지 확인 
- 아니면 넘어가고 비교하는 숫자 유지 

12345678
32121323

0 1 2 3 

last_index = 4 
length = 1 
4 - 1 = 3 : 4 
4 - 2 = 2 : 3 

length  = 2
4 - 2 = 2: 4 
4 - 4 = 0: 2

'''

def check(given_array):
    last_index = len(given_array)
    for length in range(1, N // 2 + 1):
        part_array_1 = given_array[last_index - length:last_index]
        part_array_2 = given_array[last_index - 2 * length:last_index - length]
        
        if part_array_1 == part_array_2:
            return False
    return True 

def dfs(depth):
    if depth == N:
        print(''.join(map(str, array)))
        exit()
    
    for num in range(1, 4):
        if array[-1] == num:
            continue 
        if check(array + [num]):
            array.append(num)
            dfs(depth + 1)
            array.pop()

if __name__ == '__main__':
    N = int(input())
    for i in range(1, 4):
        array = [i]
        dfs(1)
