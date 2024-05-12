class Book:
    def __init__(self, isbn: str, titulo: str, autor: str, year: str, editorial: str):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._any_publicacio = year
        self._editorial = editorial
    
    def __str__(self): 
        pass
    
    #Faltan getters
    