"""
Ejercicio 009

Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 
y num2. Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores
(que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.
Como pensarlo:

"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(f"El primer numero es: {num1} y el segundo es: {num2}")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"El primer numero es: {num1} y el segundo es: {num2}")


num1 = (input("Ingrese el primer numero: "))
num2 = (input("Ingrese el segundo numero: "))
print(num1,num2, sep=" <==> ")
aux = num1
num1 = num2
num2 = aux
print(num1,num2, sep=" <==> ")

num1,num2 = num2,num1 #solo python
print(num1,num2, sep=" <==> ")