from scoring import Scoring
from conjuntos import Conjuntos
import numpy as np 
import logging 

class Simple(Scoring): 
    
    def __init__(self): 
        self._min_votos: int = 0
        self._avg_num_votos: np.ndarray
        self._avg_global: float = 0
        
        super().__init__()
        
    def inicialitzar(self, dataset: Conjuntos): 
        matriz_valoraciones = dataset.valoraciones
        matriz_elementos = dataset.elementos
        
        self._min_votos = int(input("Min votos a tener en cuenta: "))
        
        num_votos_og = (matriz_valoraciones != 0).sum(axis=0)
        filtro_min_votos = num_votos_og >= self._min_votos
        logging.debug("Num items a considerar: {}".format(filtro_min_votos.sum()))
        
        
        num_votos = num_votos_og[filtro_min_votos]
        avg_items = matriz_valoraciones.sum(axis=0)[filtro_min_votos]/num_votos
        
        self._avg_num_votos = np.array([avg_items, num_votos])
        self._avg_global = (num_votos*avg_items).sum()/num_votos.sum()
        logging.debug("Shape de la matriz avg_items i num_votos: {}".format(self._avg_num_votos.shape))
        
        #Actualiza dataset según min_votos
        dataset.valoraciones = matriz_valoraciones[:, filtro_min_votos]
        dataset.elementos = matriz_elementos[filtro_min_votos]
       
        logging.debug("Nueva shape de matriz de valoraciones (usuariosXitems): {}".format(dataset.valoraciones.shape))
        logging.debug("Nuevo número de items: {}".format(len(dataset.elementos)))
        

    #Dependiente de usuario
    def calcular_scores(self, dataset: Conjuntos, fila_num_user: int):
        filtro_a_puntuar = super().calcular_scores(dataset, fila_num_user)
        avg_items, num_votos = self._avg_num_votos[0], self._avg_num_votos[1] 
        
        termino1 = num_votos[filtro_a_puntuar]*avg_items[filtro_a_puntuar]/(num_votos[filtro_a_puntuar]+self._min_votos)
        termino2 = (self._min_votos*self._avg_global)/(num_votos[filtro_a_puntuar]+self._min_votos)    
        return termino1 + termino2, filtro_a_puntuar
        

    
        
        
        
    

