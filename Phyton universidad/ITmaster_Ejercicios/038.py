"""
## Ejercicio 038

### Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.
### Ejemplo
n = 5

n x 1 = 5
n x 2 = 10
n x 3 = 15
n x 4 = 20
n x 5 = 25
n x 6 = 30
n x 7 = 35
n x 8 = 40
n x 9 = 45
n x 10 = 50
"""

n = int(input("Numero: "))
MUL = 10
for i in range(MUL):
    resultado = n * (i+1)
    print(f"{n} X {i+1} = {resultado}")




