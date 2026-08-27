from material import Material


class Periodico(Material):
    """Clase hija de Material que representa un periódico."""

    def __init__(self, titulo, autor, precio, es_nuevo, fecha_publicacion):
        """Inicializa un periódico con su fecha de publicación."""
        super().__init__(titulo, autor, precio, es_nuevo)
        self.fecha_publicacion = fecha_publicacion

    def descripcion(self):
        """Sobrescribe el método de Material y agrega la fecha de publicación."""
        return f"{super().descripcion()}\nFecha de publicación: {self.fecha_publicacion}"
