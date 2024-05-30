'''
dataset
evaluator
recomendation_system
recommender
scoring 
user
'''

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

dataset = args.dataset
metode = args.method

try: 
    nom_arxiu = 'recommender_' + dataset + '_' + metode + '.dat'
    print(nom_arxiu)

finally: 
    #Logging close
    logger.handlers.clear()
    logging.shutdown()