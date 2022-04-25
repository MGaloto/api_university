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