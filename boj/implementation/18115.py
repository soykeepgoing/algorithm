if __name__ == '__main__': 
    N = int(input())
    A = list(map(int, input().split()))
    p1 = 0; p2 = N - 1
    
    cards = [-1 for _ in range(N)]
    card_num = N
    cnt = 0
    for i in range(N): 
        x = A[i]
        if x == 1: 
            cards[p1] = card_num
            p1 = p1 + cnt + 1
            cnt = 0
        elif x == 2: 
            cards[(p1 + cnt) + 1] = card_num 
            cnt += 1
        elif x == 3: 
            cards[p2] = card_num
            p2 -= 1

        card_num -= 1

    print(*cards)
