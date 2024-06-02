# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:01:42 2024

@author: david
"""

from conjuntos import Conjuntos
from books import Books
from movies import Movies
import abc
import numpy as np
import logging

class Scoring(abc.ABC): 
    def __init__(self): 
        logging.debug("Se ha creado un objecto tipo {}".format(type(self)))
    
    def es_puntuable(self, tipus: str) -> bool:
        return True   
    
    def inicialitzar(self, dataset: Conjuntos): 
        pass
    
    def calcular_scores(self, dataset: Conjuntos, fila_num_user: int, es_cero:int) -> np.ndarray: 
        if es_cero == 0:
            filtro_a_puntuar = dataset.get_fila_user(fila_num_user) == 0
        else: 
            filtro_a_puntuar = dataset.get_fila_user(fila_num_user) != 0
        logging.info("El usuario no ha puntuado {} items".format(filtro_a_puntuar.sum()))
        return filtro_a_puntuar
        assert filtro_a_puntuar.sum() != 0, "No se puede recomendar al usuario"  
       
    '''
    def get_fila_user(self, fila_num_user: int) -> np.ndarray: 
        return self._dataset.valoraciones[fila_num_user]  
    
    def get_elementos_filtro(self, fila_num_user: int, filtro_a_puntuar): 
        return self._dataset.elementos[filtro_a_puntuar]
    '''