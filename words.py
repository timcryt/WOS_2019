from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation 

def get_words_quanity(words_map):
	words_quanity = 0
	for i in words_map:
		words_quanity += words_map[i][1]
	return words_quanity

def get_words_map(words_list):
	words_map = {};
	for i in words_list:
		if not i in punctuation + '«»':
			if not words_map.get(i) is None:
				words_map[i][1] += 1
			else:
				words_map[i] = [len(i), 1]
	return words_map;

def get_words_len(words_map):
	words_len = 0
	for i in words_map:
		words_len += words_map[i][0] * words_map[i][1]
	return words_len
		
def get_sents_quanity(words_list):
	sents_quanity = 0
	for word in words_list:
		if word in ['.', '!', '?']:
			sents_quanity += 1	
	return sents_quanity

with open('sherlock.txt') as f:
	text = f.read()
text = text.lower()
words_list = word_tokenize(text)
words_map = get_words_map(words_list)
words_quanity = get_words_quanity(words_map)
words_len = get_words_len(words_map)
words_average_len = words_len / words_quanity
sents_quanity = get_sents_quanity(words_list)

print('Количество слов в тексте:', words_quanity)
print('Средняя длина слова в тексте:', words_average_len)
print('Ориентировочное количесво предложений в тексте:', sents_quanity)
