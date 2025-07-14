import sys 
input = sys.stdin.readline 

def binary_search(x, blocks, l, r):
    while l < r:
        tmp = (blocks[l] + blocks[r]) 

        if tmp == x:
            return l, r
        elif tmp < x: 
            l += 1 
        elif tmp > x: 
            r -= 1
    
    return 'danger', False

if __name__ == '__main__':
    while 1:
        try:
            x = int(input())
            n = int(input())
            blocks = [] 
            for _ in range(n):
                blocks.append(int(input()))
            blocks.sort()

            l, r = binary_search(x * 10000000, blocks, l = 0, r = n - 1)

            if not r:
                print('danger')
            else:
                print('yes', blocks[l], blocks[r])

        except:
            break