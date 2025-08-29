'''
XXXOO.XXX
XOXOXOXOX
OXOXOXOXO
XXOOOXXOX
XO.OX...X
.XXX.XOOO
X.OO..X..
OOXXXOOXO
end

0 1 2
3 4 5 
6 7 8
0 1 2 3 4 5 6 7 8 9
1. [0, 1, 2] [3, 4, 5], [6, 7, 8]
2. [0, 3, 6] [1, 4, 7], [2, 5, 8]
3. [0, 4, 8] [2, 4, 6]

X.X
.X.
X.X

.X.
X.X
OOO

OXO
XOX
OXX

XXX
OOO
X..


'''
def get_row_count(mark):
    count = 0
    for i in range(0, 9, 3):
        if line[i] == mark:
            flag = False 
            for j in [i + 1, i + 2]:
                if line[j] != mark:
                    flag = True 
                    break 
            if not flag:
                count += 1
    return count 

def get_col_count(mark):
    count = 0
    for i in range(0, 3):
        if line[i] == mark:
            flag = False 
            for j in [i + 3, i + 6]:
                if line[j] != mark:
                    flag = True 
                    break 
            if not flag:
                count += 1
    return count 

def get_diag_count(mark):
    count = 0
    if line[4] == mark:
        if line[0] == line[4] == line[8]:
            count += 1
        if line[2] == line[4] == line[6]:
            count += 1
    return count 

def solution():
    x_row_count = get_row_count('X')
    x_col_count = get_col_count('X')
    x_diag_count = get_diag_count('X')

    o_row_count = get_row_count('O')
    o_col_count = get_col_count('O')
    o_diag_count = get_diag_count('O')

    x_mark_count, o_mark_count = line.count('X'), line.count('O')

    if x_mark_count - o_mark_count >= 2:
        return 'invalid'

    if x_mark_count + o_mark_count == 9:
        if o_mark_count > x_mark_count: return 'invalid'

        if (x_row_count > 1 or x_col_count > 1) or (o_row_count > 1 or o_col_count > 1):
            return 'invalid' 
        elif (o_row_count + o_col_count + o_diag_count == 1): return 'invalid'
        else:
            return 'valid'
    else:
        if (x_row_count + x_col_count + x_diag_count == 1) and (o_row_count + o_col_count + o_diag_count == 1):
            return 'invalid'
        elif x_row_count + x_col_count + x_diag_count == 1 and x_mark_count > o_mark_count:
            return 'valid'
        elif o_row_count + o_col_count + o_diag_count == 1 and x_mark_count == o_mark_count:
            return 'valid'
        else:
            return 'invalid'
            

if __name__ == '__main__':
    while 1:
        line = input()
        if line == 'end':
            break 
        else:
            answer = solution()
            print(answer)
