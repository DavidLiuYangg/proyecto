# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:58:35 2024

@author: david
"""

import csv
from book import Book
import numpy as np 
from conjuntos import Conjuntos
import os
import logging

class Books(Conjuntos):  
    def __init__(self): 
        super().__init__()  

    def cargar_datos(self):
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
        
        with open(path + "\\Users.csv", "r", encoding = 'utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            users = []
            
            for i, row in enumerate(csvreader): 
                if i < 10000:
                    userId = row[0]
                    users.append(userId)
        
        matriz_valoraciones = np.zeros((len(users), len(matriz_elementos)), dtype='float32')
        
        with open(path + "\\Ratings.csv", "r", encoding = 'utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
        
            for row in (csvreader):
                    fila = int(row[0])
                    '''
                    if row[1] in indices and row[0] in users: 
                        columna = indices.index(row[1])
                        matriz_valoraciones[fila-1, columna] = float(row[2])
                    '''
                    try: 
                        columna = indices.index(row[1])
                        matriz_valoraciones[fila-1, columna] = float(row[2])
                    except: 
                        logging.debug("No apareix")
                    
                    
        self._matriz_valoraciones, self._matriz_elementos = matriz_valoraciones, matriz_elementos
        logging.info("Shape de matriz valoraciones (usuariosXitems): {}".format(self._matriz_valoraciones.shape))
        logging.info("Número de items: {}".format(len(self._matriz_elementos)))
        
        
        