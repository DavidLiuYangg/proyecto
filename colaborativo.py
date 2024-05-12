import numpy as np 
import logging 
from recommender import Recommender

class Colaborativo(Recommender): 
    
    def __init__(self): 
        self._metodo: str = "Colaborativo"
        logging.info("S'he ha creado un objecto de tipo recomendacion Colaborativo")

    def calcular_distancias(self, user: int, fila_user: np.ndarray): 
        
        distancias = np.empty(0)
        indices = np.empty(0)
        
        #fila_user = self._matriz_valoraciones[user-1]
        
        for i in self._matriz_valoraciones.shape[0]: 
            if i != user-1: 
                fila = self._matriz_valoraciones[i, :]
                filtro_elementos_comunes = (fila!=0)*(fila_user!=0)
                if len(filtro_elementos_comunes) == 0: 
                    logging.debug("No hi ha elements comuns entre %s i %s", i+1, user)
                else: 
                    numerador = (fila[filtro_elementos_comunes]*fila_user[filtro_elementos_comunes]).sum()
                    denominador = np.sqrt((fila[filtro_elementos_comunes]**2).sum())*np.sqrt((fila_user[filtro_elementos_comunes]**2).sum())
                    dist = numerador/denominador
                    distancias = np.append(distancias, dist)
                    indices = np.append(indices, i)
                    
        return distancias, indices
    
    def calcular_usuarios(self, user: int, k_similares: int, fila_user: np.ndarray):
        
        distancias, indices = self.calcular_distancias(user, fila_user)
        usuarios_distancias = sorted(zip(distancias, indices), key = lambda x: x[0], reverse=True)[0:k_similares]
        usuarios = [k[1] for k in usuarios_distancias]
        dist = [k[0] for k in usuarios_distancias]
        
        return usuarios, dist
            
    def calcular_scores(self, user: int, fila_user: np.ndarray, filtro_no_puntuados: np.ndarray): 
        k_similares = int(input("Introdueix el nombre k usuaris més similars: "))
        k_usuarios_similares, k_distancias = self.calcular_usuarios(user, k_similares, fila_user)
        
        matriz_usuarios = self._matriz_valoraciones[k_usuarios_similares][:, filtro_no_puntuados]
        
        mu_user = fila_user.sum()/(fila_user !=0).sum()
        mu_usuarios = matriz_usuarios.mean(axis=1)
        
        scores = np.empty(0)
        
        for j in range(matriz_usuarios.shape[1]): 
            columna = matriz_usuarios[:, j]
            score = mu_user +(((columna-mu_usuarios)*k_distancias).sum())/k_distancias.sum()
            scores=np.append(scores, score)
        
        return scores
    
    def recomendar(self, user: int): 
        
        fila_user = self._matriz_valoraciones[user-1]
        filtro_no_puntuados = fila_user == 0
        
        elementos_no_puntuados = self._ll_elementos[filtro_no_puntuados]
        
        scores_no_puntuados = self.calcular_scores(user, fila_user, filtro_no_puntuados)
        
        self._recomendaciones = sorted(zip(elementos_no_puntuados, scores_no_puntuados), key=lambda x: x[1], reverse=True)

        super().mostrar_recomendaciones()