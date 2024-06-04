# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:09:14 2024

@author: david
"""
class Book:
    def __init__(self, isbn: str, titulo: str, autor: str, year: str, editorial: str):
        self._id = isbn
        self._titulo = titulo
        self._autor = autor
        self._any_publicacio = year
        self._editorial = editorial
    
    def __str__(self): 
        sortida = "ID: " + self._isbn + " - Títol: " + self._titulo + " - Autor: " + self._autor + " - Any publicació: " + self._any_publicacio + " - Editorial: " + self._editorial
        return sortida
    
    def get_id(self): 
        return self._id
    def get_titol(self): 
        return self._titulo
    def get_autor(self): 
        return self._autor
    def get_any_publicacio(self): 
        return self._any_publicacio
    def get_editorial(self): 
        return self._editorial
    
    
    ID = property(get_id)
    titol = property(get_titol)
    autor = property(get_autor)
    year = property(get_any_publicacio)
    editorial = property(get_editorial)
    
    #Faltan getters