"""
Escribir un programa que tras asignar los números, -2, 5, 8, -9, 10, 15 y -4 a un
arreglo calcule, independientemente, la suma de los elementos positivos y
negativos
"""
import array as a

num = a.array('i', [-2, 5, 8, -9, 10, 15, -4])
suma_pos = 0
suma_nega = 0 
for numeros in num:
    if numeros < 0:
        suma_nega += numeros
    if numeros > 0:
        suma_pos += numeros
        
print(f"La suma de los positivos es: {suma_pos}")
print(F"La suma de los negativos es: {suma_nega}")
