if __name__ == '__main__': 
    N = int(input())
    arr = [i + 1 for i in range(N)]
    # print(arr)
    t = 1
    bi = 0 
    while 1: 
        if len(arr) == 1: 
            break 
        ti = (bi + (t ** 3 - 1)) % len(arr)
        bi = ti 
        arr.pop(ti)
        t += 1

    print(arr[0])