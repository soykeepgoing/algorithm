

if __name__ == '__main__':
    N = int(input())
    count = 0 
    first_word = list(input())

    for _ in range(N-1):
        compare = first_word[:]
        word = input()
        cnt = 0 
        for w in word:
            if w in compare:
                compare.remove(w)
            else:
                cnt += 1
        
        if cnt < 2 and len(compare) < 2:
            count += 1
 
    
    print(count)

        
