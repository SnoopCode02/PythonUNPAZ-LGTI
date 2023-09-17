"""
3.13. Realizar un programa que por medio de un menú de opciones (usar la instrucción
elif) y trabajando con un vector de 10 números reales me permita:
a. Cargar el vector
b. Mostrar por pantalla el vector
"""
import array as a 
TAM = 10
numeros = a.array('i', range(TAM))
def es_entero(num):
    try:
        int(num)
        return True
    except:
        return False
flag = False
while not flag:
    print(f"""
        <======Menu=====>
A. Cargar el vector
B. Mostrar el vector
C. Salir del programa""")
    opcion = input("Ingrese una opcion: ").upper()
    if opcion == "A":
        for i in range(TAM):
            flag2 = False
            num = ""
            while not flag2:
                num = input(f"Ingrese el {i+1}° numero: ")
                if es_entero(num):
                    num = int(num)
                    numeros[i] = num
                    flag2 = not flag2
                else:
                    print("El caracter no res convertible a entero")
    elif opcion == "B":
        print("Arreglo")
        for i in range(TAM):
            if i == 0:
                str = f"[{numeros[i]}, "
            elif i == TAM -1:
                str = f"{numeros[i]}]"
            else:
                str = f"{numeros[i]}, "
            print(str, end="")
    elif opcion == "C":
        print("Gracias por utilizar el programa")
        flag = not flag
    else:
        print(f"La opcion ingresada '{opcion}' no es valida.")