import sys 
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    scores = [] 
    for _ in range(N):
        scores.append(float(input()))
    scores.sort()
    
    first = K
    end = N - K
    scores_split = scores[first:end]
    sum_scores_split = (scores_split)

    julsa = sum_scores_split / ((end - first))
    bojung = (sum_scores_split + K * scores_split[0] + K * (scores_split[-1])) / (N)

    print('{:.2f}'.format(julsa + 1e-9))
    print('{:.2f}'.format(bojung+ 1e-9))
