if __name__ == '__main__':
    sub, add = list(map(int, input().split()))
    people = [add]

    for _ in range(3):
        sub, add = list(map(int, input().split()))
        last = people[-1]
        people.append(last - sub + add)
    
    print(max(people))