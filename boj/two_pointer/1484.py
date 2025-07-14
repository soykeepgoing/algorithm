if __name__ == '__main__':
    G = int(input())
    y = 1 

    ans_list = [] 

    while 1: 
        tmp = G + y**2 
        root_tmp = tmp ** (1/2)

        if root_tmp == int(root_tmp):
            ans_list.append(int(root_tmp))
        
        if root_tmp ** 2 - (root_tmp - 1) ** 2 > 100000:
            break

        y += 1

    if not ans_list:
        print(-1)
    else:
        for ans in ans_list:
            print(ans)