import sys 
input = sys.stdin.readline 

if __name__ == '__main__':
    S = input().split()[0]

    alphabet_list = []

    for index, Si in enumerate(S):
        num_Si = ord(Si) - 97
        if index == 0: 
            new_alphabet_list = [0 for _ in range(26)]
        else:
            new_alphabet_list = alphabet_list[-1].copy()

        new_alphabet_list[num_Si] += 1
        alphabet_list.append(new_alphabet_list)

    q = int(input())
    for _ in range(q):
        a, l, r = input().split()
        l, r = int(l), int(r)
        a_index = ord(a) - 97
        count = alphabet_list[r][a_index] - alphabet_list[l][a_index]
        if S[l] == a:
            count += 1
        print(count)