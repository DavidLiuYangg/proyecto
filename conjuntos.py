import abc
import numpy as np
import logging

class Conjuntos(abc.ABC): 
    def __init__(self): 
        self._matriz_valoraciones: np.ndarray = np.empty(0)
        self._matriz_elementos: np.ndarray = np.empty(0) 
        #self._tipus: str = tipus
        logging.info("Se ha creado un objecto tipo {}".format(type(self)))
        
    @abc.abstractmethod 
    def cargar_datos(self, metode: str): 
        raise NotImplementedError 
    
    def get_matriz_valoraciones(self): 
        return self._matriz_valoraciones
    
    def set_matriz_valoraciones(self, nueva_matriz_valoraciones: np.ndarray): 
        self._matriz_valoraciones = nueva_matriz_valoraciones
    
    def get_matriz_elementos(self): 
        return self._matriz_elementos
     
    def set_matriz_elementos(self, nueva_matriz_elementos: np.ndarray): 
        self._matriz_elementos = nueva_matriz_elementos
    
    def get_tipus(self): 
        return self._tipus
    
    valoraciones = property(get_matriz_valoraciones, set_matriz_valoraciones)
    elementos = property(get_matriz_elementos, set_matriz_elementos)
    #tipus = property(get_tipus)
        
    