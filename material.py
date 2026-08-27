class Material:
    """Clase padre que representa un material de la biblioteca."""

    def __init__(self, titulo, autor, precio, es_nuevo):
        """Inicializa los datos comunes y valida que el precio sea positivo."""
        self.titulo = titulo
        self.autor = autor
        self.__precio = 0
        self.set_precio(precio)
        self.es_nuevo = bool(es_nuevo)

    def get_precio(self):
        """Devuelve el precio encapsulado del material."""
        return self.__precio

    def set_precio(self, precio):
        """Actualiza el precio solo si es mayor que cero."""
        if precio <= 0:
            print("Error: el precio debe ser mayor que 0. No se aceptó el valor.")
            return False
        self.__precio = precio
        return True

    def descripcion(self):
        """Devuelve la descripción básica del material."""
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Precio: ${self.get_precio()}\n"
            f"Es nuevo: {'Sí' if self.es_nuevo else 'No'}"
        )
