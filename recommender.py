import numpy as np 
import logging 
import abc
from movies import Movies
from books import Books

class Recommender: 
    
    def __init__(self): 
        self._dicc_datasets = {"Pelis": Movies, "Libros": Books}
        self._matriz_valoraciones: np.ndarray() = np.empty(0)
        #self._ll_elementos: list = []
        self._ll_elementos: np.ndarray() = np.empty(0)
        
        #self._ll_index_recomendaciones: list = []
        self._recomendaciones: list = []    
    
    @abc.abstractclassmethod
    def recomendar(self): 
        raise NotImplementedError
        
    def cargar_datos(self, tipo: str): 

        logging.info("Tipus de dataset " + tipo)
        dataset = self._dicc_datasets[tipo]()
        self._matriz_valoraciones, self._ll_elementos = dataset.leer_datos()
        
    def mostrar_recomendaciones(self, numero: int = 5): 
        
        for i in range(numero): 
            recomendacion = self._recomendaciones[i]
            print(recomendacion[0])
            
    def mostrar_usuario(self, user): #Faltan detalles
        print(self._matriz_valoraciones[user]) 