# 
from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from periodico import Periodico


def main():
    
    
    
    
    # CREAR LIBRO

    libro1 = Libro("Diario de una Pasión", "Christopher Nolan", 50000, True, 300)
    
    libro2 = Libro("Harry Potter","J. K. Rowling", 70000, True, 500)

    # CREAR REVISTA 
    
    vea = Revista ("Vea", "Juan Perez", 5000, True, 1)
    caras = Revista("Caras","David Gutierrez", 10000, True, 5)
    
    # CREAR PERIODICO
    
    lun = Periodico("LUN","Domingo Covarrubias",3000, True,"26-08-2026")
    el_mercurio = Periodico("El Mercurio","Alfredo Lamadrid",4000,True,"26-07-2026")
    
    #AGREGAR MATERIAL
    
    libro.material.agregar_objeto(libro1)
    libro.material.agregar_objeto(libro2)
    
    #MOSTRAR BIBLIOTECA
    libro.material.mostrar_catalogo()

    


if __name__ == "__main__":
    main()