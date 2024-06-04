# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:59:24 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
from OtraClase import OtraClase
import logging
import numpy as np
from math import sqrt


class Evaluator(OtraClase):
    def get_evaluation(self, scoring, dataset, fila_num_user, es_cero=1):
        puntuaciones_sist, filtro_puntuados = self.calcular_scores(scoring, dataset, fila_num_user, es_cero)
        elementos = self.obtener_elementos(dataset, filtro_puntuados)
        puntuaciones_user = self.obtener_puntuaciones_user(dataset, fila_num_user, filtro_puntuados)
        
        elementos_sist_user = sorted(zip(elementos, puntuaciones_sist, puntuaciones_user), key=lambda x: x[1], reverse=True)
        
        self.mostrar_resultados(elementos_sist_user)
        
        MAE = np.absolute(puntuaciones_sist-puntuaciones_user).sum()/len(puntuaciones_user)
        RMSE = sqrt(((((puntuaciones_user-puntuaciones_sist)**2).sum()))/len(puntuaciones_user))
        logging.info("MAE: {} - RMSE: {}\n".format(MAE, RMSE))
    