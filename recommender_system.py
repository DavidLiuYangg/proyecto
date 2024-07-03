import logging

from movies import Movies
from books import Books
from scoring import Scoring
from simple import Simple
from colaborativo import Colaborativo
from contenido import Contenido
from recommender import Recommender
from evaluator import Evaluator
from conjuntos import Conjuntos

class RecommenderSystem: 
    """
    Clase que se encarga del funcionamiento principal del recomendador y de 
    gestionar y controlar los diferentes sistemas de recomendación así 
    como la evaluación.
    """
    
    def __init__(self): 
        self._scoring: Scoring = None
        self._dataset: Conjuntos = None
        self._puntuable = None
        logging.debug("Se ha creado un objecto tipo {}".format(type(self)))
    
    def inicialitzar(self, dataset: str, metode: str): 
        """
        Carga los diferentes objetos que necesitan los sistemas de 
        recomendación y evaluación
          
        Parameters
        ----------
        dataset : Conjuntos
            Objeto de la clase "Conjuntos" que contiene la matriz de 
            valoraciones de los usuarios y matriz de elementos.
        metode: str
            El método de recomendación que se usará: Simple, 
            colaborativo o contenido.
            
        Returns
        -------
        None.
        
        Examples
        --------
        rs.inicialitzar(datset, simple)
        """
        dicc_scoring = {"Simple": Simple, "Colaborativo": Colaborativo, 
                        "Contenido": Contenido}
        self._scoring = dicc_scoring[metode]()  
        self._puntuable = self._scoring.es_puntuable(dataset) 
        
        if self._scoring.es_puntuable(dataset)  == True: 
            dicc_dataset = {"Books": Books, "Movies": Movies}
            self._dataset = dicc_dataset[dataset]()
            self._dataset.cargar_datos()
            self._scoring.inicialitzar(self._dataset)
    
    def mostrar_opciones(self): 
        """
        Muestra las diferentes opciones que tiene el usuario: Recomendar o Evaluar
            
        Returns
        -------
        None.
        
        Examples
        --------
        rs.mostrar_opciones
        """
        logging.info("\n 1 - Recomendar\n 2 - Evaluar\n 3 - Salir")
        
    def ejecutar(self) -> bool:
        """
        Empieza el proceso de recomendación o evaluación. 
        
        Returns
        -------
        bool:
            True si se sigue recomendando o evaluando y False si 
            se sale del programa principal
            
        Raise
        -----
        ValueError:
            Si la opción no es un int.
        AssertionError:
            Si el numero del usuario no existe.
        
        Examples
        --------
        rs.ejecutar
        """
        continuar = True
        try: 
            self.mostrar_opciones()
            accion = int(input("Introduce una acción: "))
            num_fila_user = int(input("User_ID: ")) - 1
            assert self._dataset.existe_usuario(num_fila_user) == True, "Núm User inválido"
            if accion == 1: 
                r = Recommender()
                r.get_recommendation(self._scoring, self._dataset, num_fila_user) 
            elif accion == 2:
                e = Evaluator()
                e.get_evaluation(self._scoring, self._dataset, num_fila_user)
            elif accion == 3:
                continuar = False
            else: 
                logging.info("Opción de acción no válida")
        
        except KeyboardInterrupt: 
            continuar = False
        
        except ValueError as error: 
            logging.error("Type introducido incorrecto - {}".format(error))
            
        except NotImplementedError as error: 
            logging.error("Falta implementar función o clase abstracta - {}".
                          format(error))
        
        except AssertionError as error: 
            logging.error(error)
            
        finally: 
            return continuar
        
    def get_puntuable(self) -> bool: 
        """
        Determinar si es la selección de dataset y método es puntuable.
        
        Returns
        -------
        bool
            True si es puntuable y False si no es puntuable

        """
        return self._puntuable
    
    puntuable = property(get_puntuable)