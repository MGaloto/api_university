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


class Whed():
    
    def __init__(self):
            self.main()

    def main(self):
        
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
        
        
        
        
        def getStreet(self, soup):
            try:
                street = soup.find_all('div', { 'class' : 'dl'})
                street = street[0].text.split('Street:')[1].split('\n')[0]
                return street
            except:
                return None
            
        def getLogo(self, soup):
            logos = soup.find_all('div', { 'class': 'galerie'})
            lista_logos = []
            if len(logos) >= 1:
                for i in range(len(logos)):
                    logos_final = ['https://whed.net/' + logos[i]['style'].replace(')','').replace('background-image:url(','')for i in range(len(logos))]
                    lista_logos.append(logos_final)
        
                return logos_final
            else:
                return lista_logos
            
        
        
        
        def getCity(self, soup):
            try:
                inst = soup.find_all('div', { 'class' : 'dl'})
                inst = inst[0].text.split('City:')[1].split('\n')[0]
                return inst
            except:
                return None
                        
            
            
        def getInstitute(self, soup):
            try:
                inst = soup.find_all('div', { 'class' : 'dl'})
                for i in range(len(inst)):
                        if inst[i].find('span').text == 'Institution Funding ' or inst[i].find('span').text == 'Institution Funding':
                            institute = inst[i].p.text
                return institute
            except:
                return None
            
        def getHistory(self, soup):
            try:
                explore = soup.find_all('div', { 'class' : 'dl'})
                for i in range(len(explore)):
                        if explore[i].find('span').text == 'History ' or explore[i].find('span').text == 'History':
                            hist = explore[i].p.text
                return hist
            except:
                return None
        
        
        def getProvincia(self, soup):
            try:
                prov = soup.find_all('div', { 'class' : 'dl'})[0]
                prov = prov.text.split('Province:')[1].split('\n')[0]
                return prov
            except:
                return None
            
        
        def getCountry(self, soup):
            try:
                country = soup.find_all('p', { 'class': 'country'})[0].text
                return country
            except:
                return None
            
        def getLink(self, soup):
            try:
                link = soup.find_all('a', { 'class': 'lien'})[0]['href']
                return link
            except:
                return None
                          
        def getLang(self, soup):
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
            
            ciudad = self.getCity(soup)
            street = self.getStreet(soup)
            inst   = self.getInstitute(soup)
            hist   = self.getHistory(soup)
            logo   = self.getLogo(soup)
            link   = self.getLink(soup)
            provincia = self.getProvincia(soup)
            pais = self.getCountry(soup)
            
            print('Provincia: ',provincia)
            print('Ciudad: ',ciudad)
            print('Calle: ',street)
            print('Instituto: ',inst)
            print('Historia: ',hist)
            print('Logo: ',logo)
            print('pais', pais)
            print('LENG: ', self.getLang(soup))
            print('Link: ',link,'\n')
            
            dicc = {'Area'           : None,
                    'Titulo'         : None,
                    'Categoria'      : None,
                    'Nivel'          : None,
                    'Pais'           : pais,
                    'Ciudad'         : ciudad,
                    'Lenguaje'       : self.getLang(soup),
                    'Provincia'      : provincia,
                    'Calle'          : street,
                    'Sitio'          : None,
                    'Institucion'    : inst,
                    'Subtitulos'     : None,
                    'Calificacion'   : None,
                    'Part Time'      : None,
                    'Full Time'      : None,
                    'Cursada'        : None,
                    'Duracion'       : None,
                    'Carrera'        : None,
                    'Universidad'    : names_final_unique_clean[count - 1].strip(),
                    'Descripcion'    : hist,
                    'Deadline'       :None,
                    'Requerimientos' : None,
                    'Link'           : href,
                    'Tutition Free'  : None,
                    'Valoracones'    : None,
                    'About University': None,
                    'Link University' : link,
                    'logo'           : logo,
                    'Multimedia'     : None
                    }
                            
            contenidofinal.append(dicc)
            
        with open('whed.json', 'w', encoding='utf-8') as archivo_json:
            json.dump(contenidofinal, archivo_json, ensure_ascii=False, indent = 2)
        
        
        
if __name__ == "__main__":
    objName = Whed()
    objName.main() 



 


    
    
    
    
    
    
    
    