import numpy as np 
import pickle 
import os.path
import logging 
from datetime import date
from simple import Simple
from colaborativo import Colaborativo
from contenido import Contenido

#Logging setup
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fecha = date.today().strftime("%Y%m%d")
formato = logging.Formatter('%(levelname)s - %(name)s: %(message)s')

#file = logging.FileHandler('log_'+fecha+'.txt') #Modo añadir
file = logging.FileHandler('log_'+fecha+'.txt', mode='w')
file.setFormatter(formato)

stream = logging.StreamHandler()
stream.setFormatter(formato)

logger.addHandler(file)
logger.addHandler(stream)

#Carga de objecto
try:
    dicc_metodos = {"Simple": Simple, "Colaborativo": Colaborativo, "Contenido": Contenido}
    
    print(list(dicc_metodos.keys()))
    metode = input("Introdueix el tipo de recomendació: ")
    dataset = input("Introdueix el tipus de dataset: ")
    
    nom_arxiu = 'recommender_' + str(dataset) + '_' + metode + '.dat'
    
    if os.path.isfile(nom_arxiu) == True: 
        logging.info("Existeix l'arxiu")
        with open(nom_arxiu, 'rb') as fitxer: 
            r = pickle.load(fitxer)
    else: 
        logging.info("No existeix l'arxiu " + nom_arxiu)
        r = dicc_metodos[metode]()
        r.cargar_datos(dataset)
        
        with open(nom_arxiu, 'wb') as fitxer:
            pickle.dump(r, fitxer)
            
    continuar = True
    
    while continuar == True: 
        accion = input("Introdueix la acció a fer: ")

        if accion == "Recomanació": 
            user_ID = int(input("Introdueix el número del USER: "))
            r.recomendar(user_ID)
            
        elif accion == "Comparació": 
            pass
        else: 
            logging.info("SORTINT")
            continuar = False
    
finally: 
    #Logging close
    logger.handlers.clear()
    logging.shutdown()
