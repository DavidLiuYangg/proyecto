import csv
import abc
from llibre import Llibre
from movie import Movie
from usuari import Usuari
import numpy as np 


class Conjuntos: 
    @abc.abstractmethod 
    def llegeix_dades(self): 
        raise NotImplementedError    
    
class Libros(Conjuntos):    
    def llegeix_dades(self):
        with open("books.csv", "r", encoding = 'utf-8') as csv_file: #271360 libros
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            llibres = []
            indices = []
            for row in csvreader:   
                indices.append(row[0])
                llibre = Llibre(row[0], row[1], row[2])
                llibres.append(llibre)
        
        '''
        with open("booksUsers.csv", "r", encoding = 'utf-8') as csv_file: #278858 users
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            user = []
            
            for row in csvreader: 
                userId = row[0]
                user.append(userId)
        '''
        
        matriz = np.empty((278858, 271360), dtype='float16')
        
        with open("booksRatings.csv", "r", encoding = 'utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
        
            for row in csvreader:
                fila = int(row[0])
                columna = indices.index(row[1])
                matriz[fila-1, columna] = float(row[2])
                
        return llibres, matriz
        
def Anime(Conjuntos): 
    def llegeix_dades(self): 
        pass
    
class Movies(Conjuntos):
    def llegeix_dades(self): 
        with open("movies.csv", "r", encoding='utf-8') as csv_file: #9742 pelis
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            movies = []
            indices = []
            
            for row in csvreader: 
                indices.append(row[0])
                peli = Movie(row[0], row[1], row[2].split("|")) 
                movies.append(peli)
        
        matriz = np.empty((610, 9742), dtype='float32')
        
        with open("moviesRatings.csv", "r", encoding = 'utf-8') as csv_file: #610 users
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)    
            
            for row in csvreader:
                fila = int(row[0])
                columna = indices.index(row[1])
                matriz[fila-1, columna] = float(row[2])
                
        return movies, matriz
