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
    def get_evaluation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int, es_cero: int =1):
        try:
            puntuaciones, filtro, elementos = super().calcular(scoring, dataset, fila_num_user, es_cero, es_recomendacion=False)
            puntuaciones_user = super().obtener_puntuaciones_user(dataset, fila_num_user, filtro)
            resultados = sorted(zip(elementos, puntuaciones, puntuaciones_user), key=lambda x: x[1], reverse=True)
            super().mostrar_resultados(resultados)
            
            MAE = np.absolute(puntuaciones - puntuaciones_user).sum() / len(puntuaciones_user)
            RMSE = sqrt((((puntuaciones_user - puntuaciones)**2).sum()) / len(puntuaciones_user))
            logging.info("MAE: {} - RMSE: {}\n".format(MAE, RMSE))
        except AssertionError as error:
            logging.error(error)