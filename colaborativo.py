import numpy as np 
import logging 
from recommender import Recommender

class Colaborativo(Recommender): 
    
    def __init__(self): 
        
        super().__init__()
        logging.info("S'he ha creado un objecto de tipo recomendacion Colaborativo")

    def calcular_distancias(self, user: int, fila_user: np.ndarray) -> list: 
        
        k = int(input("Introdueix el número de k usuarios: "))
        
        distancias = np.empty(0)
        indices = np.empty(0)
        
        for i in range(self._matriz_valoraciones.shape[0]): 
            if i != user-1: 
                filtro_comun = (fila_user != 0)*(self._matriz_valoraciones[i] != 0)
                if filtro_comun.sum() != 0: 
                    numerador = (self._matriz_valoraciones[i][filtro_comun]*fila_user[filtro_comun]).sum()
                    denominador = np.sqrt((self._matriz_valoraciones[i][filtro_comun]**2).sum()*(fila_user[filtro_comun]**2).sum())
                    
                    distancias = np.append(distancias, numerador / denominador)
                    indices = np.append(indices, i)
                else: 
                    pass
                    #logging.info("No hi ha elements en comun amb l'usuari %d", i+1)
        
        return sorted(zip(indices, distancias), key=lambda x: x[1], reverse=True)[0:k]
        
    def calcular_usuarios(self, k_usuarios: list) -> int:
        
        usuarios = [int(a[0]) for a in k_usuarios]
        distancias_ord = np.array([a[1] for a in k_usuarios])
        
        return usuarios, distancias_ord
        
    def calcular_scores(self, user: int, fila_user: np.ndarray, filtro_no_puntuados: np.ndarray): 
        
        k_usuarios = self.calcular_distancias(user, fila_user)
        usuarios, distancias_ord = self.calcular_usuarios(k_usuarios)
        
        logging.debug("Indices usuarios similares: {}".format(usuarios))
        
        matriz_usuarios = self._matriz_valoraciones[usuarios]
        logging.debug("Shape matriz k usuarios: {}".format(matriz_usuarios.shape))


        mu_user = fila_user.sum()/(fila_user != 0).sum()
        mu_usuarios = matriz_usuarios.sum(axis=1)/(matriz_usuarios != 0).sum(axis=1)
        matriz_usuarios_filtro = matriz_usuarios[:, filtro_no_puntuados]
        
        logging.debug("MU user: {}".format(mu_user))
        logging.debug("MU users: {}".format(mu_usuarios))
        logging.debug("Distancias: {}".format(distancias_ord))
        
        scores = np.empty(0)
        
        for j in range(matriz_usuarios_filtro.shape[1]):
            columna = matriz_usuarios_filtro[:, j]
            score = mu_user + ((columna - mu_usuarios)*distancias_ord).sum()/distancias_ord.sum()
            scores = np.append(scores, score)
        
        return scores
        
    def recomendar(self, user: int): 
        
        fila_user = self._matriz_valoraciones[user-1]
        filtro_no_puntuados = fila_user == 0
        num_items_no_puntuados = filtro_no_puntuados.sum()
        logging.info("El usuario no ha puntuado %d items", num_items_no_puntuados)
        
        if num_items_no_puntuados != 0: 
            elementos_no_puntuados = self._ll_elementos[filtro_no_puntuados]
            scores_no_puntuados = self.calcular_scores(user, fila_user, filtro_no_puntuados)
            
            self._recomendaciones = sorted(zip(elementos_no_puntuados, scores_no_puntuados), key=lambda x: x[1], reverse=True)
            self.mostrar_recomendaciones()
            
        else: 
            logging.info("No es pot recomanar a l'usuari")