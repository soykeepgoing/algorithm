'''
유니온 파인드 

8 5
3 1 2 7
2 3 4
1 5
2 5 6
2 6 8
1 8

1. 각 파티 사람들의 부모노드 찾기 (사이클 지정)
- know_truth에 속한다면 pass 
- 아니라면 작은 값으로 

2. 파티에서 파티 사람들 순회할때 파티 사람들의 부모 노드가 진실을 아는 사람에 속한다면 break 

'''

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a in know_truth and b in know_truth:
        return 
    
    if a in know_truth:
        parent[b] = a
    elif b in know_truth:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b 

def set_parent_value(party):
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])

if __name__ == '__main__':
    n, m = map(int, input().split())
    know_truth = list(map(int, input().split()))[1:]

    parties = []
    parent = list(range(n+1))

    for __ in range(m):
        parties.append(list(map(int, input().split()))[1:])

    for party in parties:
        set_parent_value(party)
    
    # print(parent)

    answer = 0
    for party in parties:
        for people in party:
            if find(parent[people]) in know_truth:
                break 
        
        else:
            answer += 1
    
    print(answer)
