import requests
import unicodedata
from flask import Flask, json 
from pprint import pprint
import json


app = Flask(__name__)


@app.route("/study/<page>/")
def Study(page):
    consolidado = json.load(open('Consolidado/consolidado_final.json', encoding='utf-8'))
    consolidado_page = consolidado[int(page)]
    response = app.response_class(response = json.dumps(consolidado_page), status = 200, mimetype = "application/json")

    return response

app.run( port = 3000, host = "0.0.0.0" )




