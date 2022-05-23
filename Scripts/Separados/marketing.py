import json
import pprint
import pandas as pd



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


