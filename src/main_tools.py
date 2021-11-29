from configuration.configuration import engine
import pandas as pd
from textblob import TextBlob

def characters():
    query = list(engine.execute("SELECT distinct(AuthorName) FROM project_friends.Author;"))
    lista =  [{"nombre": elemento[0]} for elemento in query]
    return lista



def quotes(character):
    friends_character = list(engine.execute(f"SELECT idAuthor FROM project_friends.Author WHERE AuthorName = '{character}' ;"))[0][0]
    what = list(engine.execute(f"SELECT quote_ FROM Quote WHERE Author_idAuthor = '{friends_character}';"))
    return what

 

def episodes (episodio):
    episode = list(engine.execute(f"SELECT idEpisodes from project_friends.Episodes WHERE EpTitle = '{episodio}'"))
    print(episode[0][0])
    what = list(engine.execute(f"SELECT quote_ FROM Quote WHERE Episodes_idEpisodes = '{episode[0][0]}';"))
    return what



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



