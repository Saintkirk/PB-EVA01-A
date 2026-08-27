from libro import Libro
from revista import Revista

material = Libro("Prueba", "Autor", 100, True, 10)
assert material.set_precio(0) is False
assert material.get_precio() == 100

libro_invalido = Libro("Prueba", "Autor", 100, True, 0)
assert libro_invalido.paginas == 0

revista_invalida = Revista("Prueba", "Autor", 100, True, -1)
assert revista_invalida.edicion == 0

print("Pruebas de validación aprobadas.")
