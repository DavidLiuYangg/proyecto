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
    """
        Subclase del objeto "Scoring" que se encarga de realizar los cálculos relacionados con la recomendación en base al contenido.
    """
        
    def __init__(self):
        self._tfidf_matrix = np.empty(0)
        super().__init__()

    def es_puntuable(self, tipus: str) -> bool:
        """
        Evalua si el tipo de dataset es puntuable. 
            
        Parameters
        ----------
        tipus: str
            El tipo de dataset.
                
        Returns
        -------
        Bool:
            Depende del tipo de dataset devuelve True o False
            
        Examples
        --------
        Puntuable = sistema.es_puntuable
        while Puntuable = True
            ...
        """
        return tipus != "Books"

    def inicialitzar(self, dataset: Conjuntos) -> None: 
        """
        Esta función inicializa la matriz TFIDF necesaria para poder hacer recomendaciones en base al contenido. 
          
        Parameters
        ----------
        dataset: Conjuntos
            Un objeto de la clase conjuntos que contiene una matriz de valoraciones y elementos.
                
        Returns
        -------
        None.
        
        Examples
        --------
        rs.inicalitzar(dataset)
        """
        item_features = [peli.generos for peli in dataset.elementos]
        tfidf = TfidfVectorizer(stop_words='english')
        self._tfidf_matrix = tfidf.fit_transform(item_features).toarray()

        logging.debug("Vocabulario ({}): {}".format(len(tfidf.get_feature_names_out()), tfidf.get_feature_names_out()))
        logging.debug("Shape matriz TFIDF: {}".format(self._tfidf_matrix.shape))
        item_features = [peli.generos for peli in dataset.elementos]
        tfidf = TfidfVectorizer(stop_words='english')
        self._tfidf_matrix = tfidf.fit_transform(item_features).toarray()

        logging.debug("Vocabulario ({}): {}".format(len(tfidf.get_feature_names_out()), tfidf.get_feature_names_out()))
        logging.debug("Shape matriz TFIDF: {}".format(self._tfidf_matrix.shape))
    
    #Dependiente de usuario    
    def calcular_perfil(self, fila_user: np.ndarray) -> np.ndarray: 
        """
        Calcula el perfil del usuario.
           
        Parameters
        ----------
        fila_user : np.ndarray
            Matriz que contiene la fila del usuario que contiene sus valoraciones. 
                
        Returns
        -------
        np.ndarray
            El array del perfil del usuario, donde asigna la importancia del usuario respecto a cada una de las características del vocabulario de conjunto de dartos. 
            
        Examples
        --------
        perfil_usuario = self.calcular_perfil(fila_user)
        """
        perfil = np.dot(fila_user, self._tfidf_matrix)
        return perfil/fila_user.sum()
    
    def calcular_distancia_cosinus(self, perfil_usuario: np.ndarray) -> np.ndarray: 
        """
        Calcula la distancia entre el perfil de un usuario y cada item.
        
        Parameters
        ----------
        perfil_usuario : np.ndarray
            El array del perfil del usuario.
            
        Returns
        -------
            distancia_items : np.ndarray
                Devuelve un arrray donde cada valor es la distancia entre las valoraciones del usuario y los items. 

        Examples
        --------
        distancia = calcular_distancia_cosinus(perfil_usuario)
        """
        similitud_items = np.dot(self._tfidf_matrix, perfil_usuario)
        distancias_items = similitud_items/np.sqrt((perfil_usuario**2).sum()*(self._tfidf_matrix**2).sum(axis=1))
        return distancias_items    
    
    def calcular_scores(self, dataset: Conjuntos, fila_num_user: int, es_cero:int):
        """
        Calcula las puntuaciones del usuario para los items que no ha puntuado. 
    
        Parameters
        ----------
        dataset: Conjuntos
            Objeto de la clase "Conjuntos" que contiene una matriz de valoraciones y una matriz de elementos.               
        fila_num_jser: int
            Valor entero que indica la fila del usuario en la matriz de valoraciones.
        es_cero : int
            Valor que indica si es cero o no.
            
        Returns
        -------
            scores : np.ndarray
                Una matriz donde cada valor es la puntuación que calcula el sistema para los items no puntuados del usuario. 
            filtr_no_puntuados : np.ndarray
                Una matriz que sirve para filtar los elementos no puntuados del usuario. 

        Examples
        --------
        Puntuaciones, filtro = scoring.calcular_scores(dataset, fila_num_user, es_cero)
        """
        
        filtro_no_puntuados = super().calcular_scores(dataset, fila_num_user,es_cero )
        
        fila_user = dataset.get_fila_user(fila_num_user)
        perfil_usuario = self.calcular_perfil(fila_user)
        distancias_items = self.calcular_distancia_cosinus(perfil_usuario)
        scores = distancias_items*dataset.valoraciones.max()
        return scores, filtro_no_puntuados
    
    
           