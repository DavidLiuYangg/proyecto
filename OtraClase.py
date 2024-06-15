# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:27:37 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
import logging
import numpy as np
from math import sqrt
import abc

class OtraClase(abc.ABC):
    @abc.abstractmethod 
    def ordenar_mostrar(self): 
        raise NotImplementedError
     
    def obtener_elementos(self, dataset: Conjuntos, filtro: np.ndarray) -> np.ndarray:
        return dataset.get_elementos_filtro(filtro)
    
    def obtener_puntuaciones_user(self, dataset: Conjuntos, fila_num_user: int, filtro: np.ndarray):
        return dataset.get_fila_user(fila_num_user)[filtro]
    
    def calcular(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int , es_cero: int):
        try:
            
            puntuaciones, filtro = scoring.calcular_scores(dataset, fila_num_user, es_cero)
            elementos = self.obtener_elementos(dataset, filtro)
            puntuaciones_user = dataset.get_fila_user(fila_num_user)[filtro]
            return puntuaciones, elementos, puntuaciones_user
        
        except AssertionError as error:
            logging.error(error)
