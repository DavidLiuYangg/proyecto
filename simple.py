import numpy as np 
import logging 
import abc
from recommender import Recommender

class Simple(Recommender): 
    
    def __init__(self): 
        super().__init__()
        self._min_votos: int = 1
        self._avg_num_votos: np.ndarray = np.empty(0)
        self._avg_global: float = 0
        
        logging.info("S'he ha creado un objecto de tipo recomendacion Simple")
        
    def calcular_avg_i_votos(self): 
        
        self._min_votos = int(input("Min votos a tener en cuenta: "))
        
        num_votos_og = (self._matriz_valoraciones != 0).sum(axis=0)
        filtro_min_votos = num_votos_og >= self._min_votos
        
        logging.debug("Num items a considerar: {}".format(filtro_min_votos.sum()))
        
        num_vots = num_votos_og[filtro_min_votos]
        avg_items = self._matriz_valoraciones.sum(axis=0)[filtro_min_votos]/num_vots
        
        self._avg_num_votos = np.array([avg_items, num_vots])
        logging.debug("Shape de la matriz avg_items i num_vots: {}".format(self._avg_num_votos.shape))
        self._avg_global = (num_vots*avg_items).sum()/num_vots.sum()
        
        #Actualiza atributos según min_votos
        self._ll_elementos = self._ll_elementos[filtro_min_votos]
        logging.debug("Nuevo número de items: {}".format(len(self._ll_elementos)))
        self._matriz_valoraciones = self._matriz_valoraciones[:, filtro_min_votos]
        logging.debug("Nueva shape de la matriz de valoraciones: {}".format(self._ll_elementos.shape))
        
    def cargar_datos(self, tipo: str):
        
        super().cargar_datos(tipo)
        self.calcular_avg_i_votos()
        
    def calcular_scores(self, avg_item: np.ndarray, num_vots: np.ndarray, filtro_no_puntuados: np.ndarray): 
        
        termino1 = num_vots[filtro_no_puntuados]*avg_item[filtro_no_puntuados]/(num_vots[filtro_no_puntuados]+self._min_votos)
        termino2 = (self._min_votos*self._avg_global)/(num_vots[filtro_no_puntuados]+self._min_votos)    
        return termino1 + termino2
    
    def recomendar(self, user: int):
        
        fila_user = self._matriz_valoraciones[user-1]
        filtro_no_puntuados = fila_user == 0
        num_items_no_puntuados = filtro_no_puntuados.sum()
        logging.info("El usuario no ha puntuado %d items", num_items_no_puntuados)
        
        if num_items_no_puntuados != 0: 
            elementos_no_puntuados = self._ll_elementos[filtro_no_puntuados]
            scores_no_puntuados = self.calcular_scores(self._avg_num_votos[0], self._avg_num_votos[1], filtro_no_puntuados)
            
            self._recomendaciones = sorted(zip(elementos_no_puntuados, scores_no_puntuados), key=lambda x: x[1], reverse=True)
            self.mostrar_recomendaciones()
            
        else: 
            logging.info("No es pot recomanar a l'usuari")
            
        
        
        
    

