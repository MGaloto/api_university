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


href_final = []
names_final = []

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome('chromedriver.exe', options = options)
url = 'https://whed.net/home.php'
driver.get(url)
sleep(5)
html = driver.execute_script('return document.documentElement.outerHTML')
soup = BS(html, 'html.parser')
select = driver.find_element_by_id('Chp1')
select.click()
country = driver.find_element_by_xpath('//*[@id="Chp1"]/option[1]')
country.click()
llaves = driver.find_element_by_xpath('//*[@id="search"]')
llaves.send_keys('university')
enter = driver.find_element_by_xpath('//*[@id="fsearch"]/p/input')
enter.click()
despliegue = driver.find_element_by_xpath('//*[@id="contenu"]/form[1]/div/p[2]/select')
despliegue.click()
cien = driver.find_element_by_xpath('//*[@id="contenu"]/form[1]/div/p[2]/select/option[4]')
cien.click()
html = driver.execute_script('return document.documentElement.outerHTML')
soup = BS(html, 'html.parser')
contenidos = soup.find_all('a', { 'class' : 'fancybox fancybox.iframe'  })
names      = soup.find_all('a', { 'class' : 'fancybox fancybox.iframe'  })
name       = [names[i].text for i in range(len(names))]
hrefs = ['https://whed.net/' + contenidos[i]['href'] for i in range(len(contenidos))]
href_final.append(hrefs)
names_final.append(name)
page_dos = driver.find_element_by_xpath('//*[@id="contenu"]/form[2]/div/a[1]')
page_dos.click()

for i in range(118):
    page_next = driver.find_element_by_class_name('next')
    page_next.click()
    sleep(2)
    html = driver.execute_script('return document.documentElement.outerHTML')
    soup = BS(html, 'html.parser')
    contenidos = soup.find_all('a', { 'class' : 'fancybox fancybox.iframe'  })
    names      = soup.find_all('a', { 'class' : 'fancybox fancybox.iframe'  })
    name       = [names[i].text for i in range(len(names))]
    hrefs = ['https://whed.net/' + contenidos[i]['href'] for i in range(len(contenidos))]
    href_final.append(hrefs)
    names_final.append(name)



href_final_unique = []
for i in range(len(href_final)):
    href = href_final[i]
    for i in range(len(href)):
        href_final_unique.append(href[i])
    

names_final_unique = []
for i in range(len(names_final)):
    names = names_final[i]
    for i in range(len(names)):
        names_final_unique.append(names[i])


names_final_unique_clean = []
for i in range(len(names_final_unique)):
    names = names_final_unique[i].replace('\n\t\t    ', '').replace('\t\t  ', '').replace('\t', '').replace('\n', '')
    names_final_unique_clean.append(names)




def getStreet(soup):
    try:
        street = soup.find_all('div', { 'class' : 'dl'})
        street = street[0].text.split('Street:')[1].split('\n')[0]
        return street
    except:
        return None
    
def getLogo(soup):
    logos = soup.find_all('div', { 'class': 'galerie'})
    lista_logos = []
    if len(logos) >= 1:
        for i in range(len(logos)):
            logos_final = ['https://whed.net/' + logos[i]['style'].replace(')','').replace('background-image:url(','')for i in range(len(logos))]
            lista_logos.append(logos_final)

        return logos_final
    else:
        return lista_logos
    



def getCity(soup):
    try:
        inst = soup.find_all('div', { 'class' : 'dl'})
        inst = inst[0].text.split('City:')[1].split('\n')[0]
        return inst
    except:
        return None
                
    
    
def getInstitute(soup):
    try:
        inst = soup.find_all('div', { 'class' : 'dl'})
        for i in range(len(inst)):
                if inst[i].find('span').text == 'Institution Funding ' or inst[i].find('span').text == 'Institution Funding':
                    institute = inst[i].p.text
        return institute
    except:
        return None
    
def getHistory(soup):
    try:
        explore = soup.find_all('div', { 'class' : 'dl'})
        for i in range(len(explore)):
                if explore[i].find('span').text == 'History ' or explore[i].find('span').text == 'History':
                    hist = explore[i].p.text
        return hist
    except:
        return None


def getProvincia(soup):
    try:
        prov = soup.find_all('div', { 'class' : 'dl'})[0]
        prov = prov.text.split('Province:')[1].split('\n')[0]
        return prov
    except:
        return None
    

def getCountry(soup):
    try:
        country = soup.find_all('p', { 'class': 'country'})[0].text
        return country
    except:
        return None
    
def getLink(soup):
    try:
        link = soup.find_all('a', { 'class': 'lien'})[0]['href']
        return link
    except:
        return None
                  
def getLang(soup):
    try:
        inst = soup.find_all('div', { 'class' : 'dl'})
        for i in range(len(inst)):
                if inst[i].find('span').text == 'Language(s) ' or inst[i].find('span').text == 'Language(s)':
                    institute = inst[i].p.text
        return institute
    except:
        return None
            
contenidofinal =  []


count = 0
for href in href_final_unique:
    print('Nombre', names_final_unique_clean[count].strip())
    sleep(.25)
    count += 1
    response = requests.get(href)
    print(href)
    #tree     = html.fromstring(response.content)
    soup = BS(response.text, 'lxml')
    
    print('\nHREF: ',href)
    
    ciudad = getCity(soup)
    street = getStreet(soup)
    inst   = getInstitute(soup)
    hist   = getHistory(soup)
    logo   = getLogo(soup)
    link   = getLink(soup)
    provincia = getProvincia(soup)
    pais = getCountry(soup)
    
    print('Provincia: ',provincia)
    print('Ciudad: ',ciudad)
    print('Calle: ',street)
    print('Instituto: ',inst)
    print('Historia: ',hist)
    print('Logo: ',logo)
    print('pais', pais)
    print('LENG: ', getLang(soup))
    print('Link: ',link,'\n')
    
    dicc = {'Area'           : None,
            'Titulo'         : None,
            'Categoria'      : None,
            'Nivel'          : None,
            'Pais'           : getCountry(soup),
            'Ciudad'         : getCity(soup),
            'Lenguaje'       : getLang(soup),
            'Provincia'      : getProvincia(soup),
            'Calle'          : getStreet(soup),
            'Sitio'          : None,
            'Institucion'    : getInstitute(soup),
            'Subtitulos'     : None,
            'Calificacion'   : None,
            'Part Time'      : None,
            'Full Time'      : None,
            'Cursada'        : None,
            'Duracion'       : None,
            'Carrera'        : None,
            'Universidad'    : names_final_unique_clean[count - 1].strip(),
            'Descripcion'    : getHistory(soup),
            'Deadline'       :None,
            'Requerimientos' : None,
            'Link'           : href,
            'Tutition Free'  : None,
            'Valoracones'    : None,
            'About University': None,
            'Link University' : getLink(soup),
            'logo'           : getLogo(soup),
            'Multimedia'     : None
            }
            

    contenidofinal.append(dicc)
    


with open('whed.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(contenidofinal, archivo_json, ensure_ascii=False, indent = 2)



#%%








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


url = 'https://search.prtl.co/2018-07-23/?q=en-359|lv-bachelor|uc-84|tc-EUR&size=100&start=0'
respuesta = requests.get(url)
data = respuesta.json()




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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
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
                'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(data[i]["id"]),
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



'https://www.bachelorsportal.com/studies/' +  str(data[0]["id"])

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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(datados[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 85) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 85) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(datados[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 183) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 183) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(datados[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 280) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 280) + '|lv-bachelor|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-bachelor|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.bachelorsportal.com/studies/' +  str(datados[i]["id"]),
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
        
                    
                    
diccionario_total = diccionario + diccionario_cero + diccionario_dos + diccionario_tres + diccionario_cuatro

links = [ each['Link'] for each in diccionario_total ] 
unique_content = [ diccionario_total[ links.index(id) ] for id in set([diccionario_total[i]['Link'] for i in range(len(diccionario_total))])]

with open('contenidototalbachiller.json', 'w', encoding='utf-8') as archivo:
    json.dump(unique_content, archivo, ensure_ascii = False, indent = 2)


contenido_bachiller = json.load(open('contenidototalbachiller.json', encoding='utf-8'))


#%%






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
        

         

def getCity(data):
    try:
        city = data[i]["venues"][0]['city']
        return city
    except:
        return None      

def getPais(data):
    try:
        pais = data[i]["venues"][0]['country']
        return pais
    except:
        return None 


def getArea(data):
    try:
        area = data[i]["venues"][0]['area']
        return area
    except:
        return None   



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
                'Ciudad'   : getCity(data),
                'Pais'     : getPais(data),
                'Area'     : getArea(data),   
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
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data),   
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
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados),   
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
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data),   
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
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados),   
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
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data),   
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
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados),   
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
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data),   
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
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados),   
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
        
        
        
        
        
        
        
                    
                    
diccionario_total_distance = diccionario + diccionario_cero + diccionario_dos + diccionario_tres + diccionario_cuatro

links = [ each['Link'] for each in diccionario_total_distance ] 
unique_content = [ diccionario_total_distance[ links.index(id) ] for id in set([diccionario_total_distance[i]['Link'] for i in range(len(diccionario_total_distance))])]

with open('contenidototaldistance.json', 'w', encoding='utf-8') as archivo:
    json.dump(unique_content, archivo, ensure_ascii = False, indent = 2)


contenido_distance = json.load(open('contenidototaldistance.json', encoding='utf-8'))


#%%




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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
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
                'Link'     : 'https://www.mastersportal.com/studies/' +  str(data[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.mastersportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.mastersportal.com/studies/' +  str(datados[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 85) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.mastersportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 85) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.mastersportal.com/studies/' +  str(datados[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 183) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.mastersportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 183) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.mastersportal.com/studies/' +  str(datados[i]["id"]),
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 280) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.mastersportal.com/studies/' +  str(data[i]["id"]),
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 280) + '|lv-master|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-master|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.mastersportal.com/studies/' +  str(datados[i]["id"]),
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
        
                    
                    
diccionario_total_master = diccionario + diccionario_cero + diccionario_dos + diccionario_tres + diccionario_cuatro

links = [ each['Link'] for each in diccionario_total_master ] 
unique_content = [ diccionario_total_master[ links.index(id) ] for id in set([diccionario_total_master[i]['Link'] for i in range(len(diccionario_total_master))])]

with open('contenidototalmaster.json', 'w', encoding='utf-8') as archivo:
    json.dump(unique_content, archivo, ensure_ascii = False, indent = 2)


contenido_master = json.load(open('contenidototalmaster.json', encoding='utf-8'))


#%%




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



#%%




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
        

def getCity(data):
    try:
        city = data[i]["venues"][0]['city']
        return city
    except:
        return None      

def getPais(data):
    try:
        pais = data[i]["venues"][0]['country']
        return pais
    except:
        return None 


def getArea(data):
    try:
        area = data['venues'][0]['area']
        return area
    except:
        return None            
     



diccionario_cero = []

start = 0

longitud_max = 9900

iterations = int(9900 / 100)

nombres =  []



for i in range(iterations):
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
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
                'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(data[i]["id"]),
                'Ciudad'   : getCity(data),
                'Pais'     : getPais(data),
                'Area'     : getArea(data[i]),   
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data[i]),   
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados[i]),   
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 85) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data[i]),   
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 85) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados[i]),   
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 183) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data[i]),   
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 183) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados[i]),   
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
    url = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number + 280) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
    respuesta = requests.get(url)
    data = respuesta.json()
    print('Start: ',start)
    print('Url: ',url)
    number += 1
    if url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                    'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(data[i]["id"]),
                    'Ciudad'   : getCity(data),
                    'Pais'     : getPais(data),
                    'Area'     : getArea(data[i]),   
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
                urldos = 'https://search.prtl.co/2018-07-23/?q=en-359|di-' + str(number - 1 + 280) + '|lv-short|uc-84|tc-EUR&size=100&start=' + str(start)
                respuestados = requests.get(urldos)
                datados = respuestados.json()
                print('Start Dos: ',start)
                print('Url Dos: ',urldos)
                if urldos == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=0' or url == 'https://search.prtl.co/2018-07-23/?q=en-359|di-380|lv-short|uc-84|tc-EUR&size=100&start=100':
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
                                'Link'     : 'https://www.shortcoursesportal.com/studies/' +  str(datados[i]["id"]),
                                'Ciudad'   : getCity(datados),
                                'Pais'     : getPais(datados),
                                'Area'     : getArea(datados[i]),   
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
        
                    
                    
