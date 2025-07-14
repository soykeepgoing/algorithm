if __name__ == '__main__':
    L, R = input().split()

    if len(L) != len(R): 
        count = 0
    else:
        count = 0 
        i = 0 
        while i < len(R):
            if L[i] != R[i]:
                break 
            else:
                if L[i] == '8':
                    count += 1
            i += 1
    
    print(count)