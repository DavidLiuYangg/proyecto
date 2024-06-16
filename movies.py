import csv
import numpy as np 
import os
import logging

from movie import Movie
from conjuntos import Conjuntos

class Movies(Conjuntos):
    """
    Subclase de la clase "Conjuntos". Se encarga de la matriz de 
    valoraciones y elementos del conjunto de datos tipo "Movies".
    """
    
    def __init__(self): 
        super().__init__()

    def cargar_datos(self): 
        """
        Abre y lee los diferentes archivos para cargar las respectivas matrices.    
          
        Returns
        -------
        None.
        
        Examples
        --------
        Movies.cargar_datos
        """
        #Camino de los archivos de forma genral
        path = os.path.dirname(os.path.abspath(__file__)) + "\\dataset\\MovieLens100k"
        matriz_elementos = np.empty(0)
        ll_indices_id = []
        
        with open(path + "\\movies.csv", "r", encoding='utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            for row in csvreader: 
                peli = Movie(row[0], row[1], row[2]) 
                matriz_elementos = np.append(matriz_elementos, peli)
                ll_indices_id.append(row[0])
        matriz_valoraciones = np.empty((0, len(matriz_elementos)), dtype='float32')
        ll_users = []
        
        with open(path + "\\ratings.csv", "r", encoding='utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)    
            for row in csvreader:
                user = row[0]
                #Si es un usuario nuevo, se añade una fila toda llena de zeros
                if user not in ll_users: 
                    ll_users.append(user)
                    z = np.zeros((1, len(matriz_elementos)), dtype='float32')                    
                    matriz_valoraciones = np.append(matriz_valoraciones, z, axis=0)
                num_fila = int(user)-1
                num_columna = ll_indices_id.index(row[1])
                matriz_valoraciones[num_fila, num_columna] = float(row[2])

        self._matriz_valoraciones, self._matriz_elementos = matriz_valoraciones, matriz_elementos
        logging.info("Shape de matriz valoraciones (usuariosXitems): {}".
                     format(self._matriz_valoraciones.shape))
        logging.info("Número de items: {}".format(len(self._matriz_elementos)))
        