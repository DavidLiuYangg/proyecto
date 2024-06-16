# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:59:24 2024

@author: david
"""
from scoring import Scoring
from conjuntos import Conjuntos
from OtraClase import Action
import logging
import numpy as np
from math import sqrt


class Evaluator(Action):
    """
    Subclase de la clase "Action" que se encagar de obtener las evaluaciones y mostrarlas.
    """
    def get_evaluation(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int, es_cero: int =1):
        """
        Obtener el error entre los scores calculados por el sistema y las calificaciones del usuario y mostrarlas.

        Parameters
        ----------
        scoring : Scoring
            Objeto de la clase Scoring que permite calculas los scores del sistema.
        dataset : Conjuntos
            Objeto de la clase "Conjuntos" que contiene la matriz de valoraciones de los usuarios y matriz de elementos.
        fila_num_jser: int
            Valor entero que indica la fila del usuario en la matriz de valoraciones.
        es_cero : int
            Valor que indica si es cero o no.
            
        Returns
        -------
        None.
        
        Examples
        --------
        evaluator.get_evaluation(scoring,dataset,1)
        """
        try:
            puntuaciones, elementos, filtro = self.calcular(scoring, dataset, fila_num_user, es_cero)
            puntuaciones_user = dataset.get_fila_user(fila_num_user)[filtro]
            self.ordenar_mostrar(elementos, puntuaciones, puntuaciones_user)
            
            MAE = np.absolute(puntuaciones - puntuaciones_user).sum() / len(puntuaciones_user)
            RMSE = sqrt((((puntuaciones_user - puntuaciones)**2).sum()) / len(puntuaciones_user))
            logging.info("MAE: {} - RMSE: {}\n".format(MAE, RMSE))
            
        except AssertionError as error:
            logging.error(error)
            
            
        def ordenar_mostrar(self, elementos: list, puntuaciones_sist: list, puntuaciones_user: list, n: int= 5):
            """
            Función que se encarga de ordenar las puntuaciones y mostrarlas. 

            Parameters
            ----------
            elementos : list
                Lista con las diferentes películas puntuadas.
            puntuaciones_sist : list
                lista con las puntuaciones calculadas por el sistema.
            puntuaciones_user : list
                Lista con las puntuaciones dadas por el usuario.
            n : int, optional
                Numero de elementos que se quieran mostrar

            Returns
            -------
            None.
            
            Examples
            --------
            evaluator.ordenar_mostrar(elementos, puntuaciones_sist, puntuaciones_user)
            """
            resultados = sorted(zip(elementos, puntuaciones_sist, puntuaciones_user), key=lambda x: x[1], reverse=True)
            for i in range(n):
                logging.info("ID: {} ==> Predicción: {}, Puntuación Usuario: {}\n".format(str(resultados[i][0].get_id()), resultados[i][1], resultados[i][2]))