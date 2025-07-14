if __name__ == '__main__':
    S = input()
    T = input()
    answer = 1
    
    check_T_list = [T]

    while check_T_list:
        new_check_T_list = [] 
        for T_tmp in check_T_list:
            if T_tmp == S:
                break 
            elif len(T_tmp) < 1 or (len(T_tmp) < len(S)) or (T_tmp[-1] not in ['A', 'B']): 
                answer = 0 
                break 
            elif T_tmp[-1] == 'A':
                new_check_T_list.append(T_tmp[:-1])
            elif T_tmp[-1] == 'B':
                new_T_tmp = T_tmp[:-1]
                new_check_T_list.append(new_T_tmp[::-1])
        # print(new_check_T_list)

        check_T_list = new_check_T_list[::]

    print(answer)