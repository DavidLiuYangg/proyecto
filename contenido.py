import csv
import numpy as np 
import pickle 
import os.path
import logging 
from datetime import date
import abc
from recommender import Recommender

class Contenido(Recommender): 
    def __init__(self): 
        self._metodo = "Contenido"
        
    def recomendar(self): 
        pass