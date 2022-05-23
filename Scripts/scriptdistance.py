
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


class Distance():
    
    def __init__(self):
            self.main()

    def main(self):

        
        diccionario_cero = []
        start = ''
        linked = ''
        longitud_max = 9990
        iterations = int(9900 / 10)
        nombres =  []
        
        for i in range(iterations):
            url = 'https://search.prtl.co/2018-07-23/?' + str(linked) +'q=en-2384%7Cmh-blended%2Conline%7Ctc-CAD%7Cuc-56' 
            respuesta = requests.get(url)
            data = respuesta.json()
            print('Url: ',url)
            value = (i + 1) * 10
            linked = 'start=' +  str(value)  + '&'
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
                        'Link'     : 'https://www.'+ str(data[i]["level"])  +'sportal.com/studies/' +  str(data[i]["id"]),
                        'Ciudad'   : self.getCity(data),
                        'Pais'     : self.getPais(data),
                        'Area'     : self.getArea(data),   
                        'Universidad'   : self.getOrg(data[i]), 
                        'Calificacion' : data[i]["degree"],
                        'Modalidad' : self.getModality(data[i]["density"]),
                        'Cursada'    : self.getMethods(data[i]["methods"]),
                        'Duracion Parcial'   : self.getDurationParcial(data[i]),
                        'Duracion Full'    : self.getDurationFull(data[i]),
                        'Descripcion' : data[i]["summary"],
                        'Nivel'      : data[i]["level"],
                        'Sub Nivel'      : data[i]["degree"],
                        'Logo'       : self.getLogo(data),
                        'Matricula'  : self.getMatricula(data[i]),
                        'Unidad Matricula' : self.getMatriculaUnit(data[i]),
                        'Moneda Matricula' : self.getMatriculaCoin(data[i])
                    }
                    
                    diccionario_cero.append(diccero)
        
        
        
        diccionario = []
        names = []
        start = 100
        longitud_max = 9900
        iterations = int(9900 / 100)
        number = 0
        
        
        for i in range(iterations):
            url = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number) + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
            respuesta = requests.get(url)
            try:
                data = respuesta.json()
            except:
                print(url)
                print('VER!!!!!!!!!!!!!')
                continue
            print('Start: ',start)
            print('Url: ',url)
            number += 1
            if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
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
                            'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(data[i]["id"]),
                            'Ciudad'   : self.getCity(data),
                            'Pais'     : self.getPais(data),
                            'Area'     : self.getArea(data),   
                            'Universidad'   : self.getOrg(data[i]), 
                            'Calificacion' : data[i]["degree"],
                            'Modalidad' : self.getModality(data[i]["density"]),
                            'Cursada'    : self.getMethods(data[i]["methods"]),
                            'Duracion Parcial'   : self.getDurationParcial(data[i]),
                            'Duracion Full'    : self.getDurationFull(data[i]),
                            'Descripcion' : data[i]["summary"],
                            'Nivel'      : data[i]["level"],
                            'Sub Nivel'      : data[i]["degree"],
                            'Logo'       : self.getLogo(data),
                            'Matricula'  : self.getMatricula(data[i]),
                            'Unidad Matricula' : self.getMatriculaUnit(data[i]),
                            'Moneda Matricula' : self.getMatriculaCoin(data[i])
                        }
                        
                        diccionario.append(diccuno)
            
                        
                    start = 0
                    for i in range(iterations):
                        urldos = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number - 1) + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
                        respuestados = requests.get(urldos)
                        try:
                            datados = respuestados.json()
                        except:
                            print(urldos)
                            print('VER!!!!!!!!!!!!!')
                            continue
                        print('Start Dos: ',start)
                        print('Url Dos: ',urldos)
                        if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
                            break
                        else:
                            start += 100
                            if len(data) == 0:
                                continue
                            else:
                                for i in range(len(datados)):
                                    ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                                    print('Clave: ',ids)
                                    names.append(ids)
                                    
                                    diccdos = {                
                                        'Titulo'   : datados[i]["title"],
                                        'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(datados[i]["id"]),
                                        'Ciudad'   : self.getCity(datados),
                                        'Pais'     : self.getPais(datados),
                                        'Area'     : self.getArea(datados),   
                                        'Universidad'   : self.getOrg(datados[i]), 
                                        'Calificacion' : datados[i]["degree"],
                                        'Modalidad' : self.getModality(datados[i]["density"]),
                                        'Cursada'    : self.getMethods(datados[i]["methods"]),
                                        'Duracion Parcial'   : self.getDurationParcial(datados[i]),
                                        'Duracion Full'    : self.getDurationFull(datados[i]),
                                        'Descripcion' : datados[i]["summary"],
                                        'Nivel'      : datados[i]["level"],
                                        'Sub Nivel'      : datados[i]["degree"],
                                        'Logo'       : self.getLogo(data),
                                        'Matricula'  : self.getMatricula(datados[i]),
                                        'Unidad Matricula' : self.getMatriculaUnit(datados[i]),
                                        'Moneda Matricula' : self.getMatriculaCoin(datados[i])
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
            url = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number + 85) + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
            respuesta = requests.get(url)
            try:
                data = respuesta.json()
            except:
                print(url)
                print('VER!!!!!!!!!!!!!')
                continue
            print('Start: ',start)
            print('Url: ',url)
            number += 1
            if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
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
                            'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(data[i]["id"]),
                            'Ciudad'   : self.getCity(data),
                            'Pais'     : self.getPais(data),
                            'Area'     : self.getArea(data),   
                            'Universidad'   : self.getOrg(data[i]), 
                            'Calificacion' : data[i]["degree"],
                            'Modalidad' : self.getModality(data[i]["density"]),
                            'Cursada'    : self.getMethods(data[i]["methods"]),
                            'Duracion Parcial'   : self.getDurationParcial(data[i]),
                            'Duracion Full'    : self.getDurationFull(data[i]),
                            'Descripcion' : data[i]["summary"],
                            'Nivel'      : data[i]["level"],
                            'Sub Nivel'      : data[i]["degree"],
                            'Logo'       : self.getLogo(data),
                            'Matricula'  : self.getMatricula(data[i]),
                            'Unidad Matricula' : self.getMatriculaUnit(data[i]),
                            'Moneda Matricula' : self.getMatriculaCoin(data[i])
                        }
                        
                        diccionario_dos.append(diccuno)
            
                        
                    start = 0
                    for i in range(iterations):
                        urldos = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number - 1 + 85)  + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
                        respuestados = requests.get(urldos)
                        try:
                            datados = respuestados.json()
                        except:
                            print(urldos)
                            print('VER!!!!!!!!!!!!!')
                            continue
                        print('Start Dos: ',start)
                        print('Url Dos: ',urldos)
                        if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
                            break
                        else:
                            start += 100
                            if len(data) == 0:
                                continue
                            else:
                                for i in range(len(datados)):
                                    ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                                    print('Clave: ',ids)
                                    names.append(ids)
                                    
                                    diccdos = {                
                                        'Titulo'   : datados[i]["title"],
                                        'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(datados[i]["id"]),
                                        'Ciudad'   : self.getCity(datados),
                                        'Pais'     : self.getPais(datados),
                                        'Area'     : self.getArea(datados),   
                                        'Universidad'   : self.getOrg(datados[i]), 
                                        'Calificacion' : datados[i]["degree"],
                                        'Modalidad' : self.getModality(datados[i]["density"]),
                                        'Cursada'    : self.getMethods(datados[i]["methods"]),
                                        'Duracion Parcial'   : self.getDurationParcial(datados[i]),
                                        'Duracion Full'    : self.getDurationFull(datados[i]),
                                        'Descripcion' : datados[i]["summary"],
                                        'Nivel'      : datados[i]["level"],
                                        'Sub Nivel'      : datados[i]["degree"],
                                        'Logo'       : self.getLogo(data),
                                        'Matricula'  : self.getMatricula(datados[i]),
                                        'Unidad Matricula' : self.getMatriculaUnit(datados[i]),
                                        'Moneda Matricula' : self.getMatriculaCoin(datados[i])
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
            url = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number + 183) + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
            respuesta = requests.get(url)
            try:
                data = respuesta.json()
            except:
                print(url)
                print('VER!!!!!!!!!!!!!')
                continue
            print('Start: ',start)
            print('Url: ',url)
            number += 1
            if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
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
                            'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(data[i]["id"]),
                            'Ciudad'   : self.getCity(data),
                            'Pais'     : self.getPais(data),
                            'Area'     : self.getArea(data),   
                            'Universidad'   : self.getOrg(data[i]), 
                            'Calificacion' : data[i]["degree"],
                            'Modalidad' : self.getModality(data[i]["density"]),
                            'Cursada'    : self.getMethods(data[i]["methods"]),
                            'Duracion Parcial'   : self.getDurationParcial(data[i]),
                            'Duracion Full'    : self.getDurationFull(data[i]),
                            'Descripcion' : data[i]["summary"],
                            'Nivel'      : data[i]["level"],
                            'Sub Nivel'      : data[i]["degree"],
                            'Logo'       : self.getLogo(data),
                            'Matricula'  : self.getMatricula(data[i]),
                            'Unidad Matricula' : self.getMatriculaUnit(data[i]),
                            'Moneda Matricula' : self.getMatriculaCoin(data[i])
                        }
                        
                        diccionario_tres.append(diccuno)
            
                        
                    start = 0
                    for i in range(iterations):
                        urldos = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number - 1 + 183)  + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
                        respuestados = requests.get(urldos)
                        try:
                            datados = respuestados.json()
                        except:
                            print(urldos)
                            print('VER!!!!!!!!!!!!!')
                            continue
                        print('Start Dos: ',start)
                        print('Url Dos: ',urldos)
                        if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
                            break
                        else:
                            start += 100
                            if len(data) == 0:
                                continue
                            else:
                                for i in range(len(datados)):
                                    ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                                    print('Clave: ',ids)
                                    names.append(ids)
                                    
                                    diccdos = {                
                                        'Titulo'   : datados[i]["title"],
                                        'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(datados[i]["id"]),
                                        'Ciudad'   : self.getCity(datados),
                                        'Pais'     : self.getPais(datados),
                                        'Area'     : self.getArea(datados),   
                                        'Universidad'   : self.getOrg(datados[i]), 
                                        'Calificacion' : datados[i]["degree"],
                                        'Modalidad' : self.getModality(datados[i]["density"]),
                                        'Cursada'    : self.getMethods(datados[i]["methods"]),
                                        'Duracion Parcial'   : self.getDurationParcial(datados[i]),
                                        'Duracion Full'    : self.getDurationFull(datados[i]),
                                        'Descripcion' : datados[i]["summary"],
                                        'Nivel'      : datados[i]["level"],
                                        'Sub Nivel'      : datados[i]["degree"],
                                        'Logo'       : getLogo(data),
                                        'Matricula'  : self.getMatricula(datados[i]),
                                        'Unidad Matricula' : self.getMatriculaUnit(datados[i]),
                                        'Moneda Matricula' : self.getMatriculaCoin(datados[i])
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
            url = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number + 280) + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
            respuesta = requests.get(url)
            try:
                data = respuesta.json()
            except:
                print(url)
                print('VER!!!!!!!!!!!!!')
                continue
            print('Start: ',start)
            print('Url: ',url)
            number += 1
            if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
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
                            'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(data[i]["id"]),
                            'Ciudad'   : self.getCity(data),
                            'Pais'     : self.getPais(data),
                            'Area'     : self.getArea(data),   
                            'Universidad'   : self.getOrg(data[i]), 
                            'Calificacion' : data[i]["degree"],
                            'Modalidad' : self.getModality(data[i]["density"]),
                            'Cursada'    : self.getMethods(data[i]["methods"]),
                            'Duracion Parcial'   : self.getDurationParcial(data[i]),
                            'Duracion Full'    : self.getDurationFull(data[i]),
                            'Descripcion' : data[i]["summary"],
                            'Nivel'      : data[i]["level"],
                            'Sub Nivel'      : data[i]["degree"],
                            'Logo'       : self.getLogo(data),
                            'Matricula'  : self.getMatricula(data[i]),
                            'Unidad Matricula' : self.getMatriculaUnit(data[i]),
                            'Moneda Matricula' : self.getMatriculaCoin(data[i])
                        }
                        
                        diccionario_cuatro.append(diccuno)
            
                        
                    start = 0
                    for i in range(iterations):
                        urldos = 'https://search.prtl.co/2018-07-23/?q=di-' + str(number - 1 + 280)  + '%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=' + str(start)
                        respuestados = requests.get(urldos)
                        try:
                            datados = respuestados.json()
                        except:
                            print(urldos)
                            print('VER!!!!!!!!!!!!!')
                            continue
                        print('Start Dos: ',start)
                        print('Url Dos: ',urldos)
                        if url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=di-380%7Cen-2222%7Cmh-blended%2Conline%7Ctc-EUR&size=100&start=100':
                            break
                        else:
                            start += 100
                            if len(data) == 0:
                                continue
                            else:
                                for i in range(len(datados)):
                                    ids = datados[i]["title"] + ' - ' + str(datados[i]["id"])
                                    print('Clave: ',ids)
                                    names.append(ids)
                                    
                                    diccdos = {                
                                        'Titulo'   : datados[i]["title"],
                                        'Link'     : 'https://www.distancelearningportal.com/studies/' +  str(datados[i]["id"]),
                                        'Ciudad'   : self.getCity(datados),
                                        'Pais'     : self.getPais(datados),
                                        'Area'     : self.getArea(datados),   
                                        'Universidad'   : self.getOrg(datados[i]), 
                                        'Calificacion' : datados[i]["degree"],
                                        'Modalidad' : self.getModality(datados[i]["density"]),
                                        'Cursada'    : self.getMethods(datados[i]["methods"]),
                                        'Duracion Parcial'   : self.getDurationParcial(datados[i]),
                                        'Duracion Full'    : self.getDurationFull(datados[i]),
                                        'Descripcion' : datados[i]["summary"],
                                        'Nivel'      : datados[i]["level"],
                                        'Sub Nivel'      : datados[i]["degree"],
                                        'Logo'       : self.getLogo(data),
                                        'Matricula'  : self.getMatricula(datados[i]),
                                        'Unidad Matricula' : self.getMatriculaUnit(datados[i]),
                                        'Moneda Matricula' : self.getMatriculaCoin(datados[i])
                                    }
                                    diccionario_cuatro.append(diccdos)
                    start = 0
                
        
  
                            
        diccionario_total_distance = diccionario + diccionario_cero + diccionario_dos + diccionario_tres + diccionario_cuatro
        
        links = [ each['Link'] for each in diccionario_total_distance ] 
        unique_content = [ diccionario_total_distance[ links.index(id) ] for id in set([diccionario_total_distance[i]['Link'] for i in range(len(diccionario_total_distance))])]
        
        with open('contenidototaldistance.json', 'w', encoding='utf-8') as archivo:
            json.dump(unique_content, archivo, ensure_ascii = False, indent = 2)
        
        
    def getModality(self, data):
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
    
    
    def getMethods(self, data):
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
    
    
    def getDurationFull(self, data):
        try:
            
            valor = data['fulltime_duration']['value']
            unidad = data['fulltime_duration']['unit']
            total = str(valor) + ' ' + unidad
            return total
        except:
            return None
        
    def getDurationParcial(self, data):
        try:
            
            valor = data['parttime_duration']['value']
            unidad = data['parttime_duration']['unit']
            total = str(valor) + ' ' + unidad
            return total
        except:
            return None
        
    def getMatricula(self, data):
        try:
            matricula = data["tuition_fee"]["value"]
            return matricula
        except:
            return None
    
        
    def getMatriculaUnit(self, data):
        try:
            unidad = data["tuition_fee"]["unit"]
            return unidad
        except:
            return None
        
    def getMatriculaCoin(self, data):
        try:
            moneda = data["tuition_fee"]["currency"]
            return moneda
        except:
            return None
    
    
    
    def getLogo(self, data):
        try:
            if data[i]["logo"]:
                return data[i]["logo"]
            elif data[i]["squared_logo"]:
                return data[i]["logo"]
        except:
            return 
        
        
    def getOrg(self, data):
        try:
            org = data["organisation"]
            return org
        except:
            return None
            
    
             
    
    def getCity(self, data):
        try:
            city = data[i]["venues"][0]['city']
            return city
        except:
            return None      
    
    def getPais(self, data):
        try:
            pais = data[i]["venues"][0]['country']
            return pais
        except:
            return None 
    
    
    def getArea(self, data):
        try:
            area = data[i]["venues"][0]['area']
            return area
        except:
            return None   

if __name__ == "__main__":
    objName = Distance()
    objName.main() 



 
                    








