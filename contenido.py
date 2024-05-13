import csv
import numpy as np 
import pickle 
import os.path
import logging 
from datetime import date
import abc
from recommender import Recommender
from sklearn.feature_extraction.text import TfidfVectorizer

class Contenido(Recommender): 
    def __init__(self): 
        super().__init__()
        self._metodo: str = "Contenido"
        self._tfidf_matrix = np.empty(0)
    
    def calcular_representacion_items(self): 
        item_features = [peli.generos for peli in self._ll_elementos]
        tfidf = TfidfVectorizer(stop_words='english')
        self._tfidf_matrix = tfidf.fit_transform(item_features).toarray()
        
        # debug
        logging.debug("Vocabulario: {}".format(tfidf.get_feature_names_out()))
        logging.debug("Shape matriz TFIDF: {}".format(self._tfidf_matrix.shape))
        
    def cargar_datos(self, tipo: str): 
        super().cargar_datos(tipo)
        self.calcular_representacion_items()
    
    def calcular_perfil(self, fila_user: int): 
        perfil = np.dot(fila_user, self._tfidf_matrix)
        return perfil/fila_user.sum()
    
    def calcular_distancia_cosinus(self, perfil_usuario: np.ndarray): 
        #perfil_usuario_t = np.transpose([perfil_usuario])
        similitud_items = np.dot(self._tfidf_matrix, perfil_usuario)
        distancias_items = similitud_items/np.sqrt((perfil_usuario**2).sum()*(self._tfidf_matrix**2).sum(axis=1))
        return distancias_items    
    
    def calcular_scores(self, user: int, fila_user: np.ndarray, filtro_no_puntuados: np.ndarray): 
        perfil_usuario = self.calcular_perfil(fila_user)
        distancias_items = self.calcular_distancia_cosinus(perfil_usuario)
        scores = distancias_items*self._matriz_valoraciones.max()
        return scores
    
    def recomendar(self, user: int): 
       fila_user = self._matriz_valoraciones[user-1]
       filtro_no_puntuados = fila_user == 0
       num_items_no_puntuados = filtro_no_puntuados.sum()
       logging.info("El usuario no ha puntuado %d items", num_items_no_puntuados)
       
       if num_items_no_puntuados != 0: 
           elementos_no_puntuados = self._ll_elementos[filtro_no_puntuados]
           scores_no_puntuados = self.calcular_scores(user, fila_user, filtro_no_puntuados)
           
           self._recomendaciones = sorted(zip(elementos_no_puntuados, scores_no_puntuados), key=lambda x: x[1], reverse=True)
           self.mostrar_recomendaciones()
           
       else: 
           logging.info("No es pot recomanar a l'usuari")
           
           