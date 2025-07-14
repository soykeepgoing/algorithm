import heapq
if __name__ == '__main__':
    N = int(input())
    nums = [0 for _ in range(26)]
    words = [] 

    for _ in range(N):
        word = input()
        word_len = len(word)
        for i in range(word_len):
            order = ord(word[i]) - 65 
            num = 10 ** (word_len - 1 - i)
            nums[order] -= num
    
    heapq.heapify(nums)
    weight = 9
    result = 0 
    while nums: 
        num = heapq.heappop(nums)
        result += num * (-1) * weight 
        weight -= 1
    
    print(result)