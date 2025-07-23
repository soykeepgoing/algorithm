import heapq
import sys 
input = sys.stdin.readline 

def solution(gems, bags):
    answer = 0
    rest_gems = []

    for bag_weight in bags:
        while gems and bag_weight >= gems[-1][0]: 
            gem_weight, gem_value = gems.pop()
            heapq.heappush(rest_gems, -gem_value)

        if rest_gems:
            value = heapq.heappop(rest_gems)
            answer += value 
    
    return -answer

if __name__ == '__main__':

    N, K = list(map(int, input().split()))
    gems = [list(map(int, input().split())) for __ in range(N)]
    bags = [int(input()) for __ in range(K)]
    bags.sort()
    gems.sort(key = lambda x: x[0], reverse = True) # weight 기준으로 내림차순
    answer = solution(gems, bags)
    print(answer)