# W6-api-sentiment-project

![foto](url github)

## Objective

The objective of this project is to create an API which is able to receive data from clients (via their POST requests), store it, or serve information when needed (in response to their GET requests). 

## Working plan
- Clean dataset
- Obtain sample from datased
- API 
- get requests
- post requests
- NLTK

## The API

### Overview
Welcome to the Friends API! Using this service, you can get the characters in the TV series Friends, quotes for each character and quotes for a known character and episode. 

### Authentication
Currently there is no authentication required for accessing the Friends API. 

### How to start the API

 ```
URL = requests.get("http://127.0.0.1:5000/
```
- Expected response: Friends.


### Endpoints GET

1. /characters

This returns a json with the main characters of the TV series.

url = http://127.0.0.1:5000/characters

- Example response
 ```
 characters = requests.get("http://127.0.0.1:5000/characters").json()
```

2. /frases/

This returns quotes of a given character.

 ```
 character = Joey
 url = requests.get("http://127.0.0.1:5000/frases/Joey").json()
```

Example response:

 ```
 characters = requests.get("http://127.0.0.1:5000/frases/name").json()
```


URL : http://127.0.0.1:5000/frase/episode

Example response:

 ```
 characters = requests.get("http://127.0.0.1:5000/frases/Rachel Quits").json()
```




POST requests

URL: http://127.0.0.1:5000/frase/episode
/nuevafrase


URL: http://127.0.0.1:5000/borrarfrase
/borrarfrase


SENTIMENT  requests

URL: http://127.0.0.1:5000//sentimientos/character
/s




## Structure of the project files

**.1 Notebooks folder:** 
    - Clean_csv.ipynb 
    - API_PROJECT.ipynb 
    - API_Calls.ipynb 

**2. data:**
    - friends.csv 
    - firends 
    - friends_sample.csv 

**3. src:**
    - main_tools.py 
    - sql_tools.py 

**4. main.py:**
    


## Libraries




