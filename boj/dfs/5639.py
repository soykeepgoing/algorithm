'''
노드의 수가 1만개 => N^2은 안됨 

전위 순회한 결과가 주어졌을 때, 후위 순회한 결과 
50 30 24 5 28 45 98 52 60 
=> 5 28 24 45 30 60 52 98 50 


루트 - 왼쪽 - 오른쪽 => 왼쪽 - 오른쪽 - 루트

dfs로 depth 판별

root = 50 

50보다 작은애들 

30 24 5 28 45 

root = 30 

30보다 작은애들 

24 5 28 

길이가 3이라면 5 28 24 출력 

30보다 큰애들 

45

길이가 3보다 작다면 45 출력 

root 출력 => 30 

50보다 큰 애들 

98 52 60 

50 

30 24 5 28 45 
98 52 60 

30 
24 5 28 
45 

반례

40 28 17 12 5 20 59 49 42 50 99 101

28 17 12 5 20 

17 12 5 
20


'''
import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10000)

def dfs(array):
    if len(array) == 1:
        print(array[0])

    if len(array) > 1:
        root = array[0]
        small_array, big_array = [], [] 
        for i in range(1, len(array)):
            if array[i] < root: 
                small_array.append(array[i])
            else:
                big_array.append(array[i])

        dfs(small_array)
        dfs(big_array)
        print(root)

if __name__ == '__main__':
    nums = [] 
    while True:
        try:  
            num = int(input())
            nums.append(num)
        except:
            break 
    
    dfs(nums)
