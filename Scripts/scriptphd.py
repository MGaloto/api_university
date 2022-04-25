
import requests
import json
import re
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup as BS
from lxml import etree, html
import time
import math




def getModality(data):
    lista_modalidad = data
    partime = lista_modalidad['parttime']
    fulltime = lista_modalidad['fulltime']
    if partime == False and fulltime == True:
        resultado = 'fulltime'
    elif partime == True and fulltime == False:
        resultado = 'parttime'
    else:
        resultado = 'fulltime and partime'
    return resultado


def getMethods(data):
    lista_metodos = data
    face2face = lista_metodos['face2face']
    online    = lista_metodos['online']
    if face2face == False and online == True:
        resultado = 'online'
    elif face2face == True and online == False:
        resultado = 'face2face'
    else:
        resultado = 'blendede'
        return 
    return resultado



def getDurationFull(data):
    try:
        
        valor = data['fulltime_duration']['value']
        unidad = data['fulltime_duration']['unit']
        total = str(valor) + ' ' + unidad
        return total
    except:
        return None
    
def getDurationParcial(data):
    try:
        
        valor = data['parttime_duration']['value']
        unidad = data['parttime_duration']['unit']
        total = str(valor) + ' ' + unidad
        return total
    except:
        return None
    
def getMatricula(data):
    try:
        matricula = data["tuition_fee"]["value"]
        return matricula
    except:
        return None

    
def getMatriculaUnit(data):
    try:
        unidad = data["tuition_fee"]["unit"]
        return unidad
    except:
        return None
    
def getMatriculaCoin(data):
    try:
        moneda = data["tuition_fee"]["currency"]
        return moneda
    except:
        return None



def getLogo(data):
    try:
        if data[i]["logo"]:
            return data[i]["logo"]
        elif data[i]["squared_logo"]:
            return data[i]["logo"]
    except:
        return 
    
    
def getOrg(data):
    try:
        org = data["organisation"]
        return org
    except:
        return None
        

def getArea(data):
    try:
        area = data['area']
        return area
    except:
        return None            



diccionario_cero = []

start = 0

longitud_max = 9900

iterations = int(9900 / 100)

nombres =  []


for i in range(iterations):
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    start +=100
    sleep(1)
    if len(data) == 0:
        continue
    else:
        for i in range(len(data)):
            ids = data[i]["title"] + ' - ' + str(data[i]["id"])
            print('Clave: ',ids)
            nombres.append(ids)
            diccero = {                
                'Titulo'   : data[i]["title"],
                'Link'     : 'https://www.phdportal.com/studies/' +  str(data[i]["id"]),
                'Ciudad'   : data[i]["venues"][0]['city'],
                'Pais'     : data[i]["venues"][0]['country'],
                'Area'     : getArea(data[i]["venues"][0]),   
                'Universidad'   : getOrg(data[i]), 
                'Calificacion' : data[i]["degree"],
                'Modalidad' : getModality(data[i]["density"]),
                'Cursada'    : getMethods(data[i]["methods"]),
                'Duracion Parcial'   : getDurationParcial(data[i]),
                'Duracion Full'    : getDurationFull(data[i]),
                'Descripcion' : data[i]["summary"],
                'Nivel'      : data[i]["level"],
                'Sub Nivel'      : data[i]["degree"],
                'Logo'       : getLogo(data),
                'Matricula'  : getMatricula(data[i]),
                'Unidad Matricula' : getMatriculaUnit(data[i]),
                'Moneda Matricula' : getMatriculaCoin(data[i])
            }
            
            diccionario_cero.append(diccero)





'''
CORRER A PARTIR DE AQUI

'''


diccionario = []

names = []

start = 100

longitud_max = 9900

iterations = int(9900 / 100)


number = 0






