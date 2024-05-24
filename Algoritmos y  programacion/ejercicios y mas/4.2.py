'''2. Realizar un programa que tenga una clase Persona con las siguientes características. La
clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos
necesarios para inicializar los atributos utilizando el constructor (__init__), mostrar los datos e
indicar si la persona es mayor de edad o no.
¡Utilice el constructor!'''

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
    
    def mayor(self):
        if self.edad >= 18:
            print('La persona es mayor.')
        else:
            print('La persona es menor')
    
    
mipersona1 = Persona('Alexis', 17)
mipersona1.imprimir()
mipersona1.mayor()
print()
mipersona2 = Persona('Mili', 83)        
mipersona2.imprimir()
mipersona2.mayor()
