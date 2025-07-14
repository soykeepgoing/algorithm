import sys 
input = sys.stdin.readline 

def search(fruits): 
    start = 0 
    fruit_count = {}
    max_length = 0 

    for end in range(len(fruits)):
        fruit = fruits[end]

        if fruit in  fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1

        if len(fruit_count) > 2: 
            fruit_count[fruits[start]] -= 1
            if fruit_count[fruits[start]] == 0: 
                del fruit_count[fruits[start]]
            start += 1

        max_length = max(max_length, end - start + 1)
    return max_length


if __name__ == '__main__': 
    N = int(input())
    fruits = list(map(int, input().split()))
    answer = search(fruits)
    print(answer)