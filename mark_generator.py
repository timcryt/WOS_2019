def normalize(mark):
    for word in mark:
        s = 0
        for next_word in mark[word]:
            s += mark[word][next_word]
        for next_word in mark[word]:
            mark[word][next_word] = mark[word][next_word] / s
    return mark

def gen_mark(text, key_size, word_size):
    mark = {}
    for i in range(key_size, len(text) -  key_size + 1):
        word_gram = ''.join(text[i:i+word_size])
        key_gram = ''.join(text[i-key_size:i])
        if not key_gram in mark:
            mark[key_gram] = {}
        if not word_gram in mark[key_gram]:
            mark[key_gram][word_gram] = 0
        mark[key_gram][word_gram] += 1
    mark = normalize(mark)
    mark = {'key_size': key_size, 'word_size' : word_size, 'mark': mark}
    return mark

def gen_mark_from_file(file, key_size, word_size):
    t = file.read()
    text = list(t)
    mark = gen_mark(text, key_size, word_size)
    return mark

def gen_mark_from_str(string, key_size, word_size):
    text = list(t)
    mark = gen_mark(text, key_size, word_size)
    return mark
