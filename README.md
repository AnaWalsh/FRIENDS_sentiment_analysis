# W6-api-sentiment-project

![foto](https://github.com/AnaWalsh/W6-api-sentiment-project/blob/main/imagenes/foto.png)

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


### Endpoint GET

1. /characters

This returns a json with the main characters of the TV series.

```
url = requests.get("http://127.0.0.1:5000/characters").json()
```

-Expected response: json with the main characters.
'''
[
  {
    "nombre": "Monica"
  }, 
  {
    "nombre": "Joey"
  }, 
  {
    "nombre": "Chandler"
  }, 
  {
    "nombre": "Phoebe"
  }, 
  {
    "nombre": "Ross"
  }, 
  {
    "nombre": "Rachel"
  }
]
'''


2. /frases/

This returns quotes of a given character.

 ```
 character = Joey
 url = requests.get("http://127.0.0.1:5000/frases/Joey").json()
```

Example response: "Joey says ('You kissed my girlfriend!',"

3. /frase/
```
episode = Rachel Quits
```

```
url = requests.get("http://127.0.0.1:5000/frase/episode").json()
```

Example response: 

"In Rachel Quits is this quote: [('Oh, come here sweetie, listen, you\\x92re gonna go on like a thousand interviews before you get a job. (she glares at him) That\\x92s not how that was supposed to come out.',), ('Okay, and ah, this one here is a Douglas Fir, now it\\x92s a little more money, but you get a nicer smell.',), ('Gunther, Gunther, please, I\\x92ve worked here for two and a half years, I know the empty trays go over there. (points to the counter.)',), ('So, what happens to the old guys?',), ('(to the guy operating the chipper) Hey! Hey!! (makes the \\..."


### Endpoint POST

1. /nuevafrase

This endpoint creates a new quote for a given episode in the database. It receives the data from a dictionary. The quote needs to be inserted this way: 

```
insertar = {"episode" : 1, "character" : 1, "quote": "Hello"}

```
url_new_phrase = requests.post("http://127.0.0.1:5000/nuevafrase").json()
```

2. /borrafrase

```
url_new_phrase = requests.post("http://127.0.0.1:5000/borrafrase").json()
```

### Endpoint sentimental analysis

1. /sentimientos/

This endpoint makes a sentimental analysis, taking all the quotes for a specified character in the TV series. 

```
character = Phoebe

url = requests.post("http://127.0.0.1:5000/sentimientos/character").json()
```

Example response: 0.1752568306010929