diccionario_total_short = diccionario + diccionario_cero + diccionario_dos + diccionario_tres + diccionario_cuatro

links = [ each['Link'] for each in diccionario_total_short ] 
unique_content = [ diccionario_total_short[ links.index(id) ] for id in set([diccionario_total_short[i]['Link'] for i in range(len(diccionario_total_short))])]

with open('contenidototalshort.json', 'w', encoding='utf-8') as archivo:
    json.dump(unique_content, archivo, ensure_ascii = False, indent = 2)


contenido_short = json.load(open('contenidototalshort.json', encoding='utf-8'))


#%%



import json
import pprint
import pandas as pd

contenidos          = json.load(open('contenidototalbachiller.json', encoding='utf-8'))

contenidos_distance = json.load(open('contenidototaldistance.json', encoding='utf-8'))

contenidos_phd      = json.load(open('contenidototalphd.json', encoding='utf-8'))

contenidos_master   = json.load(open('contenidototalmaster.json', encoding='utf-8'))

contenidos_short    = json.load(open('contenidototalshort.json', encoding='utf-8'))

whedd                = json.load(open('whedfinal.json', encoding='utf-8'))


def cleanWhed(pais):
    serie_clean = []
    if '-' in pais:
        ser = pais.split('-')[0]
        serie_clean.append(ser.replace(' of America','').replace(' Federation','').strip())
    elif '(' in pais:
        ser = pais.split('(')[0]
        serie_clean.append(ser.replace(' of America','').replace(' Federation','').strip())
    else:
        serie_clean.append(pais.replace(' of America','').replace(' Federation','').strip())
    return serie_clean[0]
    




'''
WHED
'''
whed = []
count = 0
for we in whedd:
    count += 1
    print(count)
    dicc = { 'Area': we['Area'],
             'Pais': cleanWhed(we['Pais']),
             'Ciudad': we['Ciudad'],
             'Calles': we['Calles'],
             'Institucion': we['Institucion'],
             'Idioma': we['Idioma'],
             'Subtitulos': we['Subtitulos'],
             'Calificacion': we['Calificacion'],
             'Nivel': we['Nivel'],
             'Part Time':we['Part Time'],
             'Full Time':we['Full Time'],
             'Cursada': we['Cursada'],
             'Duracion': we['Duracion'],
             'Titulo':we['Titulo'],
             'Universidad': we['Universidad'],
             'Descripcion Programa': we['Descripcion Programa'],
             'Descripcion Universidad': we['Descripcion Universidad'],
             'Categoria': we['Categoria'],
             'Deadline':we['Deadline'],
             'Requerimientos':we['Requerimientos'],
             'Tutition Free':we['Tutition Free'],
             'Valoracones': we['Valoracones'],
             'Link University': we['Link University'],
             'logo': we['logo'],
             'Multimedia': we['Multimedia']}
    whed.append(dicc)







universidad_whed       = []
link_universidad_whed  = []
lenguaje_whed          = []
calle_whed             = []
institucion_whed       = []
universidad_desc_whed  = []



for i in range(len(whed)):
    if whed[i]['Universidad'] == None:
        value = 'Unknown'
        universidad_whed.append(value)
    else:
        universidad_whed.append(whed[i]['Universidad'].lower())


for i in range(len(whed)):
    if whed[i]['Link University'] == None:
        value = 'Unknown'
        link_universidad_whed.append(value)
    else:
        link_universidad_whed.append(whed[i]['Link University'])
        
for i in range(len(whed)):
    if whed[i]['Idioma'] == None:
        value = 'Unknown'
        lenguaje_whed.append(value)
    else:
        lenguaje_whed.append(whed[i]['Idioma'])
    
for i in range(len(whed)):
    if whed[i]['Calles'] == None:
        value = 'Unknown'
        calle_whed.append(value)
    else:
        calle_whed.append(whed[i]['Calles'])
    
for i in range(len(whed)):
    if whed[i]['Institucion'] == None:
        value = 'Unknown'
        institucion_whed.append(value)
    else:
        institucion_whed.append(whed[i]['Institucion'])
        
for i in range(len(whed)):
    if whed[i]['Universidad'] == None:
        value = 'Unknown'
        universidad_desc_whed.append(value)
    else:
        universidad_desc_whed.append(whed[i]['Descripcion Universidad'])




print(len(universidad_whed))
print(len(link_universidad_whed))
print(len(lenguaje_whed))
print(len(calle_whed))
print(len(institucion_whed))
print(len(universidad_desc_whed))


category = ["Landscape Architecture",
"Computer Science",
"Master in Management (MIM)",
"Agriculture & Forestry",
"Human Resource Management",
"Software Engineering",
"Materials Science & Engineering",
"Electronics & Embedded Technology",
"Electrical Engineering",
"Environmental Economics & Policy",
"International Relations",
"Business Intelligence & Analytics",
"General Studies & Classics",
"Media Studies & Mass Media",
"International Development",
"Journalism",
"Video Games & Multimedia",
"Urban Planning",
"Technology Management",
"Art History",
"Strategic Management",
"Teaching",
"Bioinformatics",
"Biotechnology",
"Industrial & Systems Engineering",
"Environmental Management",
"Logistics Technology",
"Sports Management",
"Music",
"Media studies",
"Civil Engineering & Construction",
"Geographical Information Systems (GIS)",
"Risk Management",
"Artes Culinarias",
"Master in Business Administration (MBA)",
"Area & Cultural Studies",
"Robotics",
"Microbiology",
"Journalism & Media",
"Business Administration",
"Management, organization & Leadership",
"User Experience Design",
"Journalism & Media",
"Energy & Power Engineering",
"Tourism & Leisure",
"Marketing",
"Bio & Biomedical Engineering",
"Engineering & Technology",
"Digital Marketing",
"Metallurgical Engineering",
"Nanotechnology",
"Graphic Design",
"Health Informatics",
"Public Relations",
"Statistics",
"Education & Training",
"Biochemistry",
"Artificial Intelligence",
"Transportation Engineering",
"Architecture",
"Sustainable Energy",
"Coaching",
"Design",
"Web Technologies & Cloud Computing",
"Biology",
"Cognitive Sciences",
"Theatre & Dance",
"Business Information Systems",
"Film, Photography & Media",
"Project Management",
"Financial Mathematics",
"Modern History",
"Communication Sciences",
"Fashion Design",
"Astronomy & Space Sciences",
"Accounting",
"Accouting",
"Event Management",
"Economic Sciences",
"Culinary Arts",
"Automotive Engineering",
"Data Science & Big Data",
"Economics",
"Industrial Design",
"Chemical Engineering",
"Corporate Social Responsabilities",
"Internet of ThingsElectronic Engineering",
"Museum Studies",
"Media Management",
"Public Administration",
"Corporate Social Responsibility",
"Applied Mathematics",
"Econometrics",
"Computer Science & IT",
"Sustainable Development",
"Business & Management",
"Visual Arts",
"Management, Organisation & Leadership",
"Human Computer Interaction",
"Robotic",
"Physics",
"Natural Sciences & Mathematics",
"International Business",
"Computer Sciences",
"Supply Chain Management & Logistics",
"IT Security",
"Transport Management",
"Innovation Management",
"Corporate Communication",
"Cyber Security",
"Digital Communication",
"Music History",
"Entrepreneurship",
"Ancient History",
"Applied Sciences & Professions",
"Aerospace Engineering",
"Sports Sciences",
"Cybersecurity",
"Machine Learning",
"Mathematics",
"Finance",
"Mechatronics",
"Interior Design",
"Terrorism & Security",
"Executive MBA",
"Philosophy & Ethics",
"Retail Management",
"Informatics & Information Sciences",
"Business",
"Business Intelligence & Arts",
"Literature",
"Media Studies",
"Neuroscience",
"Environmental Engineering",
"Actuarial Science",
"Electrotechnical Engineering",
"Marine Engineering",
"Commerce",
"Arts, Design & Architecture",
"Computer Science & Big Data",
"Creative Writing",
"Organisational Behaviour",
"Human Resources Management",
"Liberal Arts",
"General Engineering & Technology",
"Political Science",
"Mechanical Engineering",
"Corporate Comminication",
"Data",
"Data Mining",
"Data Science",
"Data Analytics",
"Data Engineer",
"Technology",
'Machine Learning',
'Artificial Intelligence',
"Creative",
"Creativity",
"Writing",
"Virtual and Augmented Reality ",
"Metaverse",
"Digital Interactive ",
"Gaming for virtual and Augmented Reality ",
"Reality Works ",
"VR",
"Unity XR",
"Virtual Reality",
"Augumented Reality",
"Storytelling ",
"Immersive",
"3D",
"Content",
"Creative Industries",
"Arts",
"Film",
"Film Studies",
"Film Production",
"Film and Television Production",
"Film and Media",
"Media Studies",
"Media",
"American Studies",
"Video Production",
"Production Technology",
"Media Arts",
"Production",
"Digital Content",
"Screenwriting",
"Writer",
"Photography",
"Radio",
"Television",
"Digital Cinema ",
"Interactive Media",
"Theatre",
"Film History",
"Innovation",
"Writing",
"Film Studies with Philosophy",
"Films Arts",
"Video ",
"TV",
"Virtual and Augmented Reality",
"Literature",
"Game",
"Gamming",
"Virtual Worlds",
"Animation",
"Virtual Worlds",
"Visualisation",
"Communication",
"Music",
"Architecture",
"Paintwork",
"Sculpture",
"Music",
"Dance",
"Literature",
"Cinema",
"Inmmersive Media",
"Music Production",
"Game Development ",
"Creative Computing",
"Video Game Design and Animation",
"Art and Design",
"Art and Technology",
"Digital Art",
"Content Curation",
"Web Media",
"Culture and Arts",
"Multimedia",
"VFX",
"Business and Arts",
"Arts and Business",
"Music Business",
"Arts Administration",
"Entertaiment Management",
"Arts Management",
"Law and Arts",
"Art",
"Visual",
"Creative Writing ",
"Entertaiment",
"Fashion",
"Paint",
"Textiles",
"Fashion Communication",
"Photography",
"Animation",
"Visual Effects",
"Acting",
"Studio Art",
"Emmerging Media",
"New Media",
"Culture",
"Web Communication",
"Strategic Communication",
"Media Production",
"Video Game",
"Culinary Arts",
"Documentary",
"Screen",
"Cinematography",
"Fine Art",
"Post - Production",
"Art Gallery",
"Museum",
"Narrative",
"Drama",
"Image",
"Crafts",
"Experiences",
"Filmmaking",
"Ceramic",
"Ethnomusicology",
"Artist",
"Jazz",
"Metaverse",
"Web Technologies",
"Virtual Worlds",
"Gaming for virtual and Augmented Reality ",
"Reality Works ",
"VR ",
"Unity XR",
"Augumented Reality",
"Immersive",
"Virtual Reality",
"Tech ",
"Technology",
"Production Technology",
"Game Design",
"Virtual Technology and Design",
"Virtual and Augmented Reality",
"Game",
"Gamming",
"Virtual Worlds",
"Cybersecurity",
"Informatics",
"Robotics",
"Computer Science",
"Development ",
"Programming",
"Game Development ",
"Creative Computing",
"Computer",
"IT",
"Computer Games",
"Art and Technology",
"Computing for Interaction",
"Engineering",
"Tecnology and Business",
"Technology and Business",
"Emmerging Media",
"Cyber",
"Informatics",
"Software",
"Artificial Intelligence",
"Software",
"Technoculture",
"Developer",
"Systems",
"Computer",
"IT",
"Software Development",
"Back - end",
"Front- end",
"Smart ",
"Future",
"Biotechnology",
"Technological Innovation",
"Information Technology",
"Machines",
"Coumputing",
"Creative",
"Creativity",
"Writing",
"Design ",
"UX",
"UI",
"Product Design ",
"Web Design ",
"Web ",
"App ",
"Creative",
"Design for Virtual Reality",
"Virtual Reality",
"Motion Design",
"Photography",
"Visual Arts",
"Game Design",
"Virtual Technology and Design",
"Virtual Reality Design",
"Interior Design",
"Visualisation",
"Graph",
"Graphic",
"Graphic Design",
"Media Design",
"Design Development ",
"User experience ",
"User Experience Design",
"Industrial Design",
"Video Game Design and Animation",
"Art and Design",
"Digital Art ",
"Games",
"Illustration",
"Interaction Design",
"3D",
"UX Design",
"Furniture Design",
"Innovation and Design",
"Communication Design ",
"Web Media",
"Sustainable Design",
"Design Studies",
"Human- Centered",
"Fashion Design",
"Business Design",
"Entertaiment Design",
"Social Anthropology",
"Service Design ",
"Visual Communication",
"Front-end",
"Smart Service",
"Interaction Design",
"Experience Design",
"Visual",
"Human Computer",
"Urban Design",
"Visual Narrative",
"Creative Writing",
"Image",
"Urban ",
"International Relations",
"Health",
"Leadership",
"Sustainable",
"Social Change",
"Corporate Communications",
"Human Resources",
"Resource Management",
"Employment",
"Business Human",
"International Human",
"HRM",
"Health Administration",
"Digital Transformation",
"Coaching",
"Itercultural",
"Culture and Society",
"Culture Studies",
"Anthropology",
"Culture",
"Sociology",
"Psychology",
"Organisational Behaviour",
"Organizational",
"Conflict Studies",
"Organizational Leadership",
"Behaviour",
"Computer Science",
"Data",
"Artificial Intelligence",
"Machine Learning ",
"Big Data",
"Data Science",
"Python ",
"Analytics",
"AI",
"Cloud",
"USI",
"Cloud Computing",
"Analysis",
"Biotechnology",
"Social Media",
"Marketing",
"Marketing Digital ",
"Innovation",
"Commerce",
"Fashion Marketing",
"Fashion Management",
"Merchandising",
"Promotion",
"Fashion Buying",
"Sports Marketing",
"Advertising",
"Global Marketing ",
"Brand",
"Brand Management",
"Public Relations",
"Interactive Media and Game Design - Business , Marketing and Enterprise",
"Consumer",
"Behaviour",
"Media Communications",
"Web Communication",
"Journalism",
"Digital Communication",
"Radio",
"Arts and Business",
"Legal Studies",
"Business",
"Tecnology and Business",
"Music Business",
"Global Business",
"MBA",
"Management",
"Creative Business",
"Administration",
"Ecconomics",
"Accounting",
"Finance",
"Business Management",
"Financial Services",
"Football Business",
"Digital Business",
"Interactive Media and Game Design - Business , Marketing and Enterprise",
"Digital Innovation",
"Interantional Business",
"Busineess Law",
"Sales",
"BGM",
"Digital Interactive ",
"Media Management",
"Product Design ",
"Digital Product",
"Apps ",
"Web",
"App Development",
"Innovation",
"Product",
"Digital Product",
"Innovation",
"Mobile Development",
"Product Development",
"Product Management",
"Enterprise",
"Entrepreneurship",
"Digital Service",
"Interactive Media and Game Design - Business , Marketing and Enterprise",
"Digital Innovation",
"Smart Service",
"Project Management",
"Media Business",
"Project Innovation",
'Augmented Reality',
'VR',
'Virtual Worlds',
'Virtual Reality',
'Augmented Reality',
'VR',
'Virtual Worlds',
'Virtual Reality',
'Augmented Reality',
'VR',
'Virtual Worlds',
'Virtual Reality'
]






