# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:00:57 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
from OtraClase import OtraClase
import logging

class Recommender(OtraClase):
    """CLASE"""
    def get_recommendation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int , es_cero: int = 0):
        try:
            puntuaciones, elementos, _ = self.calcular(scoring, dataset, fila_num_user, es_cero)
            self.ordenar_mostrar(elementos, puntuaciones)
        except AssertionError as error:
            logging.error(error)
    
            
    def ordenar_mostrar(self, elementos, puntuaciones_sist, n:int = 5):
        resultados = sorted(zip(elementos, puntuaciones_sist), key=lambda x: x[1], reverse=True)
        for i in range(n):
                logging.info("==>\nPuntuación: {} - {}\n".format(resultados[i][1], str(resultados[i][0])))
            
            
            
