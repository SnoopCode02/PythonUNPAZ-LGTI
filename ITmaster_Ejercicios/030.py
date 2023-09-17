## Ejercicio 030

### Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor. 

#(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0) 
from random import randint



terminar = False
while not terminar:
    num1 = randint(1,100)  #int(input("Ingrese el primer numero: "))
    num2 = randint(1,100)  #int (input("Ingrese el segundo numero: "))
    menor = num1
    mayor = num2
    if num2 < menor:
        aux = menor 
        menor = num2
        mayor = aux
    resultado_division = round(( mayor / menor),2)
    if mayor % menor == 0:
        print(f"El numero mayor: {mayor} es divisible por el menor: {menor}. Y el resultado es: {resultado_division}")
        terminar = True
    else:
        print(f"El numero mayor: {mayor} no es divisible por el menor: {menor}. Y el resultado es: {resultado_division}")
