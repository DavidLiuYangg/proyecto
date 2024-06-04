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
        elementos_no_puntuados = dataset.get_elementos_filtro(filtro_puntuados)  
        elementos = sorted(zip(elementos_no_puntuados, puntuaciones_sist), key=lambda x: x[1], reverse=True)
        self.mostrar_recomendaciones(elementos)


        MAE = np.absolute(puntuaciones_sist-puntuaciones_user).sum()/len(puntuaciones_user)
        RMSE = sqrt((((puntuaciones_user-puntuaciones_sist).sum())**2)/len(puntuaciones_user))
        logging.info("MAE y RMS: {} - {}\n".format(MAE, RMSE))
        
    def mostrar_recomendaciones(self, recomendaciones): 
         for i in range(5): 
             logging.info("==>\nPuntuación: {} - {}\n".format(recomendaciones[i][1], str(recomendaciones[i][0])))
        
        
        