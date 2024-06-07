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
            self.calcular(scoring, dataset, fila_num_user, es_cero, es_recomendacion=False)
            
        except AssertionError as error:
            logging.error(error)