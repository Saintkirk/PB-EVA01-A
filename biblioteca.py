#Polimorfismo 

class Biblioteca:
    
    def __init__(self):
        
        self.materiales = []
        
    #Método para agregar materiales
    def agregar_materiales(self, material):
        
        self.materiales.append(material)
        print(f"{material.nombre} ha sido agregado a la biblioteca")
        
    def mostrar_catalogo(self):
        
        print("\n ---BIBLIOTECA---")
        
        if len(self.materiales) == 0:
            print("La Biblioteca está vacia")
        else:
            
            for material in self.materiales:
                print(f" - {material.nombre}")