for i in range(iterations):
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
        break
    else:
        if len(data) == 0:
            continue
        else:
            for i in range(len(data)):
                ides = data[i]["title"] + ' - ' + str(data[i]["id"])
                #print('Clave: ',ides)
                names.append(ides)
                diccuno = {                
                    'Titulo'   : data[i]["title"],
                    'Link'     : 'https://www.phdportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : data[i]["venues"][0]['city'],
                    'Pais'     : data[i]["venues"][0]['country'],
                    'Area'     : getArea(data[i]["venues"][0]),   
                    'Universidad'   : getOrg(data[i]), 
                    'Calificacion' : data[i]["degree"],
                    'Modalidad' : getModality(data[i]["density"]),
                    'Cursada'    : getMethods(data[i]["methods"]),
                    'Duracion Parcial'   : getDurationParcial(data[i]),
                    'Duracion Full'    : getDurationFull(data[i]),
                    'Descripcion' : data[i]["summary"],
                    'Nivel'      : data[i]["level"],
                    'Sub Nivel'      : data[i]["degree"],
                    'Logo'       : getLogo(data),
                    'Matricula'  : getMatricula(data[i]),
                    'Unidad Matricula' : getMatriculaUnit(data[i]),
                    'Moneda Matricula' : getMatriculaCoin(data[i])
                }
                
                diccionario.append(diccuno)
    
                
            start = 0
            for i in range(iterations):
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
                    break
                else:
                    start += 100
                    if len(data) == 0:
                        continue
                    else:
                        for i in range(len(datados)):
                            ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                            #print('Clave: ',ids)
                            names.append(ids)
                            
                            diccdos = {                
                                'Titulo'   : datados[i]["title"],
                                'Link'     : 'https://www.phdportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : datados[i]["venues"][0]['city'],
                                'Pais'     : datados[i]["venues"][0]['country'],
                                'Area'     : getArea(datados[i]["venues"][0]),   
                                'Universidad'   : getOrg(datados[i]), 
                                'Calificacion' : datados[i]["degree"],
                                'Modalidad' : getModality(datados[i]["density"]),
                                'Cursada'    : getMethods(datados[i]["methods"]),
                                'Duracion Parcial'   : getDurationParcial(datados[i]),
                                'Duracion Full'    : getDurationFull(datados[i]),
                                'Descripcion' : datados[i]["summary"],
                                'Nivel'      : datados[i]["level"],
                                'Sub Nivel'      : datados[i]["degree"],
                                'Logo'       : getLogo(data),
                                'Matricula'  : getMatricula(datados[i]),
                                'Unidad Matricula' : getMatriculaUnit(datados[i]),
                                'Moneda Matricula' : getMatriculaCoin(datados[i])
                            }
                            diccionario.append(diccdos)
            start = 0
                        
                    
                    

diccionario_dos = []

names = []

start = 100

longitud_max = 9900

iterations = int(9900 / 100)


number = 0






