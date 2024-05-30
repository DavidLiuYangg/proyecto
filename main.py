import numpy as np 
import pickle 
import os.path
import logging 
from datetime import date
from simple import Simple
from colaborativo import Colaborativo
from contenido import Contenido
import argparse as arg


#Logging setup
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fecha = date.today().strftime("%Y%m%d")
formato = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

#file = logging.FileHandler('log_'+fecha+'.txt') #Modo añadir
file = logging.FileHandler('log_'+fecha+'.txt', mode='w')
file.setFormatter(formato)

stream = logging.StreamHandler()
stream.setFormatter(formato)

logger.addHandler(file)
logger.addHandler(stream)

#Argparser
parser = arg.ArgumentParser(description="Recommender")
parser.add_argument("--dataset", choices=["Books", "Movies"], type=str, help="Tipus de dataset Books/Movies")
parser.add_argument("--method", choices=["Simple", "Colaborativo", "Contenido"], type=str, help="Tipus de recomanació Simple/Colaborativo/Contenido")

args = parser.parse_args()

#Carga de objecto
try:
    dicc_metodos = {"1": Simple, "2": Colaborativo, "3": Contenido}
    
    dataset = args.dataset
    metode = args.method
    '''
    dataset = input("Introdueix el tipus de dataset: ")    
    print("1 - Simple\n2 - Colaborativo\n3 - Contenido")
    metode = input("Introdueix el tipo de recomendació: ")
    '''
    nom_arxiu = 'recommender_' + dataset + '_' + metode + '.dat'
    
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
        accion = input(" 1 - Recomanació\n 2 - Avaluació\n 3 - Sortir\nIntrodueix la acció a fer: ")

        if accion == "1": 
            user_ID = int(input("Introdueix el número del USER: "))
            r.recomendar(user_ID)
            
        elif accion == "2": 
            pass
        else: 
            logging.info("SORTINT")
            continuar = False
    
finally: 
    #Logging close
    logger.handlers.clear()
    logging.shutdown()
