import csv
import abc
from conjuntos import Libros, Movies
from llibre import Llibre
from movie import Movie
import numpy as np


class Sistema: 
    def __init__(self): 
        self._datos = {}
        self._valoraciones = np.empty(1)
        self._tipos = {"Llibres": Libros(), "Pelis": Movies()}
    
    def Inicialitzar(self): 
        tipo = self._tipos[input("Introdueix el tipus de dades: ")]
        self._datos, self._valoraciones = tipo.llegeix_dades()
        #recomendacion = input("Quin tipus de recomendació es vol?: ")
        
    def RecomendacioSimple(self): 
        pass
    
    def RecomendacioColab(self): 
        pass
    
    def RecomendacioContingut(self): 
        pass
    
c = Sistema()
c.Inicialitzar()
