import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    T = int(input())
    N = 1000000
    
    yaksu_list = [0] * (N + 1)
    prefix_sum_list = [0] * (N + 1)

    for i in range(1, N + 1):
        j = 1
        while i * j <= N: # 곱이 최대값이 넘지 않을 때까지 
            yaksu_list[i * j] += i  # i의 배수에 무조건 i 값을 더해준다. 
            j += 1
        prefix_sum_list[i] = prefix_sum_list[i - 1] + yaksu_list[i] # 누적합에 약수의 값도 추가 
    
    for _ in range(T):
        n = int(input())
        print(prefix_sum_list[n])