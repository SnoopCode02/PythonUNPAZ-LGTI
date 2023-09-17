## Ejercicio 039

### Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176
COMIENZO = 42
FIN = 176
sum = 0
for numero in range(COMIENZO,FIN + 1):
    sum += numero
print(f"La sumatoria es: {sum}")