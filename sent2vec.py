import gensim
from math import sqrt
from pymorphy2 import MorphAnalyzer
pymorphy2_analyzer = MorphAnalyzer()

def mod(vec):
    s = 0
    for coord in vec:
        s += coord ** 2;
    return sqrt(coord)

def normalize(vec):
    m = mod(vec)
    for i in range(len(vec)):
        vec[i] = vec[i] / m
    return vec

def add_tags(words):
    table = {
        "NOUN" : "NOUN", 
        "VERB" : "VERB", 
        "ADJF": "ADJ", 
        "ADVB": "ADV", 
        "NPRO": "PRON", 
        "PREP": "PREP", 
        "PRCL": "PART",
        "CONJ": "CCONJ"
    }
    for i in range(len(words)):
        an = pymorphy2_analyzer.parse(words[i])[0]
        if an.tag.POS in table:
            words[i] = an.normal_form + "_" + table[an.tag.POS]
        else:
            words[i] = ''
    return words

def sent2vec(words):
    words = add_tags(words)
    vec = model[words[0]].copy()
    for word in words[1:]:
        if word in model:
            current_vec = model[word]
            for i in range(len(vec)):
                vec[i] += current_vec[i]
    return normalize(vec)

m_path = 'ruscorpora_upos_skipgram_300_5_2018.vec.gz'
model = gensim.models.KeyedVectors.load_word2vec_format(m_path, binary=False)
model.init_sims(replace=True)
