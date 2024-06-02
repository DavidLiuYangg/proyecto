# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:59:09 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
import numpy as np 
import logging 
from sklearn.feature_extraction.text import TfidfVectorizer

class Contenido(Scoring): 
    def __init__(self): 
        self._tfidf_matrix = np.empty(0)
        super().__init__()

    def es_puntuable(self, tipus: str) -> bool:
        return tipus != "Books"

    def inicialitzar(self, dataset: Conjuntos): 
        item_features = [peli.generos for peli in dataset.elementos]
        tfidf = TfidfVectorizer(stop_words='english')
        self._tfidf_matrix = tfidf.fit_transform(item_features).toarray()

        logging.debug("Vocabulario ({}): {}".format(len(tfidf.get_feature_names_out()), tfidf.get_feature_names_out()))
        logging.debug("Shape matriz TFIDF: {}".format(self._tfidf_matrix.shape))
    
    #Dependiente de usuario    
    def calcular_perfil(self, fila_user: int) -> np.ndarray: 
        perfil = np.dot(fila_user, self._tfidf_matrix)
        return perfil/fila_user.sum()
    
    def calcular_distancia_cosinus(self, perfil_usuario: np.ndarray) -> np.ndarray: 
        similitud_items = np.dot(self._tfidf_matrix, perfil_usuario)
        distancias_items = similitud_items/np.sqrt((perfil_usuario**2).sum()*(self._tfidf_matrix**2).sum(axis=1))
        return distancias_items    
    
    def calcular_scores(self, dataset: Conjuntos, fila_num_user: int, es_cero):
        filtro_no_puntuados = super().calcular_scores(dataset, fila_num_user,es_cero )
        
        fila_user = dataset.get_fila_user(fila_num_user)
        perfil_usuario = self.calcular_perfil(fila_user)
        distancias_items = self.calcular_distancia_cosinus(perfil_usuario)
        scores = distancias_items*dataset.valoraciones.max()
        return scores, filtro_no_puntuados
    
    
           