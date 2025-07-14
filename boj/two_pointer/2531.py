from collections import deque 

def get_count(current_nums, c):
    current_nums_set = set(current_nums)
    if c not in current_nums_set:
        return len(current_nums_set) + 1
    else:
        return len(current_nums_set)
    
if __name__ == '__main__':
    N, d, k, c = list(map(int, input().split()))
    nums = [] 
    for _ in range(N):
        nums.append(int(input()))
    
    current_nums = deque(nums[:k])
    count = get_count(current_nums, c)

    for end in range(k, k + N):
        end_index = end % N 
        
        current_nums.popleft()
        current_nums.append(nums[end_index])
        count = max(get_count(current_nums, c), count)

    print(count)