for i in range(iterations):
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 85) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
        break
    else:
        if len(data) == 0:
            continue
        else:
            for i in range(len(data)):
                ides = data[i]["title"] + ' - ' + str(data[i]["id"])
                #print('Clave: ',ides)
                names.append(ides)
                diccuno = {                
                    'Titulo'   : data[i]["title"],
                    'Link'     : 'https://www.phdportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : data[i]["venues"][0]['city'],
                    'Pais'     : data[i]["venues"][0]['country'],
                    'Area'     : getArea(data[i]["venues"][0]),   
                    'Universidad'   : getOrg(data[i]), 
                    'Calificacion' : data[i]["degree"],
                    'Modalidad' : getModality(data[i]["density"]),
                    'Cursada'    : getMethods(data[i]["methods"]),
                    'Duracion Parcial'   : getDurationParcial(data[i]),
                    'Duracion Full'    : getDurationFull(data[i]),
                    'Descripcion' : data[i]["summary"],
                    'Nivel'      : data[i]["level"],
                    'Sub Nivel'      : data[i]["degree"],
                    'Logo'       : getLogo(data),
                    'Matricula'  : getMatricula(data[i]),
                    'Unidad Matricula' : getMatriculaUnit(data[i]),
                    'Moneda Matricula' : getMatriculaCoin(data[i])
                }
                
                diccionario_dos.append(diccuno)
    
                
            start = 0
            for i in range(iterations):
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 85) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
                    break
                else:
                    start += 100
                    if len(data) == 0:
                        continue
                    else:
                        for i in range(len(datados)):
                            ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                            #print('Clave: ',ids)
                            names.append(ids)
                            
                            diccdos = {                
                                'Titulo'   : datados[i]["title"],
                                'Link'     : 'https://www.phdportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : datados[i]["venues"][0]['city'],
                                'Pais'     : datados[i]["venues"][0]['country'],
                                'Area'     : getArea(datados[i]["venues"][0]),   
                                'Universidad'   : getOrg(datados[i]), 
                                'Calificacion' : datados[i]["degree"],
                                'Modalidad' : getModality(datados[i]["density"]),
                                'Cursada'    : getMethods(datados[i]["methods"]),
                                'Duracion Parcial'   : getDurationParcial(datados[i]),
                                'Duracion Full'    : getDurationFull(datados[i]),
                                'Descripcion' : datados[i]["summary"],
                                'Nivel'      : datados[i]["level"],
                                'Sub Nivel'      : datados[i]["degree"],
                                'Logo'       : getLogo(data),
                                'Matricula'  : getMatricula(datados[i]),
                                'Unidad Matricula' : getMatriculaUnit(datados[i]),
                                'Moneda Matricula' : getMatriculaCoin(datados[i])
                            }
                            diccionario_dos.append(diccdos)
            start = 0




diccionario_tres = []

names = []

start = 100

longitud_max = 9900

iterations = int(9900 / 100)


number = 0


for i in range(iterations):
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 183) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
        break
    else:
        if len(data) == 0:
            continue
        else:
            for i in range(len(data)):
                ides = data[i]["title"] + ' - ' + str(data[i]["id"])
                #print('Clave: ',ides)
                names.append(ides)
                diccuno = {                
                    'Titulo'   : data[i]["title"],
                    'Link'     : 'https://www.phdportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : data[i]["venues"][0]['city'],
                    'Pais'     : data[i]["venues"][0]['country'],
                    'Area'     : getArea(data[i]["venues"][0]),   
                    'Universidad'   : getOrg(data[i]), 
                    'Calificacion' : data[i]["degree"],
                    'Modalidad' : getModality(data[i]["density"]),
                    'Cursada'    : getMethods(data[i]["methods"]),
                    'Duracion Parcial'   : getDurationParcial(data[i]),
                    'Duracion Full'    : getDurationFull(data[i]),
                    'Descripcion' : data[i]["summary"],
                    'Nivel'      : data[i]["level"],
                    'Sub Nivel'      : data[i]["degree"],
                    'Logo'       : getLogo(data),
                    'Matricula'  : getMatricula(data[i]),
                    'Unidad Matricula' : getMatriculaUnit(data[i]),
                    'Moneda Matricula' : getMatriculaCoin(data[i])
                }
                
                diccionario_tres.append(diccuno)
    
                
            start = 0
            for i in range(iterations):
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 183) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
                    break
                else:
                    start += 100
                    if len(data) == 0:
                        continue
                    else:
                        for i in range(len(datados)):
                            ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                            #print('Clave: ',ids)
                            names.append(ids)
                            
                            diccdos = {                
                                'Titulo'   : datados[i]["title"],
                                'Link'     : 'https://www.phdportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : datados[i]["venues"][0]['city'],
                                'Pais'     : datados[i]["venues"][0]['country'],
                                'Area'     : getArea(datados[i]["venues"][0]),   
                                'Universidad'   : getOrg(datados[i]), 
                                'Calificacion' : datados[i]["degree"],
                                'Modalidad' : getModality(datados[i]["density"]),
                                'Cursada'    : getMethods(datados[i]["methods"]),
                                'Duracion Parcial'   : getDurationParcial(datados[i]),
                                'Duracion Full'    : getDurationFull(datados[i]),
                                'Descripcion' : datados[i]["summary"],
                                'Nivel'      : datados[i]["level"],
                                'Sub Nivel'      : datados[i]["degree"],
                                'Logo'       : getLogo(data),
                                'Matricula'  : getMatricula(datados[i]),
                                'Unidad Matricula' : getMatriculaUnit(datados[i]),
                                'Moneda Matricula' : getMatriculaCoin(datados[i])
                            }
                            diccionario_tres.append(diccdos)
            start = 0




