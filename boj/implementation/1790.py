if __name__ == '__main__':
    N, k = map(int, input().split())

    answer = -1 
    now_num_len = 0

    start = 1; 
    end = N 

    while start <= end: 
        now_num_string = str(start)
        now_num_len += len(now_num_string)

        if now_num_len >= k: 
            tmp = now_num_len - len(now_num_string)
            answer = now_num_string[k - tmp - 1]
            break 
        start += 1

    print(answer)
