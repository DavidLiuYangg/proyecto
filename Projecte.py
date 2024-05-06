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
        
    def RecomendacioSimple(self, min_votos):
        array = np.empty((2,0)) 
        for i in range(self._valoraciones.shape[1]):
            datos = np.array([self._valoraciones[:,i][self._valoraciones[:,i] > 0].mean(), sum(self._valoraciones[:,i] > 0)]).reshape(2,1)
            array = np.append(array, datos, axis=1)
        avg_global = np.nanmean(array[0,:])
    return None    
    def RecomendacioColab(self): 
        pass
    
    def RecomendacioContingut(self): 
        pass
    
c = Sistema()
c.Inicialitzar()
