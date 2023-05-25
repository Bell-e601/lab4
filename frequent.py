def frequent_word(text):
    text = text.replace(',', '').replace('.','').replace('!', '').replace('?', '')
    words = text.split(' ')
    dict = {}
    for word in words:
        if word not in dict and word != '\n':
            dict[word] = 1
        else:
            dict[word] += 1
            
    
    return max(dict, key=dict.get)