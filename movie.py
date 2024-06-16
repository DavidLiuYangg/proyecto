# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:09:30 2024

@author: david
"""
class Movie: 
    """
    Clase que se encarga de gestionar las diferentes películas de los conjuntos de datos. 
    """
    def __init__(self, peli_id: int, titol: str, generos: list): 
        self._id = peli_id
        self._titol = titol
        self._generos = generos

    def __str__(self):
        """
        Sirve para poder imprimir los objetos de la clase "Movie"

        Returns
        -------
        sortida : str
            "String" con los diferentes atributos de la clase "Movie"
            
        Examples
        --------
        print(movie)
        """
        sortida = "ID: " + self._id + " - Títol: " + self._titol + " - Gèneres: " + str(self._generos)
        return sortida
        
    def get_id(self): 
        """
        Devuelve el "id" del objeto "Movie"

        Returns
        -------
        int : 
            ID del objeto "Movie"

        Examples
        --------
        id = Movie.get_id
        """
        return self._id
    
    def get_titol(self): 
        """
        Devuelve el "titol" del objeto "Movie"

        Returns
        -------
        str :
            Título del objeto "Movie"
        
        Examples
        --------
        titol = movie.get_titol
        """
        return self._titol
    
    def get_generos(self): 
        """
        Devuelve los "generos" del objeto "Movie"

        Returns
        -------
        list :
            Lista que contiene los diferentes géneros de la clase "Movie"
        
        Examples
        --------
        generos = movie.get_generos
        """
        return self._generos
    
    
    ID = property(get_id)
    titol = property(get_titol)
    generos = property(get_generos)



