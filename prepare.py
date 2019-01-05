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