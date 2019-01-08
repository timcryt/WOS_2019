def gen_word(mark, word):
    r = random()
    s = 0
    for next_word in mark[word]:
        if s <= r < s + mark[word][next_word]:
            return next_word
        s += mark[word][next_word]

def gen_text(mark, length):
    s = ""
    r = round(random()*len(text))
    words = text[r:r+key_size]
    while len(words) < 1200 or not words[len(words) - 1] in '.!?':
        window = ''.join(words[len(words) - key_size: len(words)])
        new_words = gen_word(mark, window)
        for new_word in new_words:
            words.append(new_word)
    return ''.join(words)
    s = ''.join(words)
gen_text(mark, 1000)
