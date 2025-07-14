import heapq 
import sys 
input = sys.stdin.readline 
TOP = 0 
VALUE = 1
def solve():
    max_heap = [] 
    min_heap = [] 

    for i in range(N):
        num = int(input())
        if len(min_heap) == len(max_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, (num, num))
        
        if min_heap and max_heap[TOP][VALUE] > min_heap[TOP][VALUE]:
            max_heap_top_value = heapq.heappop(max_heap)[VALUE]
            min_heap_top_value = heapq.heappop(min_heap)[VALUE]

            heapq.heappush(max_heap, (-min_heap_top_value, min_heap_top_value))
            heapq.heappush(min_heap, (max_heap_top_value, max_heap_top_value))

        print(max_heap[TOP][VALUE])

if __name__ == '__main__':
    N = int(input())
    solve()