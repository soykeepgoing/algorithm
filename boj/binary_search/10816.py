import sys 
input = sys.stdin.readline 

def get_upper(search_card, cards, start, end):
    while start < end: 
        mid = (start + end) // 2
        if search_card < cards[mid]: 
            end = mid 
        else:
            start = mid + 1
    return start

def get_lower(search_card, cards, start, end):
    while start < end: 
        mid = (start + end) // 2
        if search_card <= cards[mid]:
            end = mid
        else:
            start = mid + 1
    return start 

if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))
    cards.sort()

    M = int(input())
    search_cards = list(map(int, input().split()))
    
    ans = []

    for search_card in search_cards: 
        upper = get_upper(search_card, cards, start = 0, end = N)
        lower = get_lower(search_card, cards, start = 0, end = N)
        ans.append(upper - lower)

    print(*ans)