import abc
import numpy as np
import logging

class Conjuntos(abc.ABC): 
    """
    Clase abastracta. Se encarga de cargar y guardar la matriz de valoraciones 
    y la matriz de elementos de diferentes tipos de datasets.
    """
    
    def __init__(self): 
        self._matriz_valoraciones: np.ndarray = np.empty(0)
        self._matriz_elementos: np.ndarray = np.empty(0) 
        logging.info("Se ha creado un objecto tipo {}".format(type(self)))
        
    @abc.abstractmethod 
    def cargar_datos(self): 
        """
        Función abstracta que se encarga de carga la matriz de valoraciones 
        y elementos apartir de los diferentes conjuntos de datos.
        
        Raises
        ------
        NotImplementedError
            Levanta un error si las subclases no contienen esta función.

        Returns
        -------
        None.
        
        Examples
        --------
        conjuntos.cargar_datos

        """
        raise NotImplementedError 
    
    def existe_usuario(self, num_fila_user: int) -> bool:
        """
        Determina si el usuario existe o no dado el número de la fila. 

        Parameters
        ----------
        num_fila_user : int
            Valor que indica la fila del usuario en la matriz de valoraciones.

        Returns
        -------
        bool:
            True si el usuario existe, si no, False. 
       
        Examples
        --------
        while conjuntos.existe_usuario(num_fila_user):
            ...
        """
        return 0 <= num_fila_user < self._matriz_valoraciones.shape[0] 
    
    def get_fila_user(self, fila_num_user: int) -> np.ndarray: 
        """
        Devuelve la fila de la matriz de valoraciones del usuario. 

        Parameters
        ----------
        fila_num_user : int
            Valor que indica la fila del usuario en la matriz de valoraciones.

        Returns
        -------
        np.ndarray:
            Matriz con las valoraciones del usuario. 
            
        Examples
        --------
        fila = conjuntos.get_fila_user(1)
        """
        return self._matriz_valoraciones[fila_num_user]  
    
    def get_elementos_filtro(self, filtro_a_puntuar: np.ndarray) -> np.ndarray: 
        """
        Devuelve los elementos que se ajustan al filtro.
        
        Parameters
        ----------
        filtro_a_puntuar : np.ndarray
            Filtro de los elementos que se necesitan.

        Returns
        -------
        np.ndarray:
            Matriz que se ajusta al filtro.
            
        Examples
        --------
        elementos = conjuntos.get_elementos_filtr(filtro_a_puntuar)
        """
        return self._matriz_elementos[filtro_a_puntuar] 
    
    def get_matriz_valoraciones(self): 
        """
        Devuelve la matriz de valoraciones. 

        Returns
        -------
        np.ndarray:
            Matriz que contiene las diferentes valoraciones de los usuarios. 
            
        Examples
        --------
        matriz_valoraciones = conjuntos_get_matriz_valoraciones

        """
        return self._matriz_valoraciones
    
    def set_matriz_valoraciones(self, nueva_matriz_valoraciones: np.ndarray): 
        """
        Define una nueva matriz de valoraciones. 
        
        Parameters
        ----------
        nueva_matriz_valoraciones : np.ndarray
            Nueva matriz de valoraciones a utilizar
            
        Returns
        -------
        None
        
        Examples
        --------
        conjuntos.set_matriz_valoraciones(nueva_matriz)
        """
        self._matriz_valoraciones = nueva_matriz_valoraciones
    
    def get_matriz_elementos(self): 
        """
        Devuelve la matriz de elementos. 

        Returns
        -------
        np.ndarray:
            Matriz que contiene los diferentes elementos.
            
        Examples
        --------
        matriz_elementos = conjuntos.get_matriz_elementos
        """
        return self._matriz_elementos
    
    def set_matriz_elementos(self, nueva_matriz_elementos: np.ndarray): 
        """
        Define una nueva matriz de elementos. 
        
        Parameters
        ----------
        nueva_matriz_elementoss : np.ndarray
            Nueva matriz de elementos a utilizar
            
        Returns
        -------
        None
        
        Examples
        --------
        conjuntos.set_matriz_elementos(nueva_matriz)
        """
        self._matriz_elementos = nueva_matriz_elementos

    valoraciones = property(get_matriz_valoraciones, set_matriz_valoraciones)
    elementos = property(get_matriz_elementos, set_matriz_elementos)
        
    