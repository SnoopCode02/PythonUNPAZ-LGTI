'''
3. Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los
métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo
de triángulo que es (equilátero, isósceles o escaleno).
'''
def introducir_entero_valido(mensaje):
    while True:
        num = input(mensaje).strip()
        try:    
            num = int(num)
            return int(num)    
        except ValueError:
            print(f"El numero: {num} no es un entero, presione enter para continuar.")
            input()
class Triangulo:
    
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir(self):
        if (self.lado1 == self.lado2) and self.lado1 == self.lado3:
            print('El triangulo es equilatero')
        elif ((self.lado1 == self.lado2) and (self.lado1 != self.lado3)) or ((self.lado1 == self.lado3)and(self.lado1 != self.lado2)) or ((self.lado2 == self.lado3)and(self.lado1 != self.lado2)):
            print('El triangulo es iscoseles')
        else:
            print('El triangulo es escaleno')
            
l1 = introducir_entero_valido('Ingrese la medida del 1° lado del triangulo: ')
l2 = introducir_entero_valido('Ingrese la medida del 2° lado del triangulo: ')
l3 = introducir_entero_valido('Ingrese la medida del 3° lado del triangulo: ')  
          
tri1 = Triangulo(l1,l2,l3)

tri1.imprimir()
