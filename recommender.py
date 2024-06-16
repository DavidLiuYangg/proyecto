# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:00:57 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
from OtraClase import Action
import logging

class Recommender(Action):
    """
    Subclase de la clase "Action" que se encagar de obtener las recomendaciones y mostrarlas.
    """
    def get_recommendation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int , es_cero: int = 0):
        """
        Función que obtiene las recomendaciones y las muestra.

        Parameters
        ----------
        scoring : Scoring
            Objeto de la clase Scoring que permite calculas los scores del sistema.
        dataset : Conjuntos
            Objeto de la clase "Conjuntos" que contiene la matriz de valoraciones de los usuarios y matriz de elementos.
        fila_num_jser: int
            Valor entero que indica la fila del usuario en la matriz de valoraciones.
        es_cero : int
            Valor que indica si es cero o no.

        Returns
        -------
        None.
            
        Examples
        --------
        Recommender.get_evaluation(scoring, dataset, 1)
        """
        try:
            puntuaciones, elementos, filtro = self.calcular(scoring, dataset, fila_num_user, es_cero)
            self.ordenar_mostrar(elementos, puntuaciones)
        except AssertionError as error:
            logging.error(error)
    
            
    def ordenar_mostrar(self, elementos: list, puntuaciones_sist: list, n:int = 5):
        """
        Función que se encarga de ordenar las puntuaciones y mostrarlas. 

        Parameters
        ----------
        elementos : list
            Lista con las diferentes películas puntuadas.
        puntuaciones_sist : list
            lista con las puntuaciones calculadas por el sistema.
        n : int, optional
            Numero de elementos que se quieran mostrar

        Returns
        -------
        None.
        
        Examples
        --------
        recommender.ordenar_mostrar(elementos, puntuaciones_sist, puntuaciones_user)
        """
        resultados = sorted(zip(elementos, puntuaciones_sist), key=lambda x: x[1], reverse=True)
        for i in range(n):
                logging.info("==>\nPuntuación: {} - {}\n".format(resultados[i][1], str(resultados[i][0])))
            
            
            
