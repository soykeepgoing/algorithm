import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    M = int(input())
    A = [bin(0)]
    results = []

    sum_value = 0
    xor_value = 0

    for _ in range(M):
        order = input().split()
        if order[0] == '1':
            num = int(order[1])
            sum_value += num
            xor_value ^= num
        elif order[0] == '2':
            num = int(order[1])
            sum_value -= num 
            xor_value ^= num
        elif order[0] == '3':
            results.append(sum_value)
        elif order[0] == '4':
            results.append(xor_value)

    for r in results:
        print(r)

