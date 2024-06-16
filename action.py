import logging
import abc

from scoring import Scoring
from conjuntos import Conjuntos

class Action(abc.ABC):
    """
    Clase abstracta que se encarga de gestionar el cálculo de puntuaciones.
    """
    
    @abc.abstractmethod 
    def ordenar_mostrar(self): 
        """
        Función abstracta que ordena las puntuaciones y las muestra.

        Raises
        ------
        NotImplementedError
            Si la función no está implementada en las subclases.

        Returns
        -------
        None.

        """
        raise NotImplementedError

    def calcular(self, scoring: Scoring, dataset: Conjuntos, fila_num_user: int, 
                 es_cero: int):
        """
        Calcula las puntuaciones del sistema así como los elementos puntuados 
        y los devuelve.

        Parameters
        ----------
        scoring : Scoring
            Objeto de la clase Scoring que permite calculas los scores del sistema.
        dataset : Conjuntos
            Objeto de la clase "Conjuntos" que contiene la matriz de valoraciones 
            de los usuarios y matriz de elementos.
        fila_num_jser: int
            Valor entero que indica la fila del usuario en la matriz de valoraciones.
        es_cero : int
            Valor que indica si es cero o no.
            
        Returns
        -------
        puntuaciones : list
            lista con las puntuaciones calculadas por el sistema. 
        elementos : list
            Lista con los elementos que se han puntuado.
        filtro : TYPE
            El filtro usado para calcular las puntuaciones, que pueden ser las 
            puntuadas o no puntuadas. 
            
        Examples
        --------
        Action.calcular(scoring, dataset, 1, 1)
        """
        try:
            
            puntuaciones, filtro = scoring.calcular_scores(dataset, 
                                                           fila_num_user, es_cero)
            elementos = dataset.get_elementos_filtro(filtro)
            return puntuaciones, elementos, filtro
        
        except AssertionError as error:
            logging.error(error)
