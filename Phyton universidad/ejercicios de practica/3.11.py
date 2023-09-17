"""
3.11. Escribir un programa que lea tres números y los guarde en un vector. A
continuación, los ordenará y guardará los valores ordenados en otro vector.
Finalmente sacará ambos vectores por la pantalla
"""
import array as a
TAM = 3
num = a.array('i', range(TAM))

def es_entero(str_num):
    try:
        int(str_num)
        return True
    except:
        return False

for i in range(TAM):
    flag = False
    numero = ''
    while not flag:
        numero = input(f"Ingrese el {i+1}° numero: ")
        if es_entero(numero):
            num[i] = int(numero)
            flag = not flag
        else:
            print("El numero no es un entero.")
array_copia = a.array('i')
menor = None
medio = None
mayor = None
for numero in num:
    if menor is None:
        menor = numero
    elif numero < menor:
        menor = numero
for numero in num:
    if mayor is None:
        mayor = numero
    elif numero > mayor:
        mayor = numero
for numero in num:
    if medio is None:
        medio = numero
    if numero != menor and numero != mayor:
        medio = numero
        
array_copia.append(menor)
array_copia.append(medio)
array_copia.append(mayor)
print("Arreglo original")
for i in range(TAM):
    if i == 0:
        str = f"[{num[i]}, "
    elif i == TAM - 1:
        str = f"{num[i]}]"
    else:
        str = f"{num[i]}, "
    print(str,end="")

print("\nArreglo copia")
for i in range(TAM):
    if i == 0:
        str = f"[{array_copia[i]}, "
    elif i == TAM - 1:
        str = f"{array_copia[i]}]"
    else:
        str = f"{array_copia[i]}, "
    print(str,end="")