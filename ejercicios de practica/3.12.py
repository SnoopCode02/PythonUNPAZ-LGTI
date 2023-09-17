"""
3.12. Realizar un programa que genere 3 vectores de 10 posiciones cada uno. El primero
está formado por los números del 1 al 10. El segundo por el cuadrado de estos
números y el tercero por el cubo.
"""
import array as arr
TAM = 10
num1 = arr.array('i', [1,2,3,4,5,6,7,8,9,10])
num2 = arr.array('i')
num3 = arr.array('i')

def es_entero(num):
    try:
        int(num)
        return True
    except:
        return False
    
for numeros in num1:
    num2.append(numeros**2)
    num3.append(numeros**3)

print("Arreglo original")
for i in range(TAM):
    if i == 0:
        str = f"[{num1[i]}, "
    elif i == TAM - 1:
        str = f"{num1[i]}]"
    else:
        str = f"{num1[i]}, "
    print(str,end="")

print("\nArreglo al cuadrado")
for i in range(TAM):
    if i == 0:
        str = f"[{num2[i]}, "
    elif i == TAM - 1:
        str = f"{num2[i]}]"
    else:
        str = f"{num2[i]}, "
    print(str,end="")
    
print("\nArreglo al cubo")
for i in range(TAM):
    if i == 0:
        str = f"[{num3[i]}, "
    elif i == TAM - 1:
        str = f"{num3[i]}]"
    else:
        str = f"{num3[i]}, "
    print(str,end="")