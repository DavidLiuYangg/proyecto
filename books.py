import csv
from book import Book
import numpy as np 
from conjuntos import Conjuntos

class Books(Conjuntos):    
    def leer_datos(self):
        with open("books.csv", "r", encoding = 'utf-8') as csv_file: #271360 libros
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            ll_books = []
            indices = []
            for i, row in enumerate(csvreader): 
                if i <10000:
                    indices.append(row[0])
                    llibre = Book(row[0], row[1], row[2], row[3], row[4])
                    ll_books.append(llibre)
        
        with open("booksUsers.csv", "r", encoding = 'utf-8') as csv_file: #278858 users
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            user = []
            
            for row in csvreader: 
                userId = row[0]
                user.append(userId)
        
        matriz_valoraciones = np.empty((len(user), len(ll_books)), dtype='float32')
        
        with open("booksRatings.csv", "r", encoding = 'utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
        
            for row in csvreader:
                fila = int(row[0])
                if row[1] in indices: 
                    columna = indices.index(row[1])
                    matriz_valoraciones[fila-1, columna] = float(row[2])
                
        return matriz_valoraciones, ll_books