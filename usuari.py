class Usuari: 
    def __init__(self, id_usr: str, valoracions: dict,  localizacion: str = "", edat: int = 0 ): 
        self._id = id_usr
        self._valoracions = valoracions
        self._localizacion = localizacion
        self._edat = edat
    
    @property 
    def valoracions(self): 
        return self._valoracions