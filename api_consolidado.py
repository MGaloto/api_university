import requests
import unicodedata
from flask import Flask, json 
from pprint import pprint
import json


app = Flask(__name__)


'''
degree = {'Bachelor', 'Course', 'Master', 'Phd'}
page   = [0:64834]

'''

@app.route("/<degree>/<page>/")
def Study(degree, page):
    consolidado = json.load(open('Consolidado/consolidado_final.json', encoding='utf-8'))
    consolidado_page = [consolidado[i] for i in range(len(consolidado)) if consolidado[i]['DegreeType'] == str(degree)][int(page)]
    response = app.response_class(response = json.dumps(consolidado_page), status = 200, mimetype = "application/json")

    return response

app.run( port = 3000, host = "0.0.0.0" )








                
                
