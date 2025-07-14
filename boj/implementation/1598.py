if __name__ == '__main__':
    A, B = list(map(int, input().split()))

    ax, ay = [1, 0]
    for i in range(A):
        ay += 1
        if ay == 5:
            ay = 1
            ax += 1
        # print(i, ax, ay)
    
    bx, by = [1, 0]
    for i in range(B):
        by += 1
        if by == 5:
            by = 1
            bx += 1
    #     print(i, bx, by)
    # print(ax, ay, bx, by)
    ans = abs(by - ay) + abs(bx - ax)
    print(ans)