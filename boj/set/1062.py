import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().split())
    word_list = [input().rstrip() for _ in range(N)]
    
    if K < 5:
        print(0)
        exit()

    base_letters = {'a', 'n', 't', 'i', 'c'}
    need_letters = []
    letter_set = set()

    for word in word_list:
        unique = set(word) - base_letters
        need_letters.append(unique)
        letter_set |= unique # 합집합 연산 

    if K - 5 >= len(letter_set):
        print(N)
        exit()

    answer = 0
    for comb in combinations(letter_set, K - 5):
        selected = set(comb)
        count = 0
        for word in need_letters:
            if word.issubset(selected): # 집합 연산 
                count += 1 
        answer = max(answer, count)

    print(answer)
