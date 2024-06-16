# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:09:14 2024

@author: david
"""
class Book:
    """
    Clase que gestiona los libros del conjunto de datos.
    """
    def __init__(self, isbn: str, titulo: str, autor: str, year: str, editorial: str):
        self._id = isbn
        self._titulo = titulo
        self._autor = autor
        self._any_publicacio = year
        self._editorial = editorial
    
    def __str__(self): 
        """
        Sirve para poder imprimir los objetos de la clase "Book"

        Returns
        -------
        sortida : str
            "String" con los diferentes atributos de la clase "Book"
            
        Examples
        --------
        print(book)
        """
        sortida = "ID: " + self._isbn + " - Títol: " + self._titulo + " - Autor: " + self._autor + " - Any publicació: " + self._any_publicacio + " - Editorial: " + self._editorial
        return sortida
    
    def get_id(self): 
        """
        Devuelve el "id" del objeto "Book"

        Returns
        -------
        str : 
            ISBN del objeto "Book"

        Examples
        --------
        id = book.get_id
        """
        return self._id
    def get_titol(self): 
        """
        Devuelve el "titol" del objeto "Book"

        Returns
        -------
        str :
            Título del objeto "Book"
        
        Examples
        --------
        titol = book.get_titol
        """
        return self._titulo
    def get_autor(self): 
        """
        Devuelve el "autor" "del objeto "Book"

        Returns
        -------
        str:
            Autor del objeto "Book"
            
        Examples
        --------
        autor = book.get_autor
        """
        return self._autor
    def get_any_publicacio(self): 
        """
        Devuelve el "any_publicacio" del objeto "Book"

        Returns
        -------
        str : 
            Año de publicación del objeto "Book"

        Examples
        --------
        año = book.get_any_publicacio
        """
        return self._any_publicacio
    def get_editorial(self): 
        """
        Devuelve el "editorial" del objeto "Book"

        Returns
        -------
        str : 
            Editorial del objeto "Book"
            
        Examples
        --------
        editorial = book.get_editorial

        """
        return self._editorial
    
    
    ID = property(get_id)
    titol = property(get_titol)
    autor = property(get_autor)
    year = property(get_any_publicacio)
    editorial = property(get_editorial)
    
    #Faltan getters