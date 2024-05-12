import numpy as np 
import logging 
import abc
from recommender import Recommender

class Simple(Recommender): 
    
    def __init__(self): 
        super().__init__()
        self._avg_num_votos: np.ndarray = np.empty(0)
        self._avg_global: float = 0
        self._min_votos: int = 1
        
        logging.info("S'he ha creado un objecto de tipo recomendacion Simple")
        
    def calcular_avg_i_votos(self): 
        
        self._min_votos = int(input("Min votos a tener en cuenta: "))
        matriz_valoraciones = self._matriz_valoraciones
        
        matriz_avg_item_num_votos = np.zeros((2, matriz_valoraciones.shape[1]), dtype='float32')
        
        num_votos = np.array((matriz_valoraciones != 0).sum(axis=0))
        filtro_min_votos = num_votos >= self._min_votos
        
        avg_item = np.array((matriz_valoraciones.sum(axis=0)[filtro_min_votos]/ num_votos[filtro_min_votos]))
        
        matriz_avg_item_num_votos[0][filtro_min_votos] = avg_item
        matriz_avg_item_num_votos[1][filtro_min_votos] = num_votos[filtro_min_votos]
        
        self._avg_global = (avg_item*num_votos[filtro_min_votos]).sum()/num_votos[filtro_min_votos].sum()
        self._avg_num_votos =  matriz_avg_item_num_votos
        
    def cargar_datos(self, tipo: str):
        
        super().cargar_datos(tipo)
        self.calcular_avg_i_votos()
        
    def calcular_scores(self, num_vots: np.ndarray, avg_item: np.ndarray, filtro_no_puntuados: np.ndarray()): 
        
        termino1 = num_vots[filtro_no_puntuados]*avg_item[filtro_no_puntuados]/(num_vots[filtro_no_puntuados]+self._min_votos)
        termino2 = self._min_votos*self._avg_global/(num_vots[filtro_no_puntuados]+self._min_votos)    
        return termino1 + termino2
    
    '''
    def mostrar_recomendaciones(self, numero = 5): 
        for i in range(numero): 
            recomendacion = self._recomendaciones[i]
            print(recomendacion[0])
    '''
    
    def recomendar(self, user: int):
        
        fila_user = self._matriz_valoraciones[user-1]
        filtro_no_puntuados = fila_user == 0
        
        elementos_no_puntuados = self._ll_elementos[filtro_no_puntuados]
        
        scores_no_puntuados = self.calcular_scores(self._avg_num_votos[0], self._avg_num_votos[1], filtro_no_puntuados)
        
        self._recomendaciones = sorted(zip(elementos_no_puntuados, scores_no_puntuados), key=lambda x: x[1], reverse=True)
        
        super().mostrar_recomendaciones()
        #self.mostrar_recomendaciones()
        
        
        
    

