import pickle 
import os.path
import logging 
from datetime import date
import argparse as arg

from recommender_system import RecommenderSystem

#Logging setup
logger = logging.getLogger()
logger.handlers.clear()
logger.setLevel(logging.DEBUG)

fecha = date.today().strftime("%Y%m%d")
formato = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
#Nombre del archivo del log
file = logging.FileHandler('log_'+fecha+'.txt', mode='w') 
file.setFormatter(formato)

stream = logging.StreamHandler()
stream.setFormatter(formato)

logger.addHandler(file)
logger.addHandler(stream)

#Argparser
parser = arg.ArgumentParser(description="Recommender")
parser.add_argument("dataset", choices=["Books", "Movies"], 
                    help="Tipus de dataset Books/Movies")
parser.add_argument("method", choices=["Simple", "Colaborativo", "Contenido"], 
                    help="Tipus de recomanació Simple/Colaborativo/Contenido")

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
        rs = RecommenderSystem()
        rs.inicialitzar(dataset, metode)
        
        with open(nom_arxiu, 'wb') as fitxer:
            pickle.dump(rs, fitxer)
            
    #Mira si la combinación de dataset y puntuación compatible
    valido = rs.puntuable 
    logging.info("El dataset {} es puntuable con el método {}: {}".
                 format(dataset, metode, valido))
    
    while valido == True: 
        valido = rs.ejecutar()
    else: 
        logging.info("\nSORTINT")
    
except Exception as error: 
    logging.error(error)
finally: 
    logging.shutdown()
