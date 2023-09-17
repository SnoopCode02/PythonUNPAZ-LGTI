"""
3.10. Escribir un programa que lea diez números, los guarde en un vector y a
continuación los muestre por pantalla en orden inverso al de su entrada
"""
import array as a
TAM = 10 
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
num_copia = a.array('i')

for i in range(TAM-1,-1,-1):
    num_copia.append(num[i])

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
        str = f"[{num_copia[i]}, "
    elif i == TAM - 1:
        str = f"{num_copia[i]}]"
    else:
        str = f"{num_copia[i]}, "
    print(str,end="")

""" Forma de imprimir sin guardar en otro lugar
print("\nArreglo cambiado")
for i in range(TAM-1,-1,-1):
    if i == TAM -1:
        str = f"[{num[i]}, "
    elif i == 0:
        str = f"{num[i]}]"
    else:
        str = f"{num[i]}, "
    print(str, end="")
"""