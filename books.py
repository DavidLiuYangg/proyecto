import csv
import numpy as np 
import os
import logging

from conjuntos import Conjuntos
from book import Book

class Books(Conjuntos):  
    """
    Subclase de la clase "Conjuntos" que se encarga de cargar la matriz de 
    valoraciones y elementos del conjunto de datos "Books".
    """
    
    def __init__(self): 
        super().__init__()  

    def cargar_datos(self):
        """
        Abre y lee los diferentes archivos para cargar las respectivas matrices;
        valoraciones y los libros.    
          
        Returns
        -------
        None.
        
        Examples
        --------
        Books.cargar_datos
        """
        #Se busca el camino de los archivos de forma general
        path = os.path.dirname(os.path.abspath(__file__)) + "\\dataset\\Books"
        with open(path + "\\Books.csv", "r", encoding = 'utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            matriz_elementos = np.empty(0)
            indices = []
            for i, row in enumerate(csvreader): 
                if i < 10000:
                    indices.append(row[0])
                    llibre = Book(row[0], row[1], row[2], row[3], row[4])
                    matriz_elementos = np.append(matriz_elementos, llibre)
        
        with open(path + "\\Users.csv", "r", encoding='utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            users = []
            for i, row in enumerate(csvreader): 
                if i < 10000:
                    userId = row[0]
                    users.append(userId)
        matriz_valoraciones = np.zeros((len(users), len(matriz_elementos)), 
                                       dtype='float32')
        
        with open(path + "\\Ratings.csv", "r", encoding='utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            for row in (csvreader):
                    fila = int(row[0])
                    try: 
                        columna = indices.index(row[1])
                        matriz_valoraciones[fila-1, columna] = float(row[2])
                    except:
                        logging.debug("No apareix")
                        
        self._matriz_valoraciones, self._matriz_elementos = matriz_valoraciones, matriz_elementos
        logging.info("Shape de matriz valoraciones (usuariosXitems): {}".
                     format(self._matriz_valoraciones.shape))
        logging.info("Número de items: {}".format(len(self._matriz_elementos)))
        
        
        