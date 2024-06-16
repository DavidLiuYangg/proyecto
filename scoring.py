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
    """
    Clase abstraca que se encarga de los cálculos necesarios para hacer los diferentes tipos de recomendaciones.
    """
    def __init__(self): 
        logging.debug("Se ha creado un objecto tipo {}".format(type(self)))
    
    def es_puntuable(self, tipus: str) -> bool:
        """
        Resumen: 
            
          
        Parameters
        ----------
        tipus: str
            Tipo de dataset que es.
                
        Returns
        -------
        Bool
            Devuelve "True" si el dataset es punutable.

        Examples
        --------
        while scoring.es_puntuable(tipus):
            ...
        """
        return True   
    
    def inicialitzar(self, dataset: Conjuntos): 
        pass
    
    def calcular_scores(self, dataset: Conjuntos, fila_num_user: int, es_cero:int) -> np.ndarray: 
        """
        Calcula el filtro que se va a usar.
          
        Parameters
        ----------
        dataset: Conjuntos
            Objeto de la clase "Conjuntos" que contiene una matriz de valoraciones y una matriz de elementos.               
        fila_num_jser: int
            Valor entero que indica la fila del usuario en la matriz de valoraciones.
        es_cero : int
            Valor que indica si es cero o no.
                
        Returns
        -------
        filtro_a_puntuar : np.ndarray
             Filtro que sirve para calcular respecto a elementos ya puntuados o no puntuados.
        Raise
        -----
        AssertError:
            Levanta un error si el número de items que el usuario no ha puntuado es igual a 0.
            
        Examples
        --------
        filtro = scoring.calcular_scores(dataset,fila_num_user, es_cero)
        """
        if es_cero == 0:
            filtro_a_puntuar = dataset.get_fila_user(fila_num_user) == 0
            logging.info("El usuario no ha puntuado {} items".format(filtro_a_puntuar.sum()))
        else: 
            filtro_a_puntuar = dataset.get_fila_user(fila_num_user) != 0
            logging.info("El usuario ha puntuado {} items".format(filtro_a_puntuar.sum()))
        return filtro_a_puntuar
        assert filtro_a_puntuar.sum() != 0, "No se puede recomendar al usuario"  
       
    '''
    def get_fila_user(self, fila_num_user: int) -> np.ndarray: 
        return self._dataset.valoraciones[fila_num_user]  
    
    def get_elementos_filtro(self, fila_num_user: int, filtro_a_puntuar): 
        return self._dataset.elementos[filtro_a_puntuar]
    '''