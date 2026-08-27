from material import Material


class Revista(Material):
    """Clase hija de Material que representa una revista."""

    def __init__(self, titulo, autor, precio, es_nuevo, edicion):
        """Inicializa una revista y valida que su edición sea positiva."""
        super().__init__(titulo, autor, precio, es_nuevo)
        if edicion <= 0:
            print("Error: el número de edición debe ser mayor que 0. No se aceptó el valor.")
            self.edicion = 0
        else:
            self.edicion = edicion

    def descripcion(self):
        """Sobrescribe el método de Material y agrega el número de edición."""
        return f"{super().descripcion()}\nEdición: {self.edicion}"
