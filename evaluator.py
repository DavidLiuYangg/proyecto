# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:59:24 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
import logging
import numpy as np
from math import sqrt


class Evaluator():
    def get_evaluation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int):
        puntuaciones_sist, filtro_puntuados = scoring.calcular_scores(dataset, fila_num_user, 1)
        puntuaciones_user = dataset.get_fila_user(fila_num_user)[filtro_puntuados]
        elementos = dataset.get_elementos_filtro(filtro_puntuados)
        
        elementos_sist_user = sorted(zip(elementos, puntuaciones_sist, puntuaciones_user), key=lambda x: x[1], reverse=True)
        
        self.mostrar_elementos(elementos_sist_user)
        
        MAE = np.absolute(puntuaciones_sist-puntuaciones_user).sum()/len(puntuaciones_user)
        RMSE = sqrt((((puntuaciones_user-puntuaciones_sist).sum())**2)/len(puntuaciones_user))
        logging.info("MAE: {} - RMSE: {}\n".format(MAE, RMSE))
    
    def mostrar_elementos(self, elementos:list, n:int =5):
        for i in range(n): 
            logging.info("ID: {} ==> Predicción: {}, Puntuación Usuario: {}\n".format(str(elementos[i][0].get_id()), elementos[i][1], elementos[i][2]))    
    
    