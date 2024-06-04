# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:27:37 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
import logging

class OtraClase:
    def calcular_scores(self, scoring: Scoring, dataset: Conjuntos, fila_num_user:int , es_cero:int):
        return scoring.calcular_scores(dataset, fila_num_user, es_cero)
    
    def obtener_elementos(self, dataset, filtro):
        return dataset.get_elementos_filtro(filtro)
    
    def obtener_puntuaciones_user(self, dataset, fila_num_user, filtro):
        return dataset.get_fila_user(fila_num_user)[filtro]
    
    def mostrar_resultados(self, elementos, n=5, es_recomendacion=False):
        for i in range(min(n, len(elementos))):
            if es_recomendacion:
                logging.info("==>\nPuntuación: {} - {}\n".format(elementos[i][1], str(elementos[i][0])))
            else:
                logging.info("ID: {} ==> Predicción: {}, Puntuación Usuario: {}\n".format(str(elementos[i][0].get_id()), elementos[i][1], elementos[i][2]))