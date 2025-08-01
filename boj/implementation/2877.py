n = int(input())
ans = ''
while n > 0:
    m = n % 2 
    n = n // 2
    if m == 0:
        n -= 1
        ans = '7' + ans
    else:
        ans = '4' + ans

print(ans)
