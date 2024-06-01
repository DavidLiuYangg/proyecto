from conjuntos import Conjuntos
from movies import Movies
from books import Books
from scoring import Scoring
from simple import Simple
from colaborativo import Colaborativo
from contenido import Contenido
from recommender import Recommender
from evaluator import Evaluator
import logging

class Recommender_system: 
    def __init__(self): 
        self._scoring: Scoring = None
        logging.debug("Se ha creado un objecto tipo {}".format(type(self)))
    
    def inicialitzar(self, dataset: str, metode: str): 
        dicc_scoring = {"Simple": Simple, "Colaborativo": Colaborativo, "Contenido": Contenido}
        self._scoring = dicc_scoring[metode]()  
        
        puntuable = self._scoring.es_puntuable(dataset) 
        if puntuable == True: 
            self._scoring.inicialitzar(dataset)
        else: 
            logging.info("El dataset {} es puntuable con el método {}: {}".format(dataset, metode, puntuable))
        return puntuable
    
    def ejecutar(self):
        user_id = int(input("User_ID: "))
        accion = input("Introduce una acción: ")
        
        if accion == "Recomendar": 
            r = Recommender()
            r.get_recommendation(self._scoring, user_id)
            return True
        elif accion == "Evaluar": 
            e = Evaluator()
            e.get_evaluation(self._scoring, user_id)
            return True
        else:
            return False
        
        