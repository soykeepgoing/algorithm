'''
피사노 주기 
피보나치 수를 k로 나눈 나머지는 항상 주기를 가지게 된다. 
주기의 길이가 p라면 n번째 피보나치 수를 m으로 나눈 나머지는 n%p번째 피보나치 수를 m을 나눈 나머지와 같다.
m = 10^k일때 k>2라면 주기는 항상 15 * 10^(k-1)이다. 

'''

def solution():
    m = 1000000
    p = int(15 * (m / 10))

    dp = [0, 1]
    for i in range(2, p):
        num = dp[i - 2] + dp[i - 1]
        num = num % m 
        dp.append(num)

    return dp[n % p] 

if __name__ == '__main__':
    n = int(input())
    answer = solution()
    print(answer)
