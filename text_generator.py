from random import random
def gen_word(mark, word):
    r = random()
    s = 0
    for next_word in mark[word]:
        if s <= r < s + mark[word][next_word]:
            return next_word
        s += mark[word][next_word]

def gen_text(mark, length):
    s = ""
    r = round(random()*len(mark['mark']))
    words = list(list(mark['mark'].keys())[r])
    key_size = mark['key_size']
    while len(words) < 1200 or not words[len(words) - 1] in '.!?':
        window = ''.join(words[len(words) - key_size: len(words)])
        new_words = gen_word(mark['mark'], window)
        for new_word in new_words:
            words.append(new_word)
    return "".join(words)
