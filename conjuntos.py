# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:09:01 2024

@author: david
"""

import abc
import numpy as np
import logging

class Conjuntos(abc.ABC): 
    def __init__(self): 
        self._matriz_valoraciones: np.ndarray = np.empty(0)
        self._matriz_elementos: np.ndarray = np.empty(0) 
        #self._tipus: str = tipus
        logging.info("Se ha creado un objecto tipo {}".format(type(self)))
        
    @abc.abstractmethod 
    def cargar_datos(self): 
        raise NotImplementedError 
    
    def existe_usuario(self, num_fila_user: int) -> bool:
        return 0 <= num_fila_user < self._matriz_valoraciones.shape[0] 
    
    def get_fila_user(self, fila_num_user: int) -> np.ndarray: 
        return self._matriz_valoraciones[fila_num_user]  
    
    def get_elementos_filtro(self, filtro_a_puntuar: np.ndarray): 
        return self._matriz_elementos[filtro_a_puntuar] 
    
    def get_matriz_valoraciones(self): 
        return self._matriz_valoraciones
    def set_matriz_valoraciones(self, nueva_matriz_valoraciones: np.ndarray): 
        self._matriz_valoraciones = nueva_matriz_valoraciones
    
    def get_matriz_elementos(self): 
        return self._matriz_elementos
    def set_matriz_elementos(self, nueva_matriz_elementos: np.ndarray): 
        self._matriz_elementos = nueva_matriz_elementos

    valoraciones = property(get_matriz_valoraciones, set_matriz_valoraciones)
    elementos = property(get_matriz_elementos, set_matriz_elementos)
        
    