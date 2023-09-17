## Ejercicio 022

### Escribir un programa que permita ingresar tres números 
# enteros e indicar cual es el mayor.

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))
"""
if n1 > n2:
    if n1 > n3:
        print(f"Mayor: {n1}")
    else:
        print(f"Mayor: {n3}")
else:
    if n2 > n1:
        if n2 > n3:
            print(f"Mayor: {n2}")
    
"""
mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
    
print(f"Mayor: {mayor}")