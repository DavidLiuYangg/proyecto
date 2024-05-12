class Movie: 
    def __init__(self, peli_id: int, titol: str, generos: list): 
        self._id = peli_id
        self._titol = titol
        self._generos = generos

    def __str__(self): 
        sortida = "ID: " + self._id + " - Títol: " + self._titol + " - Gèneres: " + str(self._generos)
        return sortida
        
    def get_id(self): 
        return self._id
    
    def get_titol(self): 
        return self._titol
    
    def get_generos(self): 
        return self._generos
    
    
    ID = property(get_id)
    titol = property(get_titol)
    generos = property(get_generos)
    