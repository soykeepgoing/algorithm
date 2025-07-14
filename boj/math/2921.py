# if __name__ == '__main__':
N = int(input())
ans = 0
for i in range(0, N + 1, 1):
    for j in range(i, N + 1, 1):
        ans += (i + j)

print(ans)