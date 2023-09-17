## Ejercicio 044

### Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado. 

### Ejemplo:

# - 4*3 = 4 + 4 + 4 (4 sumado 3 veces).  
# - 3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).

a = int(input("Ingrese el multiplicando: "))
b = int(input("Ingrese el multiplicador: "))

producto = 0

for i in range(b):
    producto += a

print(f"- {a}*{b} = {producto}. ({a} sumado {b} veces).")
