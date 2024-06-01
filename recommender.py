import abc
from conjuntos import Conjuntos

class Recommender: 
    def get_recommendation(self,dataset, scoring, user_id):
        filtro_no_puntuados = dataset._matriz_valoraciones[user_id-1] == 0
        recomendaciones = scoring.calcular_scores(dataset,filtro_no_puntuados)
        self.mostrar_recomendaciones(recomendaciones)
        
    def mostrar_recomendaciones(self, recomendaciones): 
        for a in range(5): 
            print(recomendaciones[a])
