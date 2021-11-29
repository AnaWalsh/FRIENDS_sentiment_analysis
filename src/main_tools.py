from configuration.configuration import engine
import pandas as pd
from textblob import TextBlob

import string
import spacy
import en_core_web_sm
from nltk.corpus import stopwords
import re
from textblob import TextBlob
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


import re

def characters():
    query = list(engine.execute("SELECT distinct(AuthorName) FROM project_friends.Author;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista



def quotes(character):
    friends_character = list(engine.execute(f"SELECT idAuthor FROM project_friends.Author WHERE AuthorName = '{character}' ;"))[0][0]
    what = list(engine.execute(f"SELECT quote_ FROM Quote WHERE Author_idAuthor = '{friends_character}';"))
    return what

#return random.choice(what) 

def episodes (episodio):
    episode = list(engine.execute(f"SELECT idEpisodes from project_friends.Episodes WHERE EpTitle = '{episodio}'"))
    print(episode[0][0])
    what = list(engine.execute(f"SELECT quote_ FROM Quote WHERE Episodes_idEpisodes = '{episode[0][0]}';"))
    return what

#return random.choice(what)


def newcharacter(character):

    engine.execute(f"""
    INSERT INTO Author (AuthorName)
    VALUES ('{character}');
    """)
   

def nuevomensaje(episode, quote, character):

    engine.execute(f"""
    INSERT INTO Quote (Episodes_idEpisodes, Author_idAuthor, quote_)
    VALUES ({episode}, '{character}', '{quote}');
    """)
    
    return f"Se ha introducido correctamente: {episode} {quote} {character}"



def borrarmensaje(text):
    engine.execute(f"""
    SELECT quote_ from project_friends.Quote WHERE quote_ = '{text}'; """)

    engine.execute(f"""
    DELETE FROM project_friends.Quote where quote_ = '{text}'; """)

    return "The text has been deleted"



#SENTIMENT TOOLS


def analisis_sentimientos(AuthorName):
    query = f"""
    SELECT Quote.quote_
    FROM project_friends.Quote
    INNER JOIN project_friends.Author
    ON Author.idAuthor= Quote.Author_idAuthor
    WHERE AuthorName= '{AuthorName}'; 
    """
    data = pd.read_sql_query(query,engine)
     #quiero un df, por eso retiro el .json y el record
    return data

#tokenizar mi quote
def tokenizer(phrases):
    nlp = spacy.load("en_core_web_sm")
    tokens = nlp(phrases)
    filtradas = []
    for token in tokens: #saco las palabras importantes para el análisis de sentimientos
        if not token.is_stop:
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma): # Esto me quita las interrogaciones
                filtradas.append(lemma)
    return " ".join(filtradas)



def sentiment(phrases):
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(phrases)
    pol = polaridad["compound"]
    return pol




