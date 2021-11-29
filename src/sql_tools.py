
import pandas as pd
import sqlalchemy as alch
from getpass import getpass
from configuration.configuration import engine


def check(que,string):
    """
    Parameterized function that checks in each table if the user, artist or song exists.
    Returns True if it exists and False if not.
    """
    if que == "author":
        query = list(engine.execute(f"SELECT AuthorName FROM Author WHERE AuthorName = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    if que == "episode_title":
        query = list(engine.execute(f"SELECT EpTitle FROM Episodes WHERE EpTitle = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    if que == "quote":
        query = list(engine.execute(f"SELECT quote_ FROM Quote WHERE quote_ = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False



def insertAuthor(lista):
    
    """
    Calls check function to check if the author exists
    Insert author if it does not exist
    """
    for i in lista:
        if check("authors", i):
            return "the author already exists"
        else:
            engine.execute(f"""INSERT INTO Author(AuthorName) VALUES ('{i}')"""); 


def check_numbers(que,integer):
    """
    Parameterised function that checks in if the SeasonNumber exists.
    Returns True if it exists and False if not.
    """
    if que == "season":
        query = list(engine.execute(f"SELECT SeasonNumber FROM Season WHERE SeasonNumber = {integer}"))
        if len(query) > 0:
            return True
        else:
            return False


def insertSeason(lista):
    """
    Calls check function to check if seasons exists
    Inserts SeasonNumber if it does not exist
    """
    for i in lista:
        if check_numbers("seasons", i):
            return "the seasons already exists"
        else:
            engine.execute(f"""INSERT INTO Season (SeasonNumber) VALUES ({i});""") 


def insertEpisode(df):
    """
    This functions receives a list and then calls to the check function defined above to check if the episode already exists in the database
    if not, it inserts the episode
    """
    for i,r in df.iterrows():
        if check("episode", r.episode_title):
            return "the episode already exists"
        else:
            engine.execute(f"INSERT INTO Episodes (EpTitle, Season_idSeason) VALUES ('{r.episode_title}', {r.season});")
            

def gimmeId(que,string):
    """
    Returns the ID of whatever we ask for knowing that the element exists.
    """
    if que == "author":
        return list(engine.execute(f"SELECT idAuthor FROM Author WHERE AuthorName ='{string}';"))[0][0]
    elif que == "episode_title":
        return list(engine.execute(f"SELECT idEpisodes FROM Episodes WHERE EpTitle ='{string}';"))[0][0]


def insertQuote(row):
    """
    Final function to insert the quotes 
    """
    if check("quote", row["quote"]):
        return "the quote already exists"
    else:
        if check("author", row["author"]):
            idAuthor = gimmeId("author", row["author"])
        else:
            insertAuthor(row["author"])
            idAuthor = gimmeId("author", row["author"])
        
        if check("episode_title", row["episode_title"]):
            idEpisodes = gimmeId("episode_title", row["episode_title"])
        else:
            insertEpisode(row["episode_title"])
            idEpisodes = gimmeId("episode_title", row["episode_title"])
            
        engine.execute(f"""
        INSERT INTO Quote (quote_, Author_IdAuthor, Episodes_idEpisodes) VALUES
        ("{row['quote']}", {idAuthor}, {idEpisodes});
        """)





    

