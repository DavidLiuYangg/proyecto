# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:01:25 2024

@author: david
"""

from movies import Movies
from books import Books
from scoring import Scoring
from simple import Simple
from colaborativo import Colaborativo
from contenido import Contenido
from recommender import Recommender
from evaluator import Evaluator
from conjuntos import Conjuntos
import logging

class Recommender_system: 
    def __init__(self): 
        self._scoring: Scoring = None
        self._dataset: Conjuntos = None
        self._puntuable = None
        logging.debug("Se ha creado un objecto tipo {}".format(type(self)))
    
    def inicialitzar(self, dataset: str, metode: str): 
        dicc_scoring = {"Simple": Simple, "Colaborativo": Colaborativo, "Contenido": Contenido}
        self._scoring = dicc_scoring[metode]()  
        self._puntuable = self._scoring.es_puntuable(dataset) 
        
        if self._scoring.es_puntuable(dataset)  == True: 
            dicc_dataset = {"Books": Books, "Movies": Movies}
            self._dataset = dicc_dataset[dataset]()
            self._dataset.cargar_datos()
            self._scoring.inicialitzar(self._dataset)
    
    def mostrar_opciones(self): 
        logging.info("\n 1 - Recomendar\n 2 - Evaluar")
        
    def ejecutar(self) -> bool:
        #user_id = int(input("User_ID: "))
        num_fila_user = int(input("User_ID: ")) - 1
        self.mostrar_opciones()
        accion = int(input("Introduce una acción: "))
        continuar = True
        
        try: 
            assert self._dataset.existe_usuario(num_fila_user) == True, "Número de User inválido"
            if accion == 1: 
                r = Recommender()
                r.get_recommendation(self._scoring, self._dataset, num_fila_user)
                
            elif accion == 2: 
                e = Evaluator()
                e.get_evaluation(self._scoring, self._dataset, num_fila_user)
            else:
                continuar = False
        except (ValueError, AssertionError) as error: 
            logging.error(error)
        finally: 
            return continuar
        
    def get_puntuable(self) -> bool: 
        return self._puntuable
    
    puntuable = property(get_puntuable)