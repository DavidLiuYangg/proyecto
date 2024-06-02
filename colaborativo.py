# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:58:58 2024

@author: david
"""
import numpy as np 
import logging 
from scoring import Scoring
from conjuntos import Conjuntos


class Colaborativo(Scoring): 
    
    #Dependiente de usuario
    def calcular_distancias(self, fila_num_user: int, fila_user: np.ndarray, dataset: Conjuntos) -> list: 
        
        k = int(input("Introdueix el número de k usuarios: "))
        
        distancias = np.empty(0)
        indices = np.empty(0)
        
        for i in range(dataset.valoraciones.shape[0]): 
            if i != fila_num_user: 
                filtro_comun = (fila_user != 0)*(dataset.valoraciones[i] != 0)
                if filtro_comun.sum() != 0: 
                    numerador = (dataset.valoraciones[i][filtro_comun]*fila_user[filtro_comun]).sum()
                    denominador = np.sqrt((dataset.valoraciones[i][filtro_comun]**2).sum()*(fila_user[filtro_comun]**2).sum())
                    
                    distancias = np.append(distancias, numerador / denominador)
                    indices = np.append(indices, i)
                    
        return sorted(zip(indices, distancias), key=lambda x: x[1], reverse=True)[0:k]
        
    def calcular_usuarios(self, k_usuarios_distancias: list) -> int:
        
        usuarios = [int(a[0]) for a in k_usuarios_distancias]
        distancias_ord = np.array([a[1] for a in k_usuarios_distancias])
        
        return usuarios, distancias_ord
        
    def calcular_scores(self, dataset: Conjuntos, fila_num_user: int, es_cero: int):
        filtro_a_puntuar = super().calcular_scores(dataset, fila_num_user, es_cero)
        
        
        fila_user = dataset.get_fila_user(fila_num_user)
        
        k_usuarios_distancias = self.calcular_distancias(fila_num_user, fila_user, dataset)
        usuarios, distancias_ord = self.calcular_usuarios(k_usuarios_distancias)
        
        logging.debug("Indices usuarios similares: {}".format(usuarios))
        
        matriz_usuarios = dataset.valoraciones[usuarios]
        logging.debug("Shape matriz k usuarios: {}".format(matriz_usuarios.shape))
        
        
        mu_user = fila_user.sum()/(fila_user != 0).sum()
        mu_usuarios = matriz_usuarios.sum(axis=1)/(matriz_usuarios != 0).sum(axis=1)
        matriz_usuarios_filtro = matriz_usuarios[:, filtro_a_puntuar]
        
        logging.debug("MU user: {}".format(mu_user))
        logging.debug("MU users: {}".format(mu_usuarios))
        logging.debug("Distancias: {}".format(distancias_ord))
        
        scores = np.empty(0)
        
        for j in range(matriz_usuarios_filtro.shape[1]):
            columna = matriz_usuarios_filtro[:, j]
            score = mu_user + ((columna - mu_usuarios)*distancias_ord).sum()/distancias_ord.sum()
            scores = np.append(scores, score)
        
        return scores, filtro_a_puntuar