def get_rest(trees, mid):
    rest = 0 
    for tree in trees: 
        if tree - mid > 0:
            rest += (tree - mid)
    return rest 

# def search(start, end, trees):
#     while start <= end: 
#         mid = (start + end) // 2
#         rest = get_rest(trees, mid)
#         if rest == M: 
#             return mid 
#         if rest > M: 
#             start = mid + 1
#         else:
#             end = mid - 1
#     return (start + end)//2

def search(start, end, trees):
    while start + 1 <  end: 
        mid = (start + end) // 2
        rest = get_rest(trees, mid)
        if rest >= M: 
            start = mid 
        else:
            end = mid 
    return start

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    trees = list(map(int, input().split()))
    start = 0; end = max(trees)

    ans = search(start, end, trees)
    print(ans)