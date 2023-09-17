"""
3.9. Dado un vector de 6 posiciones se debe
a. Sumar los valores pares
b. Multiplicar los valores impares
"""
import array as a
TAM = 6
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

sum_pares = 0
prod_impares = 1
for i in range(TAM):
    if i % 2 == 0:
        sum_pares += num[i]
    else:
        prod_impares *= num[i]

print("Arreglo original")
for i in range(TAM):
    if i == 0:
        str = f"[{num[i]}, "
    elif i == TAM - 1:
        str = f"{num[i]}]"
    else:
        str = f"{num[i]}, "
    print(str, end="")

print(f"\nLa suma de los valores pares es: {sum_pares}")
print(f"El producto de los impares es: {prod_impares}")