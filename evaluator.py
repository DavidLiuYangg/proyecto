# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:59:24 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
import logging
from math import sqrt
class Evaluator():
    def get_evaluation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int):
        puntuaciones_sist, filtro_puntuados = scoring.calcular_scores(dataset, fila_num_user, 1)
        puntuaciones_user = dataset.get_fila_user(fila_num_user)[filtro_puntuados]
        
        print("MAE: {}".format(((puntuaciones_sist-puntuaciones_user).sum())/len(puntuaciones_user)))
        print("RMSE: {}".format(sqrt((((puntuaciones_user-puntuaciones_sist).sum())**2)/len(puntuaciones_user))))
        
        
        
        