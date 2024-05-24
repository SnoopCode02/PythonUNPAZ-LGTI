'''
4. Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método
para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''
def es_entero(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            return int(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero!')
            
class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def ver_numero(self):
        print(f'1er Numero: {self.num1}')
        print(f'2do Numero: {self.num2}')
        
    def suma(self):
        print(f'{self.num1} + {self.num2} = {self.num1+self.num2}')
    
    def resta(self):
        print(f'{self.num1} - {self.num2} = {self.num1-self.num2}')
    
    def multiplicacion(self):
        print(f'{self.num1} * {self.num2} = {self.num1*self.num2}')
    
    def division(self):
        if self.num2 == 0:
            print(f'No se puede dividir por 0.')
        else:
            print(f'{self.num1} / {self.num2} = {(self.num1/self.num2):.2f}')

numero1 = es_entero('Ingrese el primer numero: ')
numero2 = es_entero('Ingrese el segundo numero: ')

micalculo = Calculadora(numero1, numero2)

micalculo.ver_numero()
micalculo.suma()
micalculo.resta()
micalculo.multiplicacion()
micalculo.division()

