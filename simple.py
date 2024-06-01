import numpy as np 
import logging 
from scoring import Scoring

class Simple(Scoring): 
    
    def __init__(self): 
        super().__init__()
        self._min_votos: int = 0
        self._avg_num_votos: np.ndarray
        self._avg_global: float = 0
        
        logging.debug("Se ha creado un objecto tipo {}".format(type(self)))
    
    def calcular_avg_i_votos(self): 
        
        matriz_valoraciones = self._dataset.valoraciones
        matriz_elementos = self._dataset.elementos
        
        self._min_votos = int(input("Min votos a tener en cuenta: "))
        
        num_votos_og = (matriz_valoraciones != 0).sum(axis=0)
        filtro_min_votos = num_votos_og >= self._min_votos
        logging.debug("Num items a considerar: {}".format(filtro_min_votos.sum()))
        
        
        num_vots = num_votos_og[filtro_min_votos]
        avg_items = matriz_valoraciones.sum(axis=0)[filtro_min_votos]/num_vots
        
        self._avg_num_votos = np.array([avg_items, num_vots])
        self._avg_global = (num_vots*avg_items).sum()/num_vots.sum()
        logging.debug("Shape de la matriz avg_items i num_vots: {}".format(self._avg_num_votos.shape))
        
        #Actualiza dataset según min_votos
        self._dataset.valoraciones = matriz_valoraciones[:, filtro_min_votos]
        self._dataset.elementos = matriz_elementos[filtro_min_votos]
       
        logging.debug("Nueva shape de matriz de valoraciones (usuariosXitems): {}".format(self._dataset.valoraciones.shape))
        logging.debug("Nuevo número de items: {}".format(len(self._dataset.elementos)))
        
    
    def inicialitzar(self, dataset: str): 
        super().inicialitzar(dataset)
        self.calcular_avg_i_votos()

    
        

    
        
        
        
    

