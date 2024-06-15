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
            puntuaciones, elementos, filtro = self.calcular(scoring, dataset, fila_num_user, es_cero)
            puntuaciones_user = dataset.get_fila_user(fila_num_user)[filtro]
            self.ordenar_mostrar(elementos, puntuaciones, puntuaciones_user)
            
            MAE = np.absolute(puntuaciones - puntuaciones_user).sum() / len(puntuaciones_user)
            RMSE = sqrt((((puntuaciones_user - puntuaciones)**2).sum()) / len(puntuaciones_user))
            logging.info("MAE: {} - RMSE: {}\n".format(MAE, RMSE))
            
        except AssertionError as error:
            logging.error(error)
            
            
        def ordenar_mostrar(self, elementos, puntuaciones_sist, puntuaciones_user, n: int= 5):
            resultados = sorted(zip(elementos, puntuaciones_sist, puntuaciones_user), key=lambda x: x[1], reverse=True)
            for i in range(n):
                logging.info("ID: {} ==> Predicción: {}, Puntuación Usuario: {}\n".format(str(resultados[i][0].get_id()), resultados[i][1], resultados[i][2]))