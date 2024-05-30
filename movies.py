import csv
from movie import Movie
import numpy as np 
from conjuntos import Conjuntos
import os

class Movies(Conjuntos):
    def leer_datos(self): 
        path = os.path.dirname(os.path.abspath(__file__)) + "\datast\MovieLens100k"
        ll_movies = np.empty(0)
        ll_indices_id = []
        
        with open(path + "movies.csv", "r", encoding='utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            
            for row in csvreader: 
                peli = Movie(row[0], row[1], row[2]) 
                ll_movies = np.append(ll_movies, peli)
                ll_indices_id.append(row[0])
        
        matriz_valoraciones = np.empty((0, len(ll_movies)), dtype='float32')
        ll_users = []
        
        with open(path + "moviesRatings.csv", "r", encoding = 'utf-8') as csv_file: 
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)    
            
            for row in csvreader:
                user = row[0]
                if user not in ll_users: 
                    ll_users.append(user)
                    z = np.zeros((1, len(ll_movies)), dtype='float32')                    
                    matriz_valoraciones = np.append(matriz_valoraciones, z, axis=0)
                    
                num_fila = int(user)-1
                num_columna = ll_indices_id.index(row[1])
                matriz_valoraciones[num_fila, num_columna] = float(row[2])
                
        return matriz_valoraciones, ll_movies