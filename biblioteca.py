class Biblioteca:
    """Administra una colección de objetos Material."""

    def __init__(self):
        """Crea una biblioteca con una lista vacía de materiales."""
        self.materiales = []

    def agregar_material(self, material):
        """Agrega un libro, revista o periódico a la biblioteca."""
        self.materiales.append(material)
        print(f"'{material.titulo}' ha sido agregado a la biblioteca.")

    def agregar_materiales(self, material):
        """Mantiene compatibilidad con el nombre plural usado en versiones anteriores."""
        self.agregar_material(material)

    def mostrar_catalogo(self):
        """Muestra la descripción de cada material usando polimorfismo."""
        print("\n--- CATÁLOGO DE LA BIBLIOTECA ---")
        if not self.materiales:
            print("La biblioteca está vacía.")
            return

        for indice, material in enumerate(self.materiales, start=1):
            print(f"\nMaterial {indice}:")
            print(material.descripcion())

    def calcular_total(self):
        """Suma y devuelve los precios de todos los materiales."""
        return sum(material.get_precio() for material in self.materiales)

    def valor_total(self):
        """Alias descriptivo para obtener el valor total del catálogo."""
        return self.calcular_total()
