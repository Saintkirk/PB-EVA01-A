# Material descripscion() ejecuta la versión de Libro. 
# Revista o periodico según el Objeto

from periodico import Periodico
from revista import Revista

class Material:

    def __init__(self, titulo, autor, precio, es_nuevo):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio
        self.es_nuevo = bool
        

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def descripcion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.__precio}")
        print(f"Es nuevo: {self.es_nuevo}")