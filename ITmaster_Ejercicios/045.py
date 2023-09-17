## Ejercicio 045

### Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.  

### Ejemplo:  

#- 4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).  
#- 3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).

a = int(input("Ingrese la base: "))
b = int(input("Ingrese el exponente: "))

producto = 1

for i in range(b):
    producto *= a

print(f"- {a}^{b} = {producto}. ({a} multiplicado {b} veces).")





