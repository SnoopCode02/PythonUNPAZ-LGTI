"""
Dado un vector de 10 posiciones se debe reemplazar los valores impares con una 0
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

num_copia = a. array('i')

for numero in num:
    if numero % 2 != 0:
        num_copia.append(0)
    else:
        num_copia.append(numero)
        
print("Arreglo original")
for i in range(TAM):
    if i == 0:
        str = f"[{num[i]}, "
    elif i == TAM - 1:
        str = f"{num[i]}]"
    else:
        str = f"{num[i]}, "
    print(str,end="")

print("Arreglo cambiado")
for i in range(TAM):
    if i == 0:
        str = f"[{num_copia[i]}, "
    elif i == TAM - 1:
        str = f"{num_copia[i]}]"
    else:
        str = f"{num_copia[i]}, "
    print(str, end="")