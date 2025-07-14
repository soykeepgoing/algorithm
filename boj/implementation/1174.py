'''
987
988

[9, 8, 8]

[9, 8, 0]
[9, 9, 0]

[32 , 1 ,0]

[43,2, 1]

'''


def get_new_num(num):
    num += 1
    num_list = list(map(int, str(num)))

    if len(num_list) >= 2:
        for index in range(len(num_list) - 1, 0, -1):
            if num_list[index] >= num_list[index - 1]:
                if index == len(num_list) - 1: # 마지막 인덱스
                    num_list[index] = 0 
                else:
                    num_list[index] = num_list[index + 1] + 1
                
                if num_list[index - 1] == 9: 
                    num_list[index - 1] = (num_list[index] + 2) * 10 + num_list[index] + 1
                else:
                    num_list[index - 1] += 1
    
    return int(''.join(map(str, num_list)))


if __name__ == '__main__':
    target_count = int(input())
    num = -1
    count = 0 

    while 1:
        num = get_new_num(num)
        count += 1
        
        # print(num)

        if num > 9876543210:
            print(-1)
            exit()

        if count == target_count:
            print(num)
            exit()