from collections import deque 

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    orders = list(map(int, input().split()))

    students = {}
    photos = []

    for i, order in enumerate(orders): 
        if order not in students.keys():
            students[order] = [1, False, i] # 횟수, 현재 있는지, 시간
        else:
            students[order][0] += 1 

        if len(photos) < N:
            if order not in photos:
                photos.append(order)
                students[order][1] = True 
        else:
            if order not in photos:
                gone_sindex = -1
                for sindex in students.keys():
                    if students[sindex][1] == True: # 현재 사진틀에 있는 
                        if gone_sindex == -1: 
                            gone_sindex = sindex
                        else:
                            if students[sindex][0] < students[gone_sindex][0]: # 추천 받은 횟수가 더 작은 학생으로 바꾸기 
                                gone_sindex = sindex
                            elif (students[sindex][0] == students[gone_sindex][0]) and (students[sindex][2] < students[gone_sindex][2]): # 추천횟수는 같으나, 입력된 시간이 적은 경우 바꾸기
                                gone_sindex = sindex 

                del students[gone_sindex]
                students[order][1] = True 
                photos.remove(gone_sindex)
                photos.append(order)

        # print(photos)
    
    print(*sorted(photos))
                