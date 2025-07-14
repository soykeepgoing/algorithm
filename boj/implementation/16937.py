import sys 
input = sys.stdin.readline 

def is_in(R, C, H, W):
    if (R not in range(0, H + 1) or C not in range(0, W + 1)): 
        if (R not in range(0, W + 1) or C not in range(0, H + 1)):
            return False
    return True 

if __name__ == '__main__':
    H, W = list(map(int, input().split()))
    N = int(input())
    stickers = []
    for _ in range(N):
        R, C = list(map(int, input().split()))
        if is_in(R,C, H, W):
            sticker = [R, C]
            stickers.append(sticker)
    
    stickers.sort(key= lambda x: x[0] * x[1], reverse = True)
    # print(stickers)
    len_of_stickers = len(stickers)
    max_area = 0 
    for i in range(len_of_stickers):
        r1, c1 = stickers[i]       
        for j in range(i + 1, len_of_stickers, 1):
            r2, c2 = stickers[j]
            if (r1 + r2 <= H and max(c1, c2) <= W) or (c1 + c2 <= W and max(r1, r2) <= H):
                max_area = max(max_area, (r1 * c1 + r2 * c2))
            if (c1 + r2 <= H and max(r1, c2) <= W) or (r1 + c2 <= W and max(c1, r2) <= H):
                max_area = max(max_area, (r1 * c1 + r2 * c2))
            if (c1 + c2 <= H and max(r1, r2) <= W) or (r1 + r2 <= W and max(c1, c2) <= H):
                max_area = max(max_area, (r1 * c1 + r2 * c2))
            if (r1 + c2 <= H and max(r2, c1) <= W) or (r2 + c1 <= W and max(r1, c2) <= H):
                max_area = max(max_area, (r1 * c1 + r2 * c2))

    print(max_area)