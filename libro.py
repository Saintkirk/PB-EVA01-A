

class Libro:
    
    def __init__(self, titulo, autor, precio, es_nuevo, edicion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio
        self.es_nuevo = (bool)      
        self.paginas = paginas

    def descripcion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.__precio}")
        print(f"Es nuevo: {self.es_nuevo}")
        print(f"Paginas: {self.paginas}")
          
    
    