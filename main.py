from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from periodico import Periodico


def main():
    """Crea los objetos, muestra sus datos, modifica un precio y consulta el catálogo."""
    # Biblioteca es la clase administradora que contiene materiales.
    biblioteca = Biblioteca()

    # Libro, Revista y Periodico son clases hijas de Material.
    libro1 = Libro("Diario de una Pasión", "Christopher Nolan", 50000, True, 300)
    libro2 = Libro("Harry Potter", "J. K. Rowling", 70000, True, 500)
    revista = Revista("Vea", "Juan Pérez", 5000, True, 1)
    periodico = Periodico("LUN", "Domingo Covarrubias", 3000, True, "26-08-2026")

    print("--- DESCRIPCIÓN DE LOS OBJETOS ---")
    print("\nLibro 1:")
    print(libro1.descripcion())
    print("\nLibro 2:")
    print(libro2.descripcion())
    print("\nRevista:")
    print(revista.descripcion())
    print("\nPeriódico:")
    print(periodico.descripcion())

    # Se utiliza el setter encapsulado para modificar el precio del libro 1.
    libro1.set_precio(55000)
    print(f"\nNuevo precio de '{libro1.titulo}': ${libro1.get_precio()}")

    # Se agregan todos los materiales a la biblioteca.
    for material in (libro1, libro2, revista, periodico):
        biblioteca.agregar_material(material)

    # Polimorfismo: cada objeto ejecuta su propia versión de descripcion().
    biblioteca.mostrar_catalogo()
    print(f"\nValor total del catálogo: ${biblioteca.calcular_total()}")


if __name__ == "__main__":
    main()