diccionario_cuatro = []

names = []

start = 100

longitud_max = 9900

iterations = int(9900 / 100)


number = 0


for i in range(iterations):
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 280) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
        break
    else:
        if len(data) == 0:
            continue
        else:
            for i in range(len(data)):
                ides = data[i]["title"] + ' - ' + str(data[i]["id"])
                #print('Clave: ',ides)
                names.append(ides)
                diccuno = {                
                    'Titulo'   : data[i]["title"],
                    'Link'     : 'https://www.phdportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : data[i]["venues"][0]['city'],
                    'Pais'     : data[i]["venues"][0]['country'],
                    'Area'     : getArea(data[i]["venues"][0]),   
                    'Universidad'   : getOrg(data[i]), 
                    'Calificacion' : data[i]["degree"],
                    'Modalidad' : getModality(data[i]["density"]),
                    'Cursada'    : getMethods(data[i]["methods"]),
                    'Duracion Parcial'   : getDurationParcial(data[i]),
                    'Duracion Full'    : getDurationFull(data[i]),
                    'Descripcion' : data[i]["summary"],
                    'Nivel'      : data[i]["level"],
                    'Sub Nivel'      : data[i]["degree"],
                    'Logo'       : getLogo(data),
                    'Matricula'  : getMatricula(data[i]),
                    'Unidad Matricula' : getMatriculaUnit(data[i]),
                    'Moneda Matricula' : getMatriculaCoin(data[i])
                }
                
                diccionario_cuatro.append(diccuno)
    
                
            start = 0
            for i in range(iterations):
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 280) + '|lv-phd|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-phd|uc-84|tc-EUR&size=100&start=100':
                    break
                else:
                    start += 100
                    if len(data) == 0:
                        continue
                    else:
                        for i in range(len(datados)):
                            ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                            #print('Clave: ',ids)
                            names.append(ids)
                            
                            diccdos = {                
                                'Titulo'   : datados[i]["title"],
                                'Link'     : 'https://www.phdportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : datados[i]["venues"][0]['city'],
                                'Pais'     : datados[i]["venues"][0]['country'],
                                'Area'     : getArea(datados[i]["venues"][0]),   
                                'Universidad'   : getOrg(datados[i]), 
                                'Calificacion' : datados[i]["degree"],
                                'Modalidad' : getModality(datados[i]["density"]),
                                'Cursada'    : getMethods(datados[i]["methods"]),
                                'Duracion Parcial'   : getDurationParcial(datados[i]),
                                'Duracion Full'    : getDurationFull(datados[i]),
                                'Descripcion' : datados[i]["summary"],
                                'Nivel'      : datados[i]["level"],
                                'Sub Nivel'      : datados[i]["degree"],
                                'Logo'       : getLogo(data),
                                'Matricula'  : getMatricula(datados[i]),
                                'Unidad Matricula' : getMatriculaUnit(datados[i]),
                                'Moneda Matricula' : getMatriculaCoin(datados[i])
                            }
                            diccionario_cuatro.append(diccdos)
            start = 0
        
                    
                    
diccionario_total_phd = diccionario + diccionario_cero + diccionario_dos + diccionario_tres + diccionario_cuatro

links = [ each['Link'] for each in diccionario_total_phd ] 
unique_content = [ diccionario_total_phd[ links.index(id) ] for id in set([diccionario_total_phd[i]['Link'] for i in range(len(diccionario_total_phd))])]

with open('contenidototalphd.json', 'w', encoding='utf-8') as archivo:
    json.dump(unique_content, archivo, ensure_ascii = False, indent = 2)


contenido_phd = json.load(open('contenidototalphd.json', encoding='utf-8'))













