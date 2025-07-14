def search(a, b): 
    len_a = len(a)
    len_b = len(b)
    answer = len_a + len_b

    for b_start in range(len_a):
        flag = True
        rest = 0
        for b_i in range(len_b): 
            a_i = b_start + b_i
            if a_i < len_a: 
                if a[a_i] == b[b_i] == '2': 
                    flag = False
                    continue 
            else: 
                rest += 1
        if flag: 
            answer = min(answer, len_a + rest)
    return answer
    

if __name__ == '__main__': 
    a = input()
    b = input()
    answer1 = search(a, b)
    answer2 = search(b,a)
    answer = min(answer1, answer2)
    print(answer)

