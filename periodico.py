
class Periodico:
    
    def __init__(self, edicion, titulo, autor, precio, es_nuevo, fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio
        self.es_nuevo = bool  
        self.fecha_publicacion = fecha_publicacion
    
    
    def descripcion(self):
        
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.__precio}")
        print(f"Es nuevo: {self.es_nuevo}")
        print(f"Fecha de publicación: {self.fecha_publicacion}")    