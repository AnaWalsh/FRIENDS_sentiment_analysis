import string
import spacy
import en_core_web_sm
from nltk.corpus import stopwords
import re
from textblob import TextBlob
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def tokenizando(texto):
    """
    This function recieves a df and takes out from it the stopwords in english.
    It also eplaces the suffixes of the words to leave them at the root.
    Arggs: data frame
    Returns: string with the root of the given words.   
    """
    
    nlp = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words
    tokens = nlp(texto)
    filter = []
    for i in tokens:
        if not i.is_stop:
            lemma = i.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filter.append(lemma)
    return " ".join(filter)


def sentimental(col):
    """
    - para usar con dataframe
    recibe un string tokenizado
    devuelve una lista con su subjetividad, su polaridad según textblog
    también en la lista están incluidos los parámetros de sia(neg,neu,pos y compound)
    """
    

    total = []
    
    blob = TextBlob(col)
    total.append(blob.sentiment[0])
    total.append(blob.sentiment[1])
    
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(col)
    total.append(polaridad["neg"])
    total.append(polaridad["neu"])
    total.append(polaridad["pos"])
    total.append(polaridad["compound"])
    return total


