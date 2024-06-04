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
        peliculas = dataset.get_elementos_filtro(filtro_puntuados)
        elementos_sist = sorted(zip(peliculas, puntuaciones_sist), key=lambda x: x[1], reverse=True)
        elementos_user = sorted(zip(peliculas, puntuaciones_user), key=lambda x: x[1], reverse=True)
        
        logging.info("==>\nSistema:\n{}".format(self.mostrar_elementos(elementos_sist)))
        logging.info("==>\nUsuario:\n{}".format(self.mostrar_elementos(elementos_user)))
        
        MAE = np.absolute(puntuaciones_sist-puntuaciones_user).sum()/len(puntuaciones_user)
        RMSE = sqrt((((puntuaciones_user-puntuaciones_sist).sum())**2)/len(puntuaciones_user))
        logging.info("MAE y RMS: {} - {}\n".format(MAE, RMSE))
        
    def mostrar_elementos(self, elementos, n:int = 5): 
        mensaje = ""
        for i in range(n): 
            mensaje += str(elementos[i][1])+" - " +str(elementos[i][0].get_id())+"\n"
        return mensaje
        
        
        