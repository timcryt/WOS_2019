import json, os
from pymystem3 import Mystem
mystem_analyzer = Mystem()
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


from pymystem3 import Mystem
mystem_analyzer = Mystem()
from string import punctuation
from nltk.corpus import stopwords

def preprocessing(text):
    textarr = mystem_analyzer.analyze(text);
    preprocessed_text = ""
    for i in textarr:
        if not i.get('analysis') is None and len(i.get('analysis')) > 0:
            if not i.get('analysis')[0].get('lex') in stopwords.words('russian'):
                preprocessed_text += i.get('analysis')[0].get('lex').lower()
        else:
            preprocessed_text += i.get('text').lower()
    for sgn in punctuation:
        preprocessed_text = preprocessed_text.replace(sgn, '')
    return preprocessed_text


def get_docs():
	docs = {}
	for path in os.listdir():
		if os.path.isfile(path):
			try:
				with open(path, 'r', encoding="utf-8") as f:
					docs[path] = word_tokenize(preprocessing(f.read()))
			except:
				pass
	return docs

def inverted_index(docs):
	index_map = {}
	for doc in docs:
		words = docs[doc]
		for word in words:
			if index_map.get(word) is None:
				index_map[word] = {}
			if index_map[word].get(doc) is None:
				index_map[word][doc] = [1]
			else:
				index_map[word][doc][0] += 1
	for word in index_map:
		for doc in index_map[word]:
			index_map[word][doc].append(index_map[word][doc][0] / len(docs[doc]))
	return index_map

print(inverted_index(get_docs()))
