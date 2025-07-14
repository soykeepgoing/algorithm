import heapq

def get_sum(heap, w = 1):
    ans = 0 

    while heap:
        a = w * heapq.heappop(heap)
        if len(heap) == 0: 
            ans += a
            break 
        b = w * heapq.heappop(heap)

        if w == -1 and (a == (a * b)):
            ans += a
            heapq.heappush(heap, w * b)
        elif a > (a * b):
            ans += a
            heapq.heappush(heap, w * b)
        else: 
            ans += (a * b)
    return ans      

if __name__ == '__main__':
    N = int(input())
    min_heap = []
    max_heap = [] 
    for _ in range(N):
        num = int(input())
        if num > 0: # 양수라면 최대힙 
            heapq.heappush(max_heap, -1 * num)
        else: # 음수는 최소힙 
            heapq.heappush(min_heap, num)

    min_total = get_sum(min_heap, w = 1)
    max_total = get_sum(max_heap, w = -1)

    print(min_total + max_total)