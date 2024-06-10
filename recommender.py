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
    def get_recommendation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int , es_cero: int = 0):
        try:
            puntuaciones, filtro, elementos  = super().calcular(scoring, dataset, fila_num_user, es_cero, es_recomendacion=True)
            resultados = sorted(zip(elementos, puntuaciones), key=lambda x: x[1], reverse=True)
            super().mostrar_resultados(resultados, es_recomendacion=True)
        except AssertionError as error:
            logging.error(error)