if __name__ == '__main__':
    distance = int(input())
    if distance == 0: 
        print(0)
        exit()
    elif distance <= 5:
        print(1)
        exit()

    pi = -1
    pattern = [1, 0, 1, 2, 1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0]
    answer = 0

    cnt = 0
    while distance >= 5: 
        distance = distance - 5
        pi = pi + 1
        pi = pi % len(pattern)
        answer = pattern[pi]
        cnt += 1
    
    if distance > 0:
        if pattern[(pi + 1) % len(pattern)] > pattern[pi]:
            answer = pattern[(pi + 1) % len(pattern)]

    print(answer)