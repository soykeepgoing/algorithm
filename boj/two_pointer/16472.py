# from collections import deque 
# import sys 
# INF = sys.maxsize 

# if __name__ == '__main__':
#     N = int(input())
#     words = list(input())
#     letters = [INF for _ in range(26)]
#     tmp_list = [] 
#     start_point = 0 
#     min_point = 0 
#     ans = -1
#     for i, word in enumerate(words):
#         word_index = ord(word) - 97

#         if word_index not in tmp_list and len(tmp_list) == N: 
#             ans = max(ans, i - start_point) # 길이 갱신
#             min_point = min(letters)
#             min_point_index = letters.index(min_point)
#             letters[min_point_index] = INF 
#             tmp_list.remove(min_point_index)
#             start_point = min_point + 1

#         letters[word_index] = i
#         if word_index not in tmp_list:
#             tmp_list.append(word_index)

#     if ans == -1: 
#         ans = len(words)

#     print(ans)        

from collections import deque 
import sys 
INF = sys.maxsize 

if __name__ == '__main__':
    N = int(input())
    words = list(input())
    letters = [INF for _ in range(26)]
    tmp_set = set() 
    start_point = 0 
    min_point = 0 
    ans = -1
    for i, word in enumerate(words):
        word_index = ord(word) - 97

        if word_index not in tmp_set and len(tmp_set) == N: 
            min_point = INF 
            min_point_index = -1 
            for idx in tmp_set:
                if letters[idx] < min_point:
                    min_point = letters[idx]
                    min_point_index = idx
            
            tmp_set.remove(min_point_index)
            start_point = min_point + 1
            letters[min_point_index] = INF 

        letters[word_index] = i
        tmp_set.add(word_index)
        ans = max(ans, i - start_point + 1)

    if ans == -1: 
        ans = len(words)

    print(ans)        
