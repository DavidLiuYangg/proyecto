# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:00:57 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
import logging


class Recommender:     
    def get_recommendation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int):
        try: 
            scores_no_puntuados, filtro_no_puntuados = scoring.calcular_scores(dataset, fila_num_user, 0)
            elementos_no_puntuados = dataset.get_elementos_filtro(filtro_no_puntuados)  
            recomendaciones = sorted(zip(elementos_no_puntuados, scores_no_puntuados), key=lambda x: x[1], reverse=True)
            self.mostrar_recomendaciones(recomendaciones)
            
        except AssertionError as error: 
            logging.error(error)
        
    def mostrar_recomendaciones(self, recomendaciones: list, n: int = 5): 
        for i in range(5): 
            logging.info("==>\nPuntuación: {} - {}\n".format(recomendaciones[i][1], str(recomendaciones[i][0])))