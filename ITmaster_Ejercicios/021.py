## Ejercicio 021

### Escribir un programa que permita ingresar dos números enteros
# e indicar si el primero es mayor, menor o igual al segundo.
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
if numero1 > numero2:
    print(f"mayor: {numero1}")
else:
    if numero1 < numero2:
        print(f"mayor: {numero2}")
    else:
        print("son iguales")