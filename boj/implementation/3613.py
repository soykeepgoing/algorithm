def is_valid(name): 
    if name[0] == '_':
        return False
    if name[-1] == '_':
        return False
    return True 

def split_into_word(name):
    
    if not is_valid(name):
        return 'Error!', None
    
    if '_' in name:
        tmp_words = name.split('_')
        if '' in tmp_words: 
            return 'Error!', None
        for tmp_word in tmp_words:
            for w in tmp_word:
                if w.isupper():
                    return 'Error!', None
        return 'C++', tmp_words
    if name[0].islower():
        pointers = []
        for i in range(len(name)):
            if name[i].isupper(): 
                pointers.append(i)
        
        tmp_words = [] 
        pre_pointer = 0 
        for pointer in pointers:
            tmp_words.append(name[pre_pointer: pointer])
            pre_pointer = pointer
        tmp_words.append(name[pre_pointer:])
        return 'java', tmp_words

    return 'Error!', None

if __name__ == '__main__':
    name = input()

    # 타입 구분 
    type, words = split_into_word(name)
    if not words: 
        print(type)
        exit()

    answer = words[0]
    if type == 'C++':
        for i in range(1, len(words)):
            new_word = words[i][0].capitalize() + words[i][1:]
            answer += new_word
    elif type == 'java':
        for i in range(1, len(words)):
            new_word = words[i][0].lower() + words[i][1:]
            answer += '_' + new_word
    
    print(answer)