areas = [
"DESIGN",
"TECH",
"BUSINESS",
"DESIGN",
"BUSINESS",
"TECH",
"TECH",
"TECH",
"TECH",
"BUSINESS",
"BUSINESS",
"BUSINESS",
"ARTS",
"ARTS",
"BUSINESS",
"ARTS",
"ARTS",
"DESIGN",
"PRODUCT",
"ARTS",
"PRODUCT",
"SOFT SKILLS",
"TECH",
"TECH",
"TECH",
"BUSINESS",
"TECH",
"SOFT SKILLS",
"ARTS",
"ARTS",
"TECH",
"TECH",
"BUSINESS",
"ARTS",
"BUSINESS",
"ARTS",
"TECH",
"TECH",
"ARTS",
"BUSINESS",
"BUSINESS",
"DESIGN",
"ARTS",
"TECH",
"ARTS",
"MARKETING",
"TECH",
"TECH",
"MARKETING",
"TECH",
"TECH",
"DESIGN",
"TECH",
"ARTS",
"BUSINESS",
"SOFT SKILLS",
"TECH",
"TECH",
"TECH",
"ARTS",
"TECH",
"SOFT SKILLS",
"DESIGN",
"TECH",
"TECH",
"TECH",
"ARTS",
"TECH",
"ARTS",
"PRODUCT",
"BUSINESS",
"ARTS",
"MARKETING",
"ARTS",
"TECH",
"BUSINESS",
"BUSINESS",
"BUSINESS",
"BUSINESS",
"ARTS",
"TECH",
"DATA",
"BUSINESS",
"DESIGN",
"TECH",
"BUSINESS",
"TECH",
"ARTS",
"ARTS",
"BUSINESS",
"BUSINESS",
"BUSINESS",
"BUSINESS",
"TECH",
"TECH",
"BUSINESS",
"ARTS",
"BUSINESS",
"TECH",
"TECH",
"TECH",
"BUSINESS",
"BUSINESS",
"TECH",
"BUSINESS",
"TECH",
"BUSINESS",
"BUSINESS",
"BUSINESS",
"TECH",
"SOFT SKILLS",
"ARTS",
"PRODUCT",
"ARTS",
"TECH",
"TECH",
"SOFT SKILLS",
"TECH",
"DATA",
"BUSINESS",
"BUSINESS",
"TECH",
"DESIGN",
"TECH",
"BUSINESS",
"ARTS",
"PRODUCT",
"TECH",
"BUSINESS",
"BUSINESS",
"ARTS",
"ARTS",
"TECH",
"TECH",
"DATA",
"TECH",
"TECH",
"BUSINESS",
"ARTS",
"TECH",
"DESIGN",
"BUSINESS",
"SOFT SKILLS",
"ARTS",
"TECH",
"BUSINESS",
"TECH",
"SOFT SKILLS" ,
"DATA",
"DATA",
"DATA",
"DATA",
"DATA"
"TECH",
"DATA",
"DATA",
'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'ARTS',
 'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
 'DESIGN',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'SOFT SKILLS',
'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
 'DATA',
'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
 'MARKETING',
'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'BUSINESS',
 'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'PRODUCT',
  'ARTS',
  'ARTS',
  'ARTS',
  'ARTS',
  'TECH',
  'TECH',
  'TECH',
  'TECH',
  'DESIGN',
  'DESIGN',
  'DESIGN',
  'DESIGN'
]




