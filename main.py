from os import name
from flask import Flask, request, jsonify
import random
from sqlalchemy.sql.expression import text

import src.main_tools as mnt

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Friends"


@app.route("/characters")
def speakers():
    friends_characters = mnt.characters()
    return jsonify(friends_characters)

@app.route("/frases/<name>")
def quotes_names(name):
    frases = f"{name} says {mnt.quotes(name)[0]}"
    return jsonify(frases)

@app.route("/frase/<episode>")
def quotes_episode(episode):
    frases = f"In {episode} is this quote: {mnt.episodes(episode)}"
    return jsonify(frases)



@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    episodio = request.form.get("episode")
    personaje = request.form.get("character")
    frase = request.form.get("quote")
    return mnt.nuevomensaje(episodio, frase, personaje)


@app.route("/borrarfrase", methos=["POST"])
def borrar():
    return mnt.borrarmensaje(text)










app.run(debug=True)
