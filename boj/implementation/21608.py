DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def search(classes, student_index, like_students, N):
    prefer = [] 

    for i in range(N):
        for j in range(N):
            if classes[i][j] == 0: # 비어있다면 
                count = 0; empty_count = 0
                for di, dj in DIRECTIONS:
                    i_new = i + di; j_new = j + dj
                    if i_new in range(N) and j_new in range(N):
                        if classes[i_new][j_new] in like_students: # 좋아하는 학생이 있다면 
                            count += 1
                        elif classes[i_new][j_new] == 0:
                            empty_count += 1

                prefer.append([count, empty_count,  i, j])

    prefer.sort(key = lambda x: [-x[0], -x[1], x[1], x[2]])
    new_i = prefer[0][2]; new_j = prefer[0][3]
    classes[new_i][new_j] = student_index

def count(classes, students, N):
    answer = 0
    for i in range(N):
        for j in range(N):
            student_index = classes[i][j]
            count = 0
            for di, dj in DIRECTIONS:
                i_new = i + di; j_new = j + dj
                if i_new in range(N) and j_new in range(N):
                    if classes[i_new][j_new] in students[student_index]:
                        count += 1
            if count == 0: answer += 0 
            elif count == 1: answer += 1
            elif count == 2: answer += 10 
            elif count == 3: answer += 100
            elif count == 4: answer += 1000
    return answer 

def main():
    N = int(input())
    classes = [[0] * N for _ in range(N)]
    students = [0] + [[] for _ in range(N**2)] 

    for _ in range(N**2):
        inputs = list(map(int, input().split()))
        student_index = inputs[0]; like_students = inputs[1:]
        search(classes, student_index, like_students, N)
        students[student_index] = like_students

    answer = count(classes, students, N)
    print(answer)


if __name__ == '__main__':
    main()