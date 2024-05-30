import csv
import numpy as np 
import pickle 
import os.path
import logging 
from datetime import date
from recommender import Recommender
from sklearn.feature_extraction.text import TfidfVectorizer
from movies import Movies
from books import Books
from movie import Movie


def colab(m, items): 
    user = 1 #User = 1
    k = 2
    fila_user = m[user-1]
    
    
    distancias = np.empty(0)
    indices = np.empty(0)
    
    for i in range(m.shape[0]): 
        if i != user-1: 
            filtro_comun = (fila_user != 0)*(m[i] != 0)
            if filtro_comun.sum() != 0: 
                numerador = (m[i][filtro_comun]*fila_user[filtro_comun]).sum()
                denominador = np.sqrt((m[i][filtro_comun]**2).sum()*(fila_user[filtro_comun]**2).sum())
                dist = numerador/denominador
                distancias = np.append(distancias, dist)
                indices = np.append(indices, i)
            else: 
                logging.info("No hi ha elements en comun amb l'usuari %d", i+1)
    
    k_usuarios = sorted(zip(indices, distancias), key=lambda x: x[1], reverse=True)[0:k]
    
    usuarios = [int(a[0]) for a in k_usuarios]
    distancias_ord = np.array([a[1] for a in k_usuarios])
    
    m_usuarios = m[usuarios]
    
    mu_user = fila_user.sum()/(fila_user !=0).sum()
    mu_usuarios = m_usuarios.sum(axis=1)/(m_usuarios !=0).sum(axis=1)
    print("MU user:", mu_user)
    print("Mu USERS:", mu_usuarios)
    print("Distancias:", distancias_ord)
    f_user = fila_user == 0
    
    print("No puntuado:", f_user.sum())
    m_no_puntos = m_usuarios[:, f_user]
    
    print("Shape usuarios i no puntos:", m_no_puntos.shape)
    
    
    scores = np.empty(0)
    for j in range(m_no_puntos.shape[1]): 
        columna = m_no_puntos[:, j]
        score = mu_user + ((columna - mu_usuarios)*distancias_ord).sum()/distancias_ord.sum()
        scores = np.append(scores, score)
    
    print("MAX:", scores.max())
    
    orde = sorted(zip(items[f_user], scores), key=lambda x: x[1], reverse=True)
    
    for i in range(5): 
        print(orde[i][0], orde[i][1])
    
    
def simple(m, items): 
    min_votos = 3
    f_min = ((m!=0).sum(axis=0)) >= min_votos
    new_m = m[:, f_min]
    new_i = items[f_min]
    
    print("New_matrix:", new_m.shape)
    print("New items:", new_i.shape)
    
    num_vots = (new_m != 0).sum(axis=0) 
    avg_item = new_m.sum(axis=0)/num_vots
    avg_global = (avg_item*num_vots).sum()/num_vots.sum()
    
    print("Avg_global:", avg_global)
    print("Shape avg_item:", avg_item.shape)
    print("Shape num_vots:", num_vots.shape)
    
    
    fila = new_m[1]
    f_user = fila == 0
    
    print("No puntuados:", len(fila[f_user]))
    
    ter1 = (num_vots[f_user]*avg_item[f_user])/(num_vots[f_user]+min_votos)
    ter2 = (min_votos*avg_global)/(num_vots[f_user]+min_votos)
    
    scores = ter1 + ter2
    
    print("Numero rec:", scores.shape)
    
    orde = sorted(zip(new_i[f_user], scores), key=lambda x: x[1], reverse=True)
    print()
    for i in range(5): 
        print(orde[i][0], orde[i][1])
    
    
ll_movies = np.empty(0)
ll_indices_id = []

with open(os.path.dirname(os.path.abspath(__file__)) + "\dataset\MovieLens100k\movies.csv", "r", encoding='utf-8') as csv_file: 
    csvreader = csv.reader(csv_file)
    fields = next(csvreader)
    
    for row in csvreader: 
        peli = Movie(row[0], row[1], row[2]) 
        ll_movies = np.append(ll_movies, peli)
        ll_indices_id.append(row[0])