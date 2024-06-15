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


class OtraClase:
    '''
    def calcular_scores(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int , es_cero: int) -> np.ndarray:
        return scoring.calcular_scores(dataset, fila_num_user, es_cero)
    
    def obtener_elementos(self, dataset: Conjuntos, filtro: np.ndarray) -> np.ndarray:
        return dataset.get_elementos_filtro(filtro)
    '''
    def obtener_puntuaciones_user(self, dataset: Conjuntos, fila_num_user: int, filtro: np.ndarray):
        return dataset.get_fila_user(fila_num_user)[filtro]
    
    def ordenar(self, elementos, puntuaciones_sist, puntuaciones_user: list = []):
        if puntuaciones_user == []: puntuaciones_user = puntuaciones_sist.copy()
        return sorted(zip(elementos, puntuaciones_sist, puntuaciones_user), key=lambda x: x[1], reverse=True)
        
    def mostrar_resultados(self): 
        pass
    '''
    def mostrar_resultados(self, elementos, puntuaciones_sist, puntuaciones_user: list = [], n: int =5, es_recomendacion: bool = False):
        resultados = self.ordenar(elementos, puntuaciones_sist, puntuaciones_user)
        for i in range(n):
            if es_recomendacion:
                logging.info("==>\nPuntuación: {} - {}\n".format(resultados[i][1], str(resultados[i][0])))
            else:
                logging.info("ID: {} ==> Predicción: {}, Puntuación Usuario: {}\n".format(str(resultados[i][0].get_id()), resultados[i][1], resultados[i][2]))
    '''
    def calcular(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int , es_cero: int):
        try:
            puntuaciones, filtro = scoring.calcular_scores(dataset, fila_num_user, es_cero)
            #puntuaciones, filtro = self.calcular_scores(scoring, dataset, fila_num_user, es_cero)
            #elementos = self.obtener_elementos(dataset, filtro)
            elementos = dataset.get_elementos_filtro(filtro)
            return puntuaciones, filtro, elementos
        except AssertionError as error:
            logging.error(error)
