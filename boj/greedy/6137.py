def solution(): 
    left, right = 0, n - 1
    t_string_list = [] 

    while left <= right:
        if letters[left] < letters[right]:
            t_string_list.append(letters[left])
            left += 1
        elif letters[left] > letters[right]:
            t_string_list.append(letters[right])
            right -= 1
        else: 
            l, r = left, right 
            take_left = True 

            while l < r and letters[l] == letters[r]:
                l += 1
                r -= 1

            if l < r and letters[l] > letters[r]:
                take_left = False 
                
            if take_left: 
                t_string_list.append(letters[left])
                left += 1
            else: 
                t_string_list.append(letters[right])
                right -= 1

    return ''.join(t_string_list)
        
def print_answer(answer):
    for i in range(0, len(answer), 80):
        print(answer[i: i + 80])


if __name__ == '__main__':
    n = int(input())
    letters = [] 
    for __ in range(n):
        letters.append(input()) 
    
    answer = solution()
    print_answer(answer)
