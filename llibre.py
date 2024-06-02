# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:09:14 2024

@author: david
"""
class Llibre:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        #self._any_publicacio = year
        #self._editorial = editorial
    
    def __str__(self):
        return (str(self._isbn)+": "+str(self._titulo)+" "+str(self._autor))
