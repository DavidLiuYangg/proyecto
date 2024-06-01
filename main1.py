'''
dataset
evaluator
recomendation_system
recommender
scoring 
user
'''

import pickle 
import os.path
import logging 
from datetime import date
import argparse as arg
from recommender_system import Recommender_system


#Logging setup
logger = logging.getLogger()
logger.handlers.clear()
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
parser.add_argument("dataset", choices=["Books", "Movies"], help="Tipus de dataset Books/Movies")
parser.add_argument("method", choices=["Simple", "Colaborativo", "Contenido"], help="Tipus de recomanació Simple/Colaborativo/Contenido")

args = parser.parse_args()

dataset = str(args.dataset)
metode = str(args.method)

try: 
    nom_arxiu = 'recommender_' + dataset + '_' + metode + '.dat'
    
    if os.path.isfile(nom_arxiu) == True: 
        logging.info("Existeix l'arxiu " + nom_arxiu)
        with open(nom_arxiu, 'rb') as fitxer: 
            rs = pickle.load(fitxer)
    else: 
        logging.info("No existeix l'arxiu " + nom_arxiu)
        rs = Recommender_system()
        puntuable = rs.inicialitzar(dataset, metode)
        
        with open(nom_arxiu, 'wb') as fitxer:
            pickle.dump(rs, fitxer)
    
    while puntuable == True: 
        continuar = rs.ejecutar()
    else: 
        logging.info("SORTINT")

finally: 
    logging.shutdown()