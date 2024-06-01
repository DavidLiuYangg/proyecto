import abc
from conjuntos import Conjuntos
from books import Books
from movies import Movies

class Scoring(abc.ABC): 
    def __init__(self): 
        self._dataset = None
        
    def es_puntuable(self, tipus: str) -> bool:
        return True   
    
    def inicialitzar(self, dataset: str): 
        dicc_dataset = {"Books": Books, "Movies": Movies}
        self._dataset = dicc_dataset[dataset]()
        self._dataset.cargar_datos()
        
    def calcular_scores(self): 
        raise NotImplementedError    
       
