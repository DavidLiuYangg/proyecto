import numpy as np 
import logging 
import abc
from movies import Movies
from books import Books

class Recommender: 
    
    def __init__(self): 
        self._dicc_datasets = {"Pelis": Movies, "Libros": Books}
        
        self._matriz_valoraciones: np.ndarray() = np.empty(0)
        self._ll_elementos: np.ndarray() = np.empty(0) #Cambiar el nombre de self._ll_elementos
        self._recomendaciones: list = [] #list(Movie, float) or list(Book, float)?   
    
    @abc.abstractclassmethod
    def recomendar(self): 
        raise NotImplementedError
        
    def cargar_datos(self, tipo: str): 
        dataset = self._dicc_datasets[tipo]()
        self._matriz_valoraciones, self._ll_elementos = dataset.leer_datos()
        
        logging.debug("Shape matriz valoraciones: {}".format(self._matriz_valoraciones.shape))
        logging.debug("Número de items: {}".format(len(self._ll_elementos)))
        
    def mostrar_recomendaciones(self, numero: int = 5): 
        logging.debug("Se mostraran {} recomendaciones".format(numero))
        for i in range(numero): 
            recomendacion = self._recomendaciones[i]
            print(recomendacion[1], recomendacion[0])
