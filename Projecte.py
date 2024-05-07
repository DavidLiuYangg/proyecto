import csv
import abc
from conjuntos import Libros, Movies
from llibre import Llibre
from movie import Movie
import numpy as np


class Sistema: 
    def __init__(self): 
        self._datos = []
        self._valoraciones = np.empty(0)
        self._usuario = np.empty(0)
        self._tipos = {"Llibres": Libros(), "Pelis": Movies()}
        
    def get_datos(self) -> list: 
        return self._datos
    
    def get_valoraciones(self) -> np.ndarray: 
        return self._valoraciones
    
    def get_usuario(self) -> np.ndarray: 
        return self._usuario
    
    datos = property(get_datos)
    valoraciones = property(get_valoraciones)
    usuario = property(get_usuario)
    
    def Inicialitzar(self): 
        tipo = self._tipos[input("Tipus de dades: ")]
        #usuario_valoraciones = input("Introdueix les valoracions: ")
        #self._usuario = np.array([float(a) for a in usuario_valoraciones.split(",")])
        self._datos, self._valoraciones = tipo.llegeix_dades()        
    
    def RecomendacioSimple(self, min_vots: int = 3) -> (float, tuple): 
        m = self._valoraciones.copy()
        puntuadas = self._usuario != 0                 
        puntuadas = np.arange(9742) !=0
        
        num_vots = np.array((m != 0).sum(axis=0), dtype='float32')
        filtro_min_votos = num_vots >= 3
        num_vots[num_vots < 3] = 0.0

        sumatori_columnas = m.sum(axis=0)
        avg_global = sumatori_columnas[filtro_min_votos].sum()/num_vots[filtro_min_votos].sum()

        num_vots[filtro_min_votos] = (num_vots[filtro_min_votos]*sumatori_columnas[filtro_min_votos])/((num_vots[filtro_min_votos]+min_vots)*num_vots[filtro_min_votos]) + (3*avg_global)/(num_vots[filtro_min_votos]+3)
        
        num_vots[puntuadas] = 0
        
        maxim = num_vots.max()
        posicio = np.where(num_vots == maxim)
        
        
        return maxim, posicio[0]
        
    def RecomendacioColab(self, num_usuaris: int = 3): 
        similituds = []
        #for fila in self._valoraciones: 
        pass
    
    def RecomendacioContingut(self): 
        pass
    
    def getRecomendacion(self): 
        recomendacion = input("Tipus de recomendació: ")
        if recomendacion == "Simple":
            k = int(input("Mínim vots: "))
            max_puntuacion, posicio = self.RecomendacioSimple(k)
            print("Es recomana ==>", self._datos[posicio[0]].titol)
        elif recomendacion == "Colaborativa": 
            pass
            
            
c = Sistema()
c.Inicialitzar()

c.getRecomendacion()
