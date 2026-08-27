from material import Material


class Libro(Material):
    """Clase hija de Material que representa un libro."""

    def __init__(self, titulo, autor, precio, es_nuevo, paginas):
        """Inicializa un libro y valida que tenga más de cero páginas."""
        super().__init__(titulo, autor, precio, es_nuevo)
        if paginas <= 0:
            print("Error: la cantidad de páginas debe ser mayor que 0. No se aceptó el valor.")
            self.paginas = 0
        else:
            self.paginas = paginas

    def descripcion(self):
        """Sobrescribe el método de Material y agrega las páginas del libro."""
        return f"{super().descripcion()}\nPáginas: {self.paginas}"
