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
        with open("books.csv", "r", encoding = 'utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            dicc_books = dict()
            dicc_val_ini = dict()
            for row in csvreader:   
                dicc_val_ini[row[0]] = 0
                dicc_books[row[0]] = Llibre(row[0], row[1], row[2])
        
        self._datos = dicc_books
        columnas = len(self._datos)
        
        with open("booksRatings.csv", "r", encoding = 'utf-8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            m_valor = np.array(0)
            usuarios = []
            for row in csvreader:
                usuari = row[0]
                if usuari not in usuarios: 
                    m_valor = np.append(m_valor, np.zeros(columnas))
                peli, valoracion = row[1], row[2]
                m_valor[usuari-1][peli-1] = valoracion
        return dicc_books, m_valor

def Anime(Conjuntos): 
    def llegeix_dades(self): 
        pass
    
class Movies(Conjuntos):
    def llegeix_dades(self): 
        with open("movies.csv", "r", encoding='utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            dicc_movies = dict()
            i = 0
            for row in csvreader: 
                peli = Movie(row[0], row[1], row[2].split("|")) 
                dicc_movies[row[0]] = (peli, i)
                i+=1

        with open("moviesRatings.csv", "r", encoding = 'utf-8') as csv_file:
            columnas = len(dicc_movies.keys())
            matriz = np.empty((0, columnas))
            usuarios = []

            csvreader = csv.reader(csv_file)
            fields = next(csvreader)            
            for row in csvreader:
                usuario = int(row[0])
                if usuario not in usuarios: 
                    usuarios.append(usuario)
                    ceros = np.zeros((1, columnas), dtype='float32')
                    matriz = np.append(matriz, ceros, axis=0)
                    
                peli, valoracion = dicc_movies[row[1]][1], float(row[2])
                matriz[usuario-1, peli] = valoracion
        return dicc_movies, matriz