"""
Escribir un programa que permita cargar un vector de 10 números y luego muestre un menú con las siguientes opciones:

Promedio de todos
Mayor de los primos
Cantidad de impares
Menor de todos
Salir del programa
El menú se debe ejecutar en un ciclo siempre y cuando no se seleccione la opción "5 Salir del programa"
"""
import array as a 
CAN_NUM = 10
numeros = a.array('i', range(CAN_NUM))


for i in range(CAN_NUM):
    numeros[i] = int(input(f"Ingrese el {i+1}° numero: "))
    
opcion = ""

while opcion != '5':
    print("---- MENU -----")
    print("1- Promedio de todos")
    print("2- Mayor de los primos")
    print("3- Cantidad de impares")
    print("4- Menor de todos")
    print("5- Salir del programa")
    print("Seleccione la opción deseada: ", end="")
    opcion = input()
    
    if opcion == '1':
        sumatoria = 0
        cont = 0
        for numero in numeros:
            sumatoria += numero
            cont += 1
        print(f"El promedio de los {CAN_NUM} numeros ingresados es: {sumatoria / cont}")
    elif opcion == '2':
        mayor = 0
        for numero in numeros:
            cont = 0 
            for antecesor in range(numero):
                if numero % (antecesor+1) == 0:
                    cont += 1
            if cont == 2 and numero > mayor:
                mayor = numero
        print(f"El mayor de los primos ingresados es {mayor}")
    elif opcion == '3':
        cont_impares = 0
        for numero in numeros:
            if numero % 2 != 0:
                cont_impares += 1
        print(f"La cantidad de impares ingresados es {cont_impares}.")
    elif opcion == '4':
        menor = None
        for numero in numeros:
            if menor is None:
                menor = numero
            if numero < menor:
                menor = numero
        print(f"El menor de los numeros es {menor}")
    elif opcion == '5':
        print("Gracias por utilizar el programa!!")
    else:
        print("La opcion ingresada no es valida!!")        
     
    
    
    
    
    



