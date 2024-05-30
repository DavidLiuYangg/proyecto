import csv
from book import Book
import numpy as np 
from conjuntos import Conjuntos
import os

class Books(Conjuntos):    
    def leer_datos(self):
        path = os.path.dirname(os.path.abspath(__file__)) + "\dataset\Books"
        with open(path + "books.csv", "r", encoding = 'utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            ll_books = np.empty(0)
            indices = []
            for i, row in enumerate(csvreader): 
                if i <50000:
                    indices.append(row[0])
                    llibre = Book(row[0], row[1], row[2], row[3], row[4])
                    ll_books = np.append(ll_books, llibre)
        
        with open(path + "booksUsers.csv", "r", encoding = 'utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            users = []
            
            for i, row in enumerate(csvreader): 
                if i <50000:
                    userId = row[0]
                    users.append(userId)
        
        matriz_valoraciones = np.zeros((len(users), len(ll_books)), dtype='float32')
        
        with open(path + "booksRatings.csv", "r", encoding = 'utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
        
            for row in (csvreader):
                    fila = int(row[0])
                    if row[1] in indices and row[0] in users: 
                        columna = indices.index(row[1])
                        matriz_valoraciones[fila-1, columna] = float(row[2])
                
        return matriz_valoraciones, ll_books