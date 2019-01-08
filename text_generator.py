from random import random
from nltk import word_tokenize
from string import punctuation
def gen_word(mark, word):
    r = random()
    s = 0
    for next_word in mark['mark'][word]:
        if s <= r < s + mark['mark'][word][next_word]:
            return next_word
        s += mark['mark'][word][next_word]

def gen_text(mark, length):
    quantum_type = mark['quantum']
    s = ""
    r = int(random()*len(mark['mark']))
    if quantum_type == 'word':
        words = list(mark['mark'].keys())[r].split(' ')
    else:
        words = list(list(mark['mark'].keys())[r])    
    key_size = mark['key_size']
    while len(words) < length or not words[len(words) - 1] in '.!?':
        if quantum_type == 'word':
            window = ' '.join(words[len(words) - key_size: len(words)])
            new_words = gen_word(mark, window)
            for new_word in new_words.split(' '):
                words.append(new_word)
        else:
            window = ''.join(words[len(words) - key_size: len(words)])
            new_words = gen_word(mark, window)
            for new_word in new_words:
                words.append(new_word)
    if quantum_type == 'word':
        ret = ' '.join(words)
        for sgn in '.!?,;:)]}':
            ret = ret.replace(' ' + sgn, sgn)
        for sgn in '([{':
            ret = ret.replace(sgn + ' ', sgn)
        return ret
    return "".join(words)