def getUniversity(universidad, universidad_whed, link_universidad_whed):
    if universidad != None:
        universidad = universidad.lower()
        for i in range(len(universidad_whed)):
            try:
                if universidad_whed[i] != None:
                    if universidad_whed[i].lower()  == universidad or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace(' - ', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace(' - ', ' ')  or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace(' - ', '').lower()  == universidad.replace('-', '') or universidad_whed[i].replace('-', '').lower()  == universidad.replace(' - ', '') or universidad_whed[i].lower() == universidad.replace('niversity', '').replace('university', '').replace('niversity', ' ').replace('university', ' ') or universidad_whed[i].replace('niversity', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad.replace('university', '').replace('university', '').replace('university', ' ').replace('university', ' ') or universidad_whed[i].replace('university', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad or universidad_whed[i].replace('at', ' ').replace('at', ' ').lower()  == universidad.replace('at', ' ') or universidad_whed[i].replace('college', ' ').replace('college ', ' ').lower()  == universidad.replace('college', ' ').replace('college ', ' ')  or universidad_whed[i].split('-')[0]  == universidad  or universidad_whed[i].split(' - ')[0]  == universidad  or universidad_whed[i].split(',')[0]  == universidad or universidad_whed[i].replace('the ','')  == universidad or universidad_whed[i].lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').replace('of ','').lower()  == universidad.replace('the ','').replace('of ','') or universidad_whed[i].split(' - ')[0].lower()   == universidad or universidad_whed[i].split('-')[0].lower()   == universidad or universidad_whed[i].split(',')[0].lower()   == universidad or universidad_whed[i].replace('the ','').lower()  == universidad:
                        return link_universidad_whed[i]
            except:
                   return 'Unknown'
    else:
        return 'Unknown'





def getAreas(category, areas, categoria):
    areas_totales = []
    try:
        
        for i in range(len(category)):
            if categoria == category[i] or categoria.split(' ')[0].lower() == category[i].lower() or categoria.lower() == category[i].lower():
                areas_totales.append(areas[i])
         
        final = set(areas_totales)
        lista_areas = list(final)
        return lista_areas
    except:
        return list()
    



def getDuracion(datapart, datafull):
    data_part = datapart
    data_full = datafull
    if data_part == None:
        return data_full
    else:
        return data_part
    
def getMatricula(importe, moneda, unidad):
    importe = cont['Matricula']
    moneda  = cont['Moneda Matricula']
    unidad  = cont['Unidad Matricula']
    if importe == None:
        return None
    else:
        tutition = str(importe) + ' ' + str(moneda) + ' / ' + str(unidad)
        return tutition

    
def getLang(universidad, universidad_whed, lenguaje_whed):
    if universidad != None:
        universidad = universidad.lower()
        for i in range(len(universidad_whed)):
            try:
                if universidad_whed[i] != None:
                    if universidad_whed[i].lower()  == universidad or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace(' - ', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace(' - ', ' ')  or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace(' - ', '').lower()  == universidad.replace('-', '') or universidad_whed[i].replace('-', '').lower()  == universidad.replace(' - ', '') or universidad_whed[i].lower() == universidad.replace('niversity', '').replace('university', '').replace('niversity', ' ').replace('university', ' ') or universidad_whed[i].replace('niversity', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad.replace('university', '').replace('university', '').replace('university', ' ').replace('university', ' ') or universidad_whed[i].replace('university', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad or universidad_whed[i].replace('at', ' ').replace('at', ' ').lower()  == universidad.replace('at', ' ') or universidad_whed[i].replace('college', ' ').replace('college ', ' ').lower()  == universidad.replace('college', ' ').replace('college ', ' ')  or universidad_whed[i].split('-')[0]  == universidad  or universidad_whed[i].split(' - ')[0]  == universidad  or universidad_whed[i].split(',')[0]  == universidad or universidad_whed[i].replace('the ','')  == universidad or universidad_whed[i].lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').replace('of ','').lower()  == universidad.replace('the ','').replace('of ','') or universidad_whed[i].split(' - ')[0].lower()   == universidad or universidad_whed[i].split('-')[0].lower()   == universidad or universidad_whed[i].split(',')[0].lower()   == universidad or universidad_whed[i].replace('the ','').lower()  == universidad:
                        return lenguaje_whed[i]
            except:
                   return 'Unkwnown'
    else:
        return 'Unknown'


def getCalles(universidad, universidad_whed, calle_whed):
    if universidad != None:
        universidad = universidad.lower()
        for i in range(len(universidad_whed)):
            try:
                if universidad_whed[i] != None:
                    if universidad_whed[i].lower()  == universidad or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace(' - ', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace(' - ', ' ')  or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace(' - ', '').lower()  == universidad.replace('-', '') or universidad_whed[i].replace('-', '').lower()  == universidad.replace(' - ', '') or universidad_whed[i].lower() == universidad.replace('niversity', '').replace('university', '').replace('niversity', ' ').replace('university', ' ') or universidad_whed[i].replace('niversity', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad.replace('university', '').replace('university', '').replace('university', ' ').replace('university', ' ') or universidad_whed[i].replace('university', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad or universidad_whed[i].replace('at', ' ').replace('at', ' ').lower()  == universidad.replace('at', ' ') or universidad_whed[i].replace('college', ' ').replace('college ', ' ').lower()  == universidad.replace('college', ' ').replace('college ', ' ')  or universidad_whed[i].split('-')[0]  == universidad  or universidad_whed[i].split(' - ')[0]  == universidad  or universidad_whed[i].split(',')[0]  == universidad or universidad_whed[i].replace('the ','')  == universidad or universidad_whed[i].lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').replace('of ','').lower()  == universidad.replace('the ','').replace('of ','') or universidad_whed[i].split(' - ')[0].lower()   == universidad or universidad_whed[i].split('-')[0].lower()   == universidad or universidad_whed[i].split(',')[0].lower()   == universidad or universidad_whed[i].replace('the ','').lower()  == universidad:
                        return calle_whed[i]
            except:
                   return 'Unkwnown'
    else:
        return 'Unknown'


def getInst(universidad, universidad_whed, institucion_whed):
    if universidad != None:
        universidad = universidad.lower()
        for i in range(len(universidad_whed)):
            try:
                if universidad_whed[i] != None:
                    if universidad_whed[i].lower()  == universidad or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace(' - ', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace(' - ', ' ')  or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace(' - ', '').lower()  == universidad.replace('-', '') or universidad_whed[i].replace('-', '').lower()  == universidad.replace(' - ', '') or universidad_whed[i].lower() == universidad.replace('niversity', '').replace('university', '').replace('niversity', ' ').replace('university', ' ') or universidad_whed[i].replace('niversity', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad.replace('university', '').replace('university', '').replace('university', ' ').replace('university', ' ') or universidad_whed[i].replace('university', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad or universidad_whed[i].replace('at', ' ').replace('at', ' ').lower()  == universidad.replace('at', ' ') or universidad_whed[i].replace('college', ' ').replace('college ', ' ').lower()  == universidad.replace('college', ' ').replace('college ', ' ')  or universidad_whed[i].split('-')[0]  == universidad  or universidad_whed[i].split(' - ')[0]  == universidad  or universidad_whed[i].split(',')[0]  == universidad or universidad_whed[i].replace('the ','')  == universidad or universidad_whed[i].lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').replace('of ','').lower()  == universidad.replace('the ','').replace('of ','') or universidad_whed[i].split(' - ')[0].lower()   == universidad or universidad_whed[i].split('-')[0].lower()   == universidad or universidad_whed[i].split(',')[0].lower()   == universidad or universidad_whed[i].replace('the ','').lower()  == universidad:
                        return institucion_whed[i]
            except:
                   return 'Unkwnown'
    else:
        return 'Unknown'

def getDesc(universidad, universidad_whed, universidad_desc_whed):
    if universidad != None:
        universidad = universidad.lower()
        for i in range(len(universidad_whed)):
            try:
                if universidad_whed[i] != None:
                    if universidad_whed[i].lower()  == universidad or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace(' - ', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace('-', ' ').lower()  == universidad.replace(' - ', ' ')  or universidad_whed[i].replace(' - ', ' ').lower()  == universidad.replace('-', ' ') or universidad_whed[i].replace(' - ', '').lower()  == universidad.replace('-', '') or universidad_whed[i].replace('-', '').lower()  == universidad.replace(' - ', '') or universidad_whed[i].lower() == universidad.replace('niversity', '').replace('university', '').replace('niversity', ' ').replace('university', ' ') or universidad_whed[i].replace('niversity', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad.replace('university', '').replace('university', '').replace('university', ' ').replace('university', ' ') or universidad_whed[i].replace('university', '').replace('university', '').replace('University', ' ').replace('university', ' ').lower() == universidad or universidad_whed[i].replace('at', ' ').replace('at', ' ').lower()  == universidad.replace('at', ' ') or universidad_whed[i].replace('college', ' ').replace('college ', ' ').lower()  == universidad.replace('college', ' ').replace('college ', ' ')  or universidad_whed[i].split('-')[0]  == universidad  or universidad_whed[i].split(' - ')[0]  == universidad  or universidad_whed[i].split(',')[0]  == universidad or universidad_whed[i].replace('the ','')  == universidad or universidad_whed[i].lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').lower()  == universidad.replace('the ','') or universidad_whed[i].replace('the ','').replace('of ','').lower()  == universidad.replace('the ','').replace('of ','') or universidad_whed[i].split(' - ')[0].lower()   == universidad or universidad_whed[i].split('-')[0].lower()   == universidad or universidad_whed[i].split(',')[0].lower()   == universidad or universidad_whed[i].replace('the ','').lower()  == universidad:
                        return universidad_desc_whed[i]
            except:
                   return 'Unkwnown'
    else:
        return 'Unkwnown'

def getCleanYear(year):
    if type(year) == list:
        value = year[0]
        return value
    else:
        return year
    


    
def categoryUnique(categ):
    if categ != None:
        if len(categ) >= 1:
            categoria = set(categ)
            categoria = list(categoria)
            return categoria
    else:
        return 'Unknown'
    
    

#%%

'''
BACHILLER
'''



contenidofinal_bachiller =  []
        
count = 0
for cont in contenidos:
    count += 1
    print(count)
    dicc = {'Area'                    : getAreas(category, areas, cont['Titulo']),
            'Pais'                    : cont['Pais'],
            'Ciudad'                  : cont['Ciudad'],
            'Calles'                  : getCalles(cont['Universidad'], universidad_whed, calle_whed),
            'Institucion'             : getInst(cont['Universidad'], universidad_whed, institucion_whed),
            'Idioma'                  : getLang(cont['Universidad'],   universidad_whed, lenguaje_whed),
            'Subtitulos'              : None,
            'Calificacion'            : cont['Calificacion'],
            'Nivel'                   : cont['Nivel'],
            'Part Time'               : getCleanYear(cont['Duracion Parcial']),
            'Full Time'               : getCleanYear(cont['Duracion Full']),
            'Cursada'                 : cont['Cursada'],
            'Duracion'                : getCleanYear(getDuracion(cont['Duracion Parcial'], cont['Duracion Full'])),
            'Titulo'                  : cont['Titulo'],
            'Universidad'             : cont['Universidad'],
            'Descripcion Programa'    : cont['Descripcion'].replace('&nbsp;', ' '),
            'Descripcion Universidad' : getDesc(cont['Universidad'], universidad_whed, universidad_desc_whed),
            'Categoria'               : categoryUnique([category[i] for i in range(len(category)) if category[i] in cont['Titulo']]),
            'Deadline'                : None,
            'Requerimientos'          : None,
            'Tutition Free'           : getMatricula(cont['Matricula'],  cont['Moneda Matricula'] , cont['Unidad Matricula'] ),
            'Valoracones'             : None,
            'Link University'         : getUniversity(cont['Universidad'],universidad_whed ,link_universidad_whed ),
            'logo'                    : cont['Logo'],
            'Multimedia'              : None
            }

    contenidofinal_bachiller.append(dicc)



clean_bachiller = []
for conte in contenidofinal_bachiller:
    if len(conte['Area']) >= 1:
        print('\n')
        print(conte['Area'])
        print(conte['Categoria'])
        print('\n')
        clean_bachiller.append(conte)
        


with open('bachiller.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(clean_bachiller, archivo_json, ensure_ascii=False, indent = 2)
    
    


'''
DISTANCIA
'''



contenidofinal_distancia =  []
contador = 0
for cont in contenidos_distance:
    dicc = {'Area'                      : getAreas(category, areas,  cont['Titulo']),
            'Pais'                      : cont['Pais'],
            'Ciudad'                    : cont['Ciudad'],
            'Calles'                    : getCalles(cont['Universidad'], universidad_whed, calle_whed),
            'Institucion'               : getInst(cont['Universidad'], universidad_whed, institucion_whed),
            'Idioma'                    : getLang(cont['Universidad'], universidad_whed, lenguaje_whed),
            'Subtitulos'                : None,
            'Calificacion'              : cont['Calificacion'],
            'Nivel'                     : cont['Nivel'],
            'Part Time'                 : getCleanYear(cont['Duracion Parcial']),
            'Full Time'                 : getCleanYear(cont['Duracion Full']),
            'Cursada'                   : cont['Cursada'],
            'Duracion'                  : getCleanYear(getDuracion(cont['Duracion Parcial'], cont['Duracion Full'])),
            'Titulo'                    : cont['Titulo'],
            'Universidad'               : cont['Universidad'],
            'Descripcion Programa'      : cont['Descripcion'].replace('&nbsp;', ' '),
            'Descripcion Universidad'   : getDesc(cont['Universidad'], universidad_whed, universidad_desc_whed),
            'Categoria'                 : categoryUnique([category[i] for i in range(len(category)) if category[i] in cont['Titulo']]),
            'Deadline'                  : None,
            'Requerimientos'            : None,
            'Tutition Free'             : getMatricula(cont['Matricula'],  cont['Moneda Matricula'] , cont['Unidad Matricula'] ),
            'Valoracones'               : None,
            'Link University'           :  getUniversity(cont['Universidad'],universidad_whed ,link_universidad_whed ),
            'logo'                      : cont['Logo'],
            'Multimedia'                : None
            }
    
            
    contenidofinal_distancia.append(dicc)
    contador += 1
    print(contador)

        


clean_distance = []
for conte in contenidofinal_distancia:
    if len(conte['Area']) >= 1:
        print('\n')
        print(conte['Area'])
        print(conte['Categoria'])
        print('\n')
        clean_distance.append(conte)
        

with open('distance.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(clean_distance, archivo_json, ensure_ascii=False, indent = 2)


'''
PHD
'''




contenidofinal_phd =  []
contador = 0
for cont in contenidos_phd:
    dicc = {'Area'                    : getAreas(category, areas,  cont['Titulo']),
            'Pais'                    : cont['Pais'],
            'Ciudad'                  : cont['Ciudad'],
            'Calles'                  : getCalles(cont['Universidad'], universidad_whed, calle_whed),
            'Institucion'             : getInst(cont['Universidad'], universidad_whed, institucion_whed),
            'Idioma'                  : getLang(cont['Universidad'],   universidad_whed, lenguaje_whed),
            'Subtitulos'              : None,
            'Calificacion'            : cont['Calificacion'],
            'Nivel'                   : cont['Nivel'],
            'Part Time'               : getCleanYear(cont['Duracion Parcial']),
            'Full Time'               : getCleanYear(cont['Duracion Full']),
            'Cursada'                 : cont['Cursada'],
            'Duracion'                : getCleanYear(getDuracion(cont['Duracion Parcial'], cont['Duracion Full'])),
            'Titulo'                  : cont['Titulo'],
            'Universidad'             : cont['Universidad'],
            'Descripcion Programa'    : cont['Descripcion'].replace('&nbsp;', ' '),
            'Descripcion Universidad' : getDesc(cont['Universidad'], universidad_whed, universidad_desc_whed),
            'Categoria'               : categoryUnique([category[i] for i in range(len(category)) if category[i] in cont['Titulo']]),
            'Deadline'                : None,
            'Requerimientos'          : None,
            'Tutition Free'           : getMatricula(cont['Matricula'],  cont['Moneda Matricula'] , cont['Unidad Matricula'] ),
            'Valoracones'             : None,
            'Link University'         : getUniversity(cont['Universidad'],universidad_whed ,link_universidad_whed ),
            'logo'                    : cont['Logo'],
            'Multimedia'              : None
            }
    
    contenidofinal_phd.append(dicc)
    contador += 1
    print(contador)
        


clean_phd = []
for conte in contenidofinal_phd:
    if len(conte['Area']) >= 1:
        print('\n')
        print(conte['Area'])
        print(conte['Categoria'])
        print('\n')
        clean_phd.append(conte)
        


with open('phd.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(clean_phd, archivo_json, ensure_ascii=False, indent = 2)





'''
MASTER
'''


contenidofinal_master =  []
contador = 0    
for cont in contenidos_master:
    dicc = {'Area'                    : getAreas(category, areas,  cont['Titulo']),
            'Pais'                    : cont['Pais'],
            'Ciudad'                  : cont['Ciudad'],
            'Calles'                  : getCalles(cont['Universidad'], universidad_whed, calle_whed),
            'Institucion'             : getInst(cont['Universidad'], universidad_whed, institucion_whed),
            'Idioma'                  : getLang(cont['Universidad'],   universidad_whed, lenguaje_whed),
            'Subtitulos'              : None,
            'Calificacion'            : cont['Calificacion'],
            'Nivel'                   : cont['Nivel'],
            'Part Time'               : getCleanYear(cont['Duracion Parcial']),
            'Full Time'               : getCleanYear(cont['Duracion Full']),
            'Cursada'                 : cont['Cursada'],
            'Duracion'                : getCleanYear(getDuracion(cont['Duracion Parcial'], cont['Duracion Full'])),
            'Titulo'                  : cont['Titulo'],
            'Universidad'             : cont['Universidad'],
            'Descripcion Programa'    : cont['Descripcion'].replace('&nbsp;', ' '),
            'Descripcion Universidad' : getDesc(cont['Universidad'], universidad_whed, universidad_desc_whed),
            'Categoria'               : categoryUnique([category[i] for i in range(len(category)) if category[i] in cont['Titulo']]),
            'Deadline'                : None,
            'Requerimientos'          : None,
            'Tutition Free'           : getMatricula(cont['Matricula'],  cont['Moneda Matricula'] , cont['Unidad Matricula'] ),
            'Valoracones'             : None,
            'Link University'         : getUniversity(cont['Universidad'],universidad_whed ,link_universidad_whed ),
            'logo'                    : cont['Logo'],
            'Multimedia'              : None
            }
    
    contenidofinal_master.append(dicc)
    contador += 1
    print(contador)


clean_master = []
for conte in contenidofinal_master:
    if len(conte['Area']) >= 1:
        print('\n')
        print(conte['Area'])
        print(conte['Categoria'])
        print('\n')
        clean_master.append(conte)
        


with open('master.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(clean_master, archivo_json, ensure_ascii=False, indent = 2)





'''
SHORT
'''


contenidofinal_short =  []
contador = 0    
for cont in contenidos_short:
    dicc = {'Area'                    : getAreas(category, areas,  cont['Titulo']),
            'Pais'                    : cont['Pais'],
            'Ciudad'                  : cont['Ciudad'],
            'Calles'                  : getCalles(cont['Universidad'], universidad_whed, calle_whed),
            'Institucion'             : getInst(cont['Universidad'], universidad_whed, institucion_whed),
            'Idioma'                  : getLang(cont['Universidad'],   universidad_whed, lenguaje_whed),
            'Subtitulos'              : None,
            'Calificacion'            : cont['Calificacion'],
            'Nivel'                   : cont['Nivel'],
            'Part Time'               : getCleanYear(cont['Duracion Parcial']),
            'Full Time'               : getCleanYear(cont['Duracion Full']),
            'Cursada'                 : cont['Cursada'],
            'Duracion'                : getCleanYear(getDuracion(cont['Duracion Parcial'], cont['Duracion Full'])),
            'Titulo'                  : cont['Titulo'],
            'Universidad'             : cont['Universidad'],
            'Descripcion Programa'    : cont['Descripcion'].replace('&nbsp;', ' '),
            'Descripcion Universidad' : getDesc(cont['Universidad'], universidad_whed, universidad_desc_whed),
            'Categoria'               : categoryUnique([category[i] for i in range(len(category)) if category[i] in cont['Titulo']]),
            'Deadline'                : None,
            'Requerimientos'          : None,
            'Tutition Free'           : getMatricula(cont['Matricula'],  cont['Moneda Matricula'] , cont['Unidad Matricula'] ),
            'Valoracones'             : None,
            'Link University'         : getUniversity(cont['Universidad'],universidad_whed ,link_universidad_whed ),
            'logo'                    : cont['Logo'],
            'Multimedia'              : None
            }
    
    contenidofinal_short.append(dicc)
    contador += 1
    print(contador)


clean_short = []
for conte in contenidofinal_short:
    if len(conte['Area']) >= 1:
        print('\n')
        print(conte['Area'])
        print(conte['Categoria'])
        print('\n')
        clean_short.append(conte)
        


with open('short.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(clean_short, archivo_json, ensure_ascii=False, indent = 2)
        
    
    



'''
WHED
'''




contenidofinal_whed =  []
contador = 0     
for cont in whed:
    dicc = {'Area'                     : cont['Area'],
            'Pais'                     : cont['Pais'],
            'Ciudad'                   : cont['Ciudad'],
            'Calles'                   : cont['Calles'],
            'Institucion'              : cont['Institucion'],
            'Idioma'                   : cont['Idioma'],
            'Subtitulos'               : cont['Subtitulos'],
            'Calificacion'             : cont['Calificacion'],
            'Nivel'                    : cont['Nivel'],
            'Part Time'                : None,
            'Full Time'                : None,
            'Cursada'                  : cont['Cursada'],
            'Duracion'                 : cont['Duracion'],
            'Titulo'                   : cont['Titulo'],
            'Universidad'              : cont['Universidad'],
            'Descripcion Programa'     : None,
            'Descripcion Universidad'  : cont['Descripcion Universidad'],
            'Categoria'                : cont['Categoria'],
            'Deadline'                 : cont['Deadline'],
            'Requerimientos'           : cont['Requerimientos'],
            'Tutition Free'            : None,
            'Valoracones'              : cont['Valoracones'],
            'Link University'          : cont['Link University'],
            'logo'                     : cont['logo'],
            'Multimedia'               : cont['Multimedia']

            }
            
    contenidofinal_whed.append(dicc)
    contador += 1
    print(contador)
    
    
with open('whedfinal.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(contenidofinal_whed, archivo_json, ensure_ascii=False, indent = 2)
        
    
    
#%%

def getTe(area, categoria):
    try:
        if categoria[0] == 'Technology':
            return 'TECH'
        else:
            return area
    except:
        return None


areas = ['ARTS',
 'BUSINESS',
 'DATA',
 'DESIGN',
 'MARKETING',
 'PRODUCT',
 'SOFT SKILLS',
 'TECH',
 'sOFT SKILLS']


whed          = json.load(open('whedfinal.json', encoding='utf-8'))

bachiller     = json.load(open('bachiller.json', encoding='utf-8'))

distance      = json.load(open('distance.json', encoding='utf-8'))

phd           = json.load(open('phd.json', encoding='utf-8'))

short         = json.load(open('short.json', encoding='utf-8'))

master        = json.load(open('master.json', encoding='utf-8'))



'''
STUDY LEVELS
'''


consolidado = master + short + phd + distance + bachiller

with open('consolidado.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(consolidado, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('consolidado.json')
df.to_excel('consolidado.xlsx')






'''
ARTS
'''


all_arts = []

for i in range(len(consolidado)):
    areas = consolidado[i]['Area']
    for ar in areas:
        if ar == 'ARTS':
            dicc = {'Area'                     : 'ARTS',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_arts.append(dicc)

            

with open('all_arts.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_arts, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_arts.json')
df.to_excel('all_arts.xlsx')







'''
BUSINESS
'''


all_business= []


for i in range(len(consolidado)):
    business = consolidado[i]['Area']
    for bus in business:
        if bus == 'BUSINESS':
            dicc = {'Area'                     : 'BUSINESS',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_business.append(dicc)


with open('all_business.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_business, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_business.json')
df.to_excel('all_business.xlsx')



'''
DATA
'''



all_data = []

for i in range(len(consolidado)):
    data = consolidado[i]['Area']
    for dat in data:
        if dat == 'DATA':
            dicc = {'Area'                     : 'DATA',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_data.append(dicc)



with open('all_data.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_data, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_data.json')
df.to_excel('all_data.xlsx')



'''
DESIGN
'''



all_design = []

for i in range(len(consolidado)):
    design = consolidado[i]['Area']
    for des in design:
        if des == 'DESIGN':
            dicc = {'Area'                     : 'DESIGN',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_design.append(dicc)



with open('all_design.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_design, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_design.json')
df.to_excel('all_design.xlsx')




'''
MARKETING
'''


all_marketing = []

for i in range(len(consolidado)):
    market = consolidado[i]['Area']
    for mar in market:
        if mar == 'MARKETING':
            dicc = {'Area'                     : 'MARKETING',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_marketing.append(dicc)



with open('all_marketing.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_marketing, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_marketing.json')
df.to_excel('all_marketing.xlsx')




'''
PRODUCT
'''



all_product = []

for i in range(len(consolidado)):
    product = consolidado[i]['Area']
    for prod in product:
        if prod == 'PRODUCT':
            dicc = {'Area'                     : 'PRODUCT',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_product.append(dicc)


with open('all_product.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_product, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_product.json')
df.to_excel('all_product.xlsx')




'''
TECH
'''



all_tech = []

for i in range(len(consolidado)):
    tech = consolidado[i]['Area']
    for te in tech:
        if te == 'TECH':
            dicc = {'Area'                     : 'TECH',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_tech.append(dicc)


with open('all_tech.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_tech, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_tech.json')
df.to_excel('all_tech.xlsx')




'''
SOFT SKILLS
'''


all_soft = []

for i in range(len(consolidado)):
    sotfskills = consolidado[i]['Area']
    for soft in sotfskills:
        if soft == 'SOFT SKILLS':
            dicc = {'Area'                     : 'SOFT SKILLS',
                    'Pais'                     : consolidado[i]['Pais'],
                    'Ciudad'                   : consolidado[i]['Ciudad'],
                    'Calles'                   : consolidado[i]['Calles'],
                    'Institucion'              : consolidado[i]['Institucion'],
                    'Idioma'                   : consolidado[i]['Idioma'],
                    'Subtitulos'               : consolidado[i]['Subtitulos'],
                    'Calificacion'             : consolidado[i]['Calificacion'],
                    'Nivel'                    : consolidado[i]['Nivel'],
                    'Part Time'                : consolidado[i]['Part Time'],
                    'Full Time'                : consolidado[i]['Full Time'],
                    'Cursada'                  : consolidado[i]['Cursada'],
                    'Duracion'                 : consolidado[i]['Duracion'],
                    'Titulo'                   : consolidado[i]['Titulo'],
                    'Universidad'              : consolidado[i]['Universidad'],
                    'Descripcion Programa'     : consolidado[i]['Descripcion Programa'],
                    'Descripcion Universidad'  : consolidado[i]['Descripcion Universidad'],
                    'Categoria'                : consolidado[i]['Categoria'],
                    'Deadline'                 : consolidado[i]['Deadline'],
                    'Requerimientos'           : consolidado[i]['Requerimientos'],
                    'Tutition Free'            : consolidado[i]['Tutition Free'],
                    'Valoracones'              : consolidado[i]['Valoracones'],
                    'Link University'          : consolidado[i]['Link University'],
                    'logo'                     : consolidado[i]['logo'],
                    'Multimedia'               : consolidado[i]['Multimedia']

                    }
                    
            all_soft.append(dicc)



with open('all_soft.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(all_soft, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('all_soft.json')
df.to_excel('all_soft.xlsx')



#%%


programas    = json.load(open('consolidado.json', encoding='utf-8'))


lista_niveles = []


for i in range(len(consolidado)):
    lista_niveles.append(consolidado[i]['Nivel'])

lista_final = set(lista_niveles)
lista_niveles = list(lista_final)


# ['phd', 'short', 'master', 'bachelor']

#%%

bachelor = []

for i in range(len(consolidado)):
    if consolidado[i]['Nivel'] == 'bachelor':
        bachelor.append(consolidado[i])

    

with open('bachelor.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(bachelor, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('bachelor.json')
df.to_excel('bachelor.xlsx')








master = []

for i in range(len(consolidado)):
    if consolidado[i]['Nivel'] == 'master':
        master.append(consolidado[i])

    

with open('master.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(master, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('master.json')
df.to_excel('master.xlsx')





short = []

for i in range(len(consolidado)):
    if consolidado[i]['Nivel'] == 'short':
        short.append(consolidado[i])

    

with open('short.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(short, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('short.json')
df.to_excel('short.xlsx')






phd = []

for i in range(len(consolidado)):
    if consolidado[i]['Nivel'] == 'phd':
        phd.append(consolidado[i])

    

with open('phd.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(phd, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('phd.json')
df.to_excel('phd.xlsx')



#%%


import json
import pprint
import pandas as pd



distance   = json.load(open('whedfinal.json', encoding='utf-8'))


dicc_country = {'United States': 'North America',
 'Germany': 'Europe',
 'United Kingdom': 'Europe',
 'India': 'Asia',
 'Turkey': 'Asia',
 'France': 'Europe',
 'United Arab Emirates': 'Asia',
 'Belgium': 'Europe',
 'South Africa': 'Africa',
 'Ireland': 'Europe',
 'Australia': 'Oceania',
 'New Zealand': 'Oceania',
 'Canada': 'North America',
 'Spain': 'Europe',
 'Malta': 'Europe',
 'Italy': 'Europe',
 'Slovakia': 'Europe',
 'Denmark': 'Europe',
 'Greece': 'Europe',
 'Latvia': 'Europe',
 'China': 'Asia',
 'Pakistan': 'Asia',
 'Taiwan': 'Asia',
 'Thailand': 'Asia',
 'Malaysia': 'Asia',
 'Sweden': 'Europe',
 'Georgia': 'Asia',
 'Lithuania': 'Europe',
 'Niger': 'Africa',
 'Switzerland': 'Europe',
 'Austria': 'Europe',
 'Singapore': 'Asia',
 'Netherlands': 'Europe',
 'Estonia': 'Europe',
 'Hong Kong (SAR)': 'Asia',
 'Luxembourg': 'Europe',
 'Uganda': 'Africa',
 'Japan': 'Asia',
 'South Korea': 'Asia',
 'Czech Republic': 'Europe',
 'Norway': 'Europe',
 'Croatia': 'Europe',
 'Saudi Arabia': 'Asia',
 'Kazakhstan': 'Asia',
 'Namibia': 'Africa',
 'Nepal': 'Asia',
 'Poland': 'Europe',
 'Portugal': 'Europe',
 'Hungary': 'Europe',
 'Jamaica': 'North America',
 'Finland': 'Europe',
 'Northern Cyprus': 'Asia',
 'Russia': 'Europe',
 'Cayman Islands': 'North America',
 'Nicaragua': 'North America',
 'Iceland': 'Europe',
 'Indonesia': 'Asia',
 'Barbados': 'North America',
 'Vietnam': 'Asia',
 'Iran': 'Asia',
 'Cyprus': 'Asia',
 'Mauritius': 'Africa',
 'Philippines': 'Asia',
 'Jordan': 'Asia',
 'Romania': 'Europe',
 'Guam': 'Oceania',
 'Kenya': 'Africa',
 'Macedonia (FYROM)': 'Europe',
 'Palestinian Territory, Occupied': 'Asia',
 'Sri Lanka': 'Asia',
 'Israel': 'Asia',
 'Bahrain': 'Asia',
 'Egypt': 'Africa',
 'Qatar': 'Asia',
 'Azerbaijan': 'Asia',
 'Slovenia': 'Europe',
 'Ukraine': 'Europe',
 'Macao (SAR)': 'Asia',
 'Albania': 'Europe',
 'Nigeria': 'Africa',
 'Lebanon': 'Asia',
 'Bulgaria': 'Europe',
 'Puerto Rico': 'North America',
 'Bangladesh': 'Asia',
 'United States Virgin Islands': 'North America',
 'Mexico': 'North America',
 'Oman': 'Asia',
 'Ethiopia': 'Africa',
 'Monaco': 'Europe',
 'Bosnia and Herzegovina': 'Europe',
 'Brazil': 'South America',
 'Armenia': 'Asia',
 'Rwanda': 'Africa',
 'Kyrgyzstan': 'Asia',
 'Liechtenstein': 'Europe',
 'Ghana': 'Africa',
 'Grenada': 'North America',
 'Argentina': 'South America',
 'Serbia': 'Europe',
 'Belize': 'North America',
 'Trinidad and Tobago': 'North America',
 'Curaçao': 'North America',
 'Aruba': 'North America'}


def edit_continent(function, universidad):
    try:
        if universidad != None:
            if universidad.lower() == 'coursera' or universidad.lower() == 'udemy':
                regreso = 'Anywhere'
            else:
                regreso = function
            return regreso
        elif universidad == None and function != None:
            return function
    except:
        return function


def edit_country(country, universidad):
    try:
        if universidad != None:
            if universidad.lower() == 'coursera' or universidad.lower() == 'udemy':
                regreso = 'Anywhere'
            else:
                regreso = country
            return regreso
        elif universidad == None and country != None:
            return country
    except:
        return country


dis_final = []


for con in distance:

    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         [con['Idioma']],
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      None,
        "PropertyID":      None,
        "PartTime ":       None,
        "FullTime ":       None,
        "AtYourOwnPace":   None,
        "Modality":          None,
        "Attendence":       None,
        "ProgramDuration":None,
        "Duration":        None,
        
        "Title":            con['Titulo'],
         "University":       con['Universidad'],
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :con['Link University'],
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    dis_final.append(dicc)
    
    
    

with open('whed_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(dis_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('whed_final.json')
df.to_excel('whed_final.xlsx')



#%%



import json
import pprint
import pandas as pd


dicc_country = {'United States': 'North America',
 'Germany': 'Europe',
 'United Kingdom': 'Europe',
 'India': 'Asia',
 'Turkey': 'Asia',
 'France': 'Europe',
 'United Arab Emirates': 'Asia',
 'Belgium': 'Europe',
 'South Africa': 'Africa',
 'Ireland': 'Europe',
 'Australia': 'Oceania',
 'New Zealand': 'Oceania',
 'Canada': 'North America',
 'Spain': 'Europe',
 'Malta': 'Europe',
 'Italy': 'Europe',
 'Slovakia': 'Europe',
 'Denmark': 'Europe',
 'Greece': 'Europe',
 'Latvia': 'Europe',
 'China': 'Asia',
 'Pakistan': 'Asia',
 'Taiwan': 'Asia',
 'Thailand': 'Asia',
 'Malaysia': 'Asia',
 'Sweden': 'Europe',
 'Georgia': 'Asia',
 'Lithuania': 'Europe',
 'Niger': 'Africa',
 'Switzerland': 'Europe',
 'Austria': 'Europe',
 'Singapore': 'Asia',
 'Netherlands': 'Europe',
 'Estonia': 'Europe',
 'Hong Kong (SAR)': 'Asia',
 'Luxembourg': 'Europe',
 'Uganda': 'Africa',
 'Japan': 'Asia',
 'South Korea': 'Asia',
 'Czech Republic': 'Europe',
 'Norway': 'Europe',
 'Croatia': 'Europe',
 'Saudi Arabia': 'Asia',
 'Kazakhstan': 'Asia',
 'Namibia': 'Africa',
 'Nepal': 'Asia',
 'Poland': 'Europe',
 'Portugal': 'Europe',
 'Hungary': 'Europe',
 'Jamaica': 'North America',
 'Finland': 'Europe',
 'Northern Cyprus': 'Asia',
 'Russia': 'Europe',
 'Cayman Islands': 'North America',
 'Nicaragua': 'North America',
 'Iceland': 'Europe',
 'Indonesia': 'Asia',
 'Barbados': 'North America',
 'Vietnam': 'Asia',
 'Iran': 'Asia',
 'Cyprus': 'Asia',
 'Mauritius': 'Africa',
 'Philippines': 'Asia',
 'Jordan': 'Asia',
 'Romania': 'Europe',
 'Guam': 'Oceania',
 'Kenya': 'Africa',
 'Macedonia (FYROM)': 'Europe',
 'Palestinian Territory, Occupied': 'Asia',
 'Sri Lanka': 'Asia',
 'Israel': 'Asia',
 'Bahrain': 'Asia',
 'Egypt': 'Africa',
 'Qatar': 'Asia',
 'Azerbaijan': 'Asia',
 'Slovenia': 'Europe',
 'Ukraine': 'Europe',
 'Macao (SAR)': 'Asia',
 'Albania': 'Europe',
 'Nigeria': 'Africa',
 'Lebanon': 'Asia',
 'Bulgaria': 'Europe',
 'Puerto Rico': 'North America',
 'Bangladesh': 'Asia',
 'United States Virgin Islands': 'North America',
 'Mexico': 'North America',
 'Oman': 'Asia',
 'Ethiopia': 'Africa',
 'Monaco': 'Europe',
 'Bosnia and Herzegovina': 'Europe',
 'Brazil': 'South America',
 'Armenia': 'Asia',
 'Rwanda': 'Africa',
 'Kyrgyzstan': 'Asia',
 'Liechtenstein': 'Europe',
 'Ghana': 'Africa',
 'Grenada': 'North America',
 'Argentina': 'South America',
 'Serbia': 'Europe',
 'Belize': 'North America',
 'Trinidad and Tobago': 'North America',
 'Curaçao': 'North America',
 'Aruba': 'North America'}




data   = json.load(open('all_data.json', encoding='utf-8'))

data.sort(key=lambda s: s['Nivel'])



arts   = json.load(open('all_arts.json', encoding='utf-8'))

arts.sort(key=lambda s: s['Nivel'])



business   = json.load(open('all_business.json', encoding='utf-8'))

business.sort(key=lambda s: s['Nivel'])



design   = json.load(open('all_design.json', encoding='utf-8'))

design.sort(key=lambda s: s['Nivel'])



marketing   = json.load(open('all_marketing.json', encoding='utf-8'))

marketing.sort(key=lambda s: s['Nivel'])



product   = json.load(open('all_product.json', encoding='utf-8'))

product.sort(key=lambda s: s['Nivel'])



soft   = json.load(open('all_soft.json', encoding='utf-8'))

soft.sort(key=lambda s: s['Nivel'])



tech   = json.load(open('all_tech.json', encoding='utf-8'))

tech.sort(key=lambda s: s['Nivel'])



bachelor   = json.load(open('bachelor.json', encoding='utf-8'))

bachelor.sort(key=lambda s: s['Nivel'])



distance   = json.load(open('distance.json', encoding='utf-8'))

distance.sort(key=lambda s: s['Nivel'])



master   = json.load(open('master.json', encoding='utf-8'))

master.sort(key=lambda s: s['Nivel'])



phd   = json.load(open('phd.json', encoding='utf-8'))

phd.sort(key=lambda s: s['Nivel'])


short   = json.load(open('short.json', encoding='utf-8'))

short.sort(key=lambda s: s['Nivel'])





def replace_nivel(nivel):
    if nivel == 'short':
        return 'Course'
    else:
        return nivel.title()


def get_languag(lang):
    lista_lang = []
    if lang != None and lang != '':
        lang_sep = lang.split(';')
        for i in range(len(lang_sep)):
            lista_lang.append(lang_sep[i])
        return lista_lang
    else:
        return None
        

    
    
def modality(part, full, at_your):
    try:
        if part != 'Unknown' and full != 'Unknown' and at_your == None:
            resultado = ['Full Time', 'Part Time']
        elif part != 'Unknown' and full == 'Unknown' and at_your == None:
            resultado = ['Part Time']
        elif part == 'Unknown' and full != 'Unknown'and at_your == None:
            resultado = ['Full Time']
        elif part == 'Unknown' and full != 'Unknown'and at_your != None:
            resultado = ['Full Time', 'At Your Own Pace']
        elif part != 'Unknown' and full == 'Unknown'and at_your != None:
            resultado = ['Part Time', 'At Your Own Pace']
        elif part == 'Unknown' and full == 'Unknown'and at_your != None:
            resultado = ['At Your Own Pace']
        elif part != 'Unknown' and full != 'Unknown'and at_your != None:
            resultado = ['Full Time', 'Part Time', 'At Your Own Pace']
        return resultado
    except:
        return 'Unknown'
    
    

    
def complete_links(university, link):
    try:
        if university != None:
            if university.lower() == 'coursera':
                regreso = 'https://www.coursera.org/'
            elif university.lower() == 'udemy':
                regreso = 'https://www.udemy.com/'
            else:
                regreso = link
            return regreso
    except:
        return None
        



def get_duration(duracion):
    try:
        if duracion != 'Unknown':
            duracion_sep = duracion.split()
            if len(duracion_sep) == 2 and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                if int(duracion_sep[0]) == 1:
                    regreso = '1 month or less'
                elif int(duracion_sep[0]) > 1 and int(duracion_sep[0]) <= 6:
                    regreso = '6 months or less'
                elif int(duracion_sep[0]) > 6 and int(duracion_sep[0]) <= 11:
                    regreso = 'less than a year'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'years' and int(duracion_sep[0]) > 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'years' and int(duracion_sep[0]) == 1:
                regreso = '1 year'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'years' and int(duracion_sep[0]) <= 4:
                regreso = duracion
            elif len(duracion_sep) == 5 and int(duracion_sep[0]) > 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 5 and int(duracion_sep[0]) == 1:
                regreso = '1 year'
            elif len(duracion_sep) == 5 and int(duracion_sep[0]) == 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                regreso = 'less than a year'
            elif len(duracion_sep) == 5 and duracion_sep[1] == 'years' and int(duracion_sep[0]) >= 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 5 and duracion_sep[1] == 'years' and int(duracion_sep[0]) <= 3:
                regreso = str(duracion_sep[0]) + ' ' + 'years'
            elif len(duracion_sep) == 2 and int(duracion_sep[0]) <= 6  and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                regreso = '6 months or less'
            elif len(duracion_sep) == 2 and int(duracion_sep[0]) <= 11  and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                regreso = 'less than a year'
            return regreso
        else:
            return duracion
    except:
        return 'Unknown'
    
def get_program_duration(duracion, full, part):
    elemento_final = []
    lista = [duracion, full, part]
    for i in range(len(lista)):
        if lista[i] != 'Unknown':
            elemento_final.append(lista[i])
            break
    if len(elemento_final) == 1:
        return elemento_final[0]
    else:
        return 'Unknown'



acumulate     = []
acumulatedos  = []
acumulatetres = []
    


def get_code(area, degree,  count, acumulate):
    ceros = '000000'
    if degree[0:2].upper()   == 'BA':
            suma_ba = str(i)
            value = degree[0:2].upper() + '_' + ceros[:-len(suma_ba)] + suma_ba + '_' + area
            acumulate.append(i)
            return value
    elif degree[0:2].upper() == 'MA':
            suma_ma = str(i - len(acumulate)) 
            value = degree[0:2].upper() + '_' + ceros[:-len(suma_ma)] + suma_ma + '_' + area
            acumulatedos.append(i)
            return value
    elif degree[0:2].upper() == 'PH':
            suma_ph = str(i - len(acumulate) - len(acumulatedos) )
            value = degree[0:2].upper() + '_' + ceros[:-len(suma_ph)] +  suma_ph + '_' + area
            acumulatetres.append(i)
            return value
    elif degree[0:2].upper() == 'SH' or degree[0:2].upper() == 'CO':
            suma_co = str(i - len(acumulate) - len(acumulatedos) - len(acumulatetres) )
            value = degree[0:2].upper() + '_'  + ceros[:-len(suma_co)] +  suma_co + '_' + area
            return value
    else:
        return None


def edit_continent(function, universidad):
    try:
        if universidad != None:
            if universidad.lower() == 'coursera' or universidad.lower() == 'udemy':
                regreso = 'Anywhere'
            else:
                regreso = function
            return regreso
        elif universidad == None and function != None:
            return function
    except:
        return function
            

def edit_country(country, universidad):
    try:
        if universidad != None:
            if universidad.lower() == 'coursera' or universidad.lower() == 'udemy':
                regreso = 'Anywhere'
            else:
                regreso = country
            return regreso
        elif universidad == None and country != None:
            return country
    except:
        return country



def your_place(universidad, duracion_programa):
    try:
        if universidad != None:
            if 'coursera' == universidad.lower() or 'udemy' == universidad.lower():
                regreso = duracion_programa
            else:
                regreso = None
            return regreso
    except:
        return None



def your_place_none(at_your, full_part):
    if at_your != None:
        regreso = None
    else:
        regreso = full_part
    return regreso


def replace_university(university):
    if university == None:
        regreso = 'Unknown'
        return regreso
    else:
        return university



data_final = []

i = 0
for con in data:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
        "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    data_final.append(dicc)
    
    
    

with open('data.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(data_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('data.json')
df.to_excel('data.xlsx')




###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

arts_final = []

i = 0
for con in arts:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    arts_final.append(dicc)
    
    
    

with open('arts.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(arts_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('arts.json')
df.to_excel('arts.xlsx')


###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

business_final = []

i = 0
for con in business:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    business_final.append(dicc)
    
    
    

with open('business.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(business_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('business.json')
df.to_excel('business.xlsx')




###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

design_final = []

i = 0
for con in design:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    design_final.append(dicc)
    
    
    

with open('design.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(design_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('design.json')
df.to_excel('design.xlsx')



###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

marketing_final = []

i = 0
for con in marketing:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    marketing_final.append(dicc)
    
    
    

with open('marketing.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(marketing_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('marketing.json')
df.to_excel('marketing.xlsx')


###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

product_final = []

i = 0
for con in product:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    product_final.append(dicc)
    
    
    

with open('product.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(product_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('product.json')
df.to_excel('product.xlsx')



###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

soft_final = []

i = 0
for con in soft:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    soft_final.append(dicc)
    
    
    

with open('soft.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(soft_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('soft.json')
df.to_excel('soft.xlsx')



###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

tech_final = []

i = 0
for con in tech:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    tech_final.append(dicc)
    
    
    

with open('tech.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(tech_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('tech.json')
df.to_excel('tech.xlsx')






###########################################################################################



consolidado_final   = json.load(open('consolidado.json', encoding='utf-8'))


con_final = []

i = 0
for con in consolidado_final:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    con_final.append(dicc)
    
    
    

with open('consolidado_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(con_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('consolidado_final.json')
df.to_excel('consolidado_final.xlsx')



###########################################################################################


niveles = tech_final + soft_final +product_final + marketing_final + design_final + business_final + arts_final + data_final



bachelor_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Bachelor':
        bachelor_final.append(niveles[i])

    

with open('bachelor_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(bachelor_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('bachelor_final.json')
df.to_excel('bachelor_final.xlsx')








master_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Master':
        master_final.append(niveles[i])

    

with open('master_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(master_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('master_final.json')
df.to_excel('master_final.xlsx')





course_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Course':
        course_final.append(niveles[i])

    

with open('course_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(course_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('course_final.json')
df.to_excel('course_final.xlsx')






phd_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Phd':
        phd_final.append(niveles[i])

    

with open('phd_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(phd_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('phd_final.json')
df.to_excel('phd_final.xlsx')




##################################################
#      Distance


def distance_level(level):
    if len(level) >= 2:
        regreso = level[0]
        return [regreso]
    else:
        return level


distance   = json.load(open('distance.json', encoding='utf-8'))

distance.sort(key=lambda s: s['Nivel'])




acumulate     = []
acumulatedos  = []
acumulatetres = []



dis_final = []

i = 0
for con in distance:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             distance_level(con['Area']),
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'][0], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    dis_final.append(dicc)
    
    
    

with open('distance_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(dis_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('distance_final.json')
df.to_excel('distance_final.xlsx')


#%%

import json
import pprint
import pandas as pd


dicc_country = {'United States': 'North America',
 'Germany': 'Europe',
 'United Kingdom': 'Europe',
 'India': 'Asia',
 'Turkey': 'Asia',
 'France': 'Europe',
 'United Arab Emirates': 'Asia',
 'Belgium': 'Europe',
 'South Africa': 'Africa',
 'Ireland': 'Europe',
 'Australia': 'Oceania',
 'New Zealand': 'Oceania',
 'Canada': 'North America',
 'Spain': 'Europe',
 'Malta': 'Europe',
 'Italy': 'Europe',
 'Slovakia': 'Europe',
 'Denmark': 'Europe',
 'Greece': 'Europe',
 'Latvia': 'Europe',
 'China': 'Asia',
 'Pakistan': 'Asia',
 'Taiwan': 'Asia',
 'Thailand': 'Asia',
 'Malaysia': 'Asia',
 'Sweden': 'Europe',
 'Georgia': 'Asia',
 'Lithuania': 'Europe',
 'Niger': 'Africa',
 'Switzerland': 'Europe',
 'Austria': 'Europe',
 'Singapore': 'Asia',
 'Netherlands': 'Europe',
 'Estonia': 'Europe',
 'Hong Kong (SAR)': 'Asia',
 'Luxembourg': 'Europe',
 'Uganda': 'Africa',
 'Japan': 'Asia',
 'South Korea': 'Asia',
 'Czech Republic': 'Europe',
 'Norway': 'Europe',
 'Croatia': 'Europe',
 'Saudi Arabia': 'Asia',
 'Kazakhstan': 'Asia',
 'Namibia': 'Africa',
 'Nepal': 'Asia',
 'Poland': 'Europe',
 'Portugal': 'Europe',
 'Hungary': 'Europe',
 'Jamaica': 'North America',
 'Finland': 'Europe',
 'Northern Cyprus': 'Asia',
 'Russia': 'Europe',
 'Cayman Islands': 'North America',
 'Nicaragua': 'North America',
 'Iceland': 'Europe',
 'Indonesia': 'Asia',
 'Barbados': 'North America',
 'Vietnam': 'Asia',
 'Iran': 'Asia',
 'Cyprus': 'Asia',
 'Mauritius': 'Africa',
 'Philippines': 'Asia',
 'Jordan': 'Asia',
 'Romania': 'Europe',
 'Guam': 'Oceania',
 'Kenya': 'Africa',
 'Macedonia (FYROM)': 'Europe',
 'Palestinian Territory, Occupied': 'Asia',
 'Sri Lanka': 'Asia',
 'Israel': 'Asia',
 'Bahrain': 'Asia',
 'Egypt': 'Africa',
 'Qatar': 'Asia',
 'Azerbaijan': 'Asia',
 'Slovenia': 'Europe',
 'Ukraine': 'Europe',
 'Macao (SAR)': 'Asia',
 'Albania': 'Europe',
 'Nigeria': 'Africa',
 'Lebanon': 'Asia',
 'Bulgaria': 'Europe',
 'Puerto Rico': 'North America',
 'Bangladesh': 'Asia',
 'United States Virgin Islands': 'North America',
 'Mexico': 'North America',
 'Oman': 'Asia',
 'Ethiopia': 'Africa',
 'Monaco': 'Europe',
 'Bosnia and Herzegovina': 'Europe',
 'Brazil': 'South America',
 'Armenia': 'Asia',
 'Rwanda': 'Africa',
 'Kyrgyzstan': 'Asia',
 'Liechtenstein': 'Europe',
 'Ghana': 'Africa',
 'Grenada': 'North America',
 'Argentina': 'South America',
 'Serbia': 'Europe',
 'Belize': 'North America',
 'Trinidad and Tobago': 'North America',
 'Curaçao': 'North America',
 'Aruba': 'North America'}




data   = json.load(open('all_data.json', encoding='utf-8'))

data.sort(key=lambda s: s['Nivel'])



arts   = json.load(open('all_arts.json', encoding='utf-8'))

arts.sort(key=lambda s: s['Nivel'])



business   = json.load(open('all_business.json', encoding='utf-8'))

business.sort(key=lambda s: s['Nivel'])



design   = json.load(open('all_design.json', encoding='utf-8'))

design.sort(key=lambda s: s['Nivel'])



marketing   = json.load(open('all_marketing.json', encoding='utf-8'))

marketing.sort(key=lambda s: s['Nivel'])



product   = json.load(open('all_product.json', encoding='utf-8'))

product.sort(key=lambda s: s['Nivel'])



soft   = json.load(open('all_soft.json', encoding='utf-8'))

soft.sort(key=lambda s: s['Nivel'])



tech   = json.load(open('all_tech.json', encoding='utf-8'))

tech.sort(key=lambda s: s['Nivel'])



bachelor   = json.load(open('bachelor.json', encoding='utf-8'))

bachelor.sort(key=lambda s: s['Nivel'])



distance   = json.load(open('distance.json', encoding='utf-8'))

distance.sort(key=lambda s: s['Nivel'])



master   = json.load(open('master.json', encoding='utf-8'))

master.sort(key=lambda s: s['Nivel'])



phd   = json.load(open('phd.json', encoding='utf-8'))

phd.sort(key=lambda s: s['Nivel'])


short   = json.load(open('short.json', encoding='utf-8'))

short.sort(key=lambda s: s['Nivel'])





def replace_nivel(nivel):
    if nivel == 'short':
        return 'Course'
    else:
        return nivel.title()


def get_languag(lang):
    lista_lang = []
    if lang != None and lang != '':
        lang_sep = lang.split(';')
        for i in range(len(lang_sep)):
            lista_lang.append(lang_sep[i])
        return lista_lang
    else:
        return None
        

    
    
def modality(part, full, at_your):
    try:
        if part != 'Unknown' and full != 'Unknown' and at_your == None:
            resultado = ['Full Time', 'Part Time']
        elif part != 'Unknown' and full == 'Unknown' and at_your == None:
            resultado = ['Part Time']
        elif part == 'Unknown' and full != 'Unknown'and at_your == None:
            resultado = ['Full Time']
        elif part == 'Unknown' and full != 'Unknown'and at_your != None:
            resultado = ['Full Time', 'At Your Own Pace']
        elif part != 'Unknown' and full == 'Unknown'and at_your != None:
            resultado = ['Part Time', 'At Your Own Pace']
        elif part == 'Unknown' and full == 'Unknown'and at_your != None:
            resultado = ['At Your Own Pace']
        elif part != 'Unknown' and full != 'Unknown'and at_your != None:
            resultado = ['Full Time', 'Part Time', 'At Your Own Pace']
        return resultado
    except:
        return 'Unknown'
    
    

    
def complete_links(university, link):
    try:
        if university != None:
            if university.lower() == 'coursera':
                regreso = 'https://www.coursera.org/'
            elif university.lower() == 'udemy':
                regreso = 'https://www.udemy.com/'
            else:
                regreso = link
            return regreso
    except:
        return None
        



def get_duration(duracion):
    try:
        if duracion != 'Unknown':
            duracion_sep = duracion.split()
            if len(duracion_sep) == 2 and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                if int(duracion_sep[0]) == 1:
                    regreso = '1 month or less'
                elif int(duracion_sep[0]) > 1 and int(duracion_sep[0]) <= 6:
                    regreso = '6 months or less'
                elif int(duracion_sep[0]) > 6 and int(duracion_sep[0]) <= 11:
                    regreso = 'less than a year'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'years' and int(duracion_sep[0]) > 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'years' and int(duracion_sep[0]) == 1:
                regreso = '1 year'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'years' and int(duracion_sep[0]) <= 4:
                regreso = duracion
            elif len(duracion_sep) == 5 and int(duracion_sep[0]) > 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 5 and int(duracion_sep[0]) == 1:
                regreso = '1 year'
            elif len(duracion_sep) == 5 and int(duracion_sep[0]) == 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 2 and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                regreso = 'less than a year'
            elif len(duracion_sep) == 5 and duracion_sep[1] == 'years' and int(duracion_sep[0]) >= 4:
                regreso = '4 years or more'
            elif len(duracion_sep) == 5 and duracion_sep[1] == 'years' and int(duracion_sep[0]) <= 3:
                regreso = str(duracion_sep[0]) + ' ' + 'years'
            elif len(duracion_sep) == 2 and int(duracion_sep[0]) <= 6  and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                regreso = '6 months or less'
            elif len(duracion_sep) == 2 and int(duracion_sep[0]) <= 11  and duracion_sep[1] == 'month' or duracion_sep[1] == 'months':
                regreso = 'less than a year'
            return regreso
        else:
            return duracion
    except:
        return 'Unknown'
    
def get_program_duration(duracion, full, part):
    elemento_final = []
    lista = [duracion, full, part]
    for i in range(len(lista)):
        if lista[i] != 'Unknown':
            elemento_final.append(lista[i])
            break
    if len(elemento_final) == 1:
        return elemento_final[0]
    else:
        return 'Unknown'



acumulate     = []
acumulatedos  = []
acumulatetres = []
    


def get_code(area, degree,  count, acumulate):
    ceros = '000000'
    if degree[0:2].upper()   == 'BA':
            suma_ba = str(i)
            value = degree[0:2].upper() + '_' + ceros[:-len(suma_ba)] + suma_ba + '_' + area
            acumulate.append(i)
            return value
    elif degree[0:2].upper() == 'MA':
            suma_ma = str(i - len(acumulate)) 
            value = degree[0:2].upper() + '_' + ceros[:-len(suma_ma)] + suma_ma + '_' + area
            acumulatedos.append(i)
            return value
    elif degree[0:2].upper() == 'PH':
            suma_ph = str(i - len(acumulate) - len(acumulatedos) )
            value = degree[0:2].upper() + '_' + ceros[:-len(suma_ph)] +  suma_ph + '_' + area
            acumulatetres.append(i)
            return value
    elif degree[0:2].upper() == 'SH' or degree[0:2].upper() == 'CO':
            suma_co = str(i - len(acumulate) - len(acumulatedos) - len(acumulatetres) )
            value = degree[0:2].upper() + '_'  + ceros[:-len(suma_co)] +  suma_co + '_' + area
            return value
    else:
        return None


def edit_continent(function, universidad):
    try:
        if universidad != None:
            if universidad.lower() == 'coursera' or universidad.lower() == 'udemy':
                regreso = 'Anywhere'
            else:
                regreso = function
            return regreso
        elif universidad == None and function != None:
            return function
    except:
        return function
            

def edit_country(country, universidad):
    try:
        if universidad != None:
            if universidad.lower() == 'coursera' or universidad.lower() == 'udemy':
                regreso = 'Anywhere'
            else:
                regreso = country
            return regreso
        elif universidad == None and country != None:
            return country
    except:
        return country



def your_place(universidad, duracion_programa):
    try:
        if universidad != None:
            if 'coursera' == universidad.lower() or 'udemy' == universidad.lower():
                regreso = duracion_programa
            else:
                regreso = None
            return regreso
    except:
        return None



def your_place_none(at_your, full_part):
    if at_your != None:
        regreso = None
    else:
        regreso = full_part
    return regreso


def replace_university(university):
    if university == None:
        regreso = 'Unknown'
        return regreso
    else:
        return university



data_final = []

i = 0
for con in data:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
        "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    data_final.append(dicc)
    
    
    

with open('data.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(data_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('data.json')
df.to_excel('data.xlsx')




###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

arts_final = []

i = 0
for con in arts:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    arts_final.append(dicc)
    
    
    

with open('arts.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(arts_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('arts.json')
df.to_excel('arts.xlsx')


###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

business_final = []

i = 0
for con in business:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    business_final.append(dicc)
    
    
    

with open('business.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(business_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('business.json')
df.to_excel('business.xlsx')




###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

design_final = []

i = 0
for con in design:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    design_final.append(dicc)
    
    
    

with open('design.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(design_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('design.json')
df.to_excel('design.xlsx')



###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

marketing_final = []

i = 0
for con in marketing:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    marketing_final.append(dicc)
    
    
    

with open('marketing.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(marketing_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('marketing.json')
df.to_excel('marketing.xlsx')


###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

product_final = []

i = 0
for con in product:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    product_final.append(dicc)
    
    
    

with open('product.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(product_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('product.json')
df.to_excel('product.xlsx')



###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

soft_final = []

i = 0
for con in soft:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']


        }
    soft_final.append(dicc)
    
    
    

with open('soft.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(soft_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('soft.json')
df.to_excel('soft.xlsx')



###########################################################################################



acumulate     = []
acumulatedos  = []
acumulatetres = []
    

tech_final = []

i = 0
for con in tech:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    tech_final.append(dicc)
    
    
    

with open('tech.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(tech_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('tech.json')
df.to_excel('tech.xlsx')






###########################################################################################



consolidado_final   = json.load(open('consolidado.json', encoding='utf-8'))


con_final = []

i = 0
for con in consolidado_final:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             con['Area'],
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    con_final.append(dicc)
    
    
    

with open('consolidado_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(con_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('consolidado_final.json')
df.to_excel('consolidado_final.xlsx')



###########################################################################################


niveles = tech_final + soft_final +product_final + marketing_final + design_final + business_final + arts_final + data_final



bachelor_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Bachelor':
        bachelor_final.append(niveles[i])

    

with open('bachelor_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(bachelor_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('bachelor_final.json')
df.to_excel('bachelor_final.xlsx')








master_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Master':
        master_final.append(niveles[i])

    

with open('master_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(master_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('master_final.json')
df.to_excel('master_final.xlsx')





course_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Course':
        course_final.append(niveles[i])

    

with open('course_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(course_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('course_final.json')
df.to_excel('course_final.xlsx')






phd_final = []

for i in range(len(niveles)):
    if niveles[i]['DegreeType'] == 'Phd':
        phd_final.append(niveles[i])

    

with open('phd_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(phd_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('phd_final.json')
df.to_excel('phd_final.xlsx')




##################################################
#      Distance


def distance_level(level):
    if len(level) >= 2:
        regreso = level[0]
        return [regreso]
    else:
        return level


distance   = json.load(open('distance.json', encoding='utf-8'))

distance.sort(key=lambda s: s['Nivel'])




acumulate     = []
acumulatedos  = []
acumulatetres = []



dis_final = []

i = 0
for con in distance:
    if con['Area'] == 'ARTS' and con['Titulo'].lower() == 'artificial intelligence':
        continue
    i += 1
    duracion_programa = get_program_duration(con['Duracion'], con['Full Time'], con['Part Time'])
    at_your =  your_place(con['Universidad'], duracion_programa)
    dicc = {
        "Area":             distance_level(con['Area']),
        "Continent":        edit_continent(dicc_country.get(con['Pais']), con['Universidad']),
        "Country" :         edit_country(con['Pais'], con['Universidad']) ,
        "City"   :          con['Ciudad'],
        "Streets" :         con['Calles'],
        "Institution" :     con['Institucion'],
        "Language":         get_languag(con['Idioma']),
        "Subtitles":        con['Subtitulos'],
        "Qualification":    con['Calificacion'],
        "DegreeType":      replace_nivel(con['Nivel']),
        "PropertyID":      get_code(con['Area'][0], con['Nivel'], i, acumulate).replace('SH','CO'),
        "PartTime ":       your_place_none(at_your, con['Part Time']),
        "FullTime ":       your_place_none(at_your, con['Full Time']),
        "AtYourOwnPace": at_your,
        
        
        "Modality":          modality(con['Part Time'], con['Full Time'], at_your),
        "Attendence":       con['Cursada'],
        "ProgramDuration":duracion_programa,
        "Duration":        get_duration(duracion_programa),
        
        "Title":            con['Titulo'],
         "University":       replace_university(con['Universidad']),
        "AboutProgram":    con['Descripcion Programa'],
        "AboutInstitution":con['Descripcion Universidad'],
        "Categories":       con['Categoria'],
        "TutitionFree":    con['Tutition Free'],
        "Link"             :complete_links(con['Universidad'], con['Link University']),
        "Logo":             con['logo'],
        "MediaContent":    con['Multimedia']

        }
    dis_final.append(dicc)
    
    
    

with open('distance_final.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(dis_final, archivo_json, ensure_ascii=False, indent = 2)

df = pd.read_json('distance_final.json')
df.to_excel('distance_final.xlsx')









