# def search_min_set(dolls, K):
#     start, end = 0, -1
#     min_set_len = len(dolls)
#     count = 0 
#     while start < len(dolls) and end < len(dolls):
#         if count == K: 
#             min_set_len = min(min_set_len, end - start + 1)
        
#         if count < K: 
#             end += 1
#             if end == len(dolls): break 
#             if dolls[end] == 1: 
#                 count += 1
#         else: 
#             if dolls[start] == 1:
#                 count -= 1
#             start += 1
#     return min_set_len

def search_min_set(dolls, K): 
    start = 0 
    count = 0
    answer = len(dolls) 
    for end in range(len(dolls)): 
        if dolls[end] == 1: 
            count += 1
        while count >= K: 
            answer = min(answer, end - start + 1)
            if dolls[start] == 1: 
                count -= 1
            start += 1

    return answer

if __name__ == '__main__': 
    N, K = list(map(int, input().split()))
    dolls = list(map(int, input().split()))
    answer = search_min_set(dolls, K)
    if answer == N: print(-1)
    else: print(answer)