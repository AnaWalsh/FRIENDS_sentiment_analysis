# W6-api-sentiment-project

![foto]guardo foto en github y aqui pongo la url entre ()

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
Welcome to the F.R.I.E.N.D.S API! Using this service, you can get the characters in the TV series Friends, quotes for each character and quotes for a known character and episode. 

### Authentication
Currently there is no authentication required for accessing the F.R.I.E.N.S. API.

### Rate Limiting
Currently the requests to the F.R.I.E.N.S. API are not limited. 

### Responses
All responses default to JSON format. 

### Endpoints

GET requests

http://127.0.0.1:5000/characters

http://127.0.0.1:5000/frases/name

http://127.0.0.1:5000/frase/episode




POST requests

http://127.0.0.1:5000/nuevafrase

http://127.0.0.1:5000/borrarfrase



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
**4. main.py:**

## Libraries


