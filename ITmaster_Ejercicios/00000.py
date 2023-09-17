import array as arr

TAM = 10
LIM_INF = -50
LIM_SUP =  50

numeros = arr.array('i', range(TAM))


def es_numero_entero(str_numero):
    try:
        int(str_numero)
        return True
    except Exception as e:
        return False


def esta_el_numero_dentro_del_intervalo(numero):
    return LIM_INF <= numero <= LIM_SUP


def leer_numero_entero_valido(mensaje):
    num = input(mensaje)
    if es_numero_entero(num):
        num = int(num)
        if not esta_el_numero_dentro_del_intervalo(num):
            print(f"El número {num} no esta dentro del intervalo ({LIM_INF} - {LIM_SUP})")
    else:
        print(f"El string '{num}' no se puede convertir a entero")
    return num


def mostrar_numeros(array_numeros):
    for i in range(TAM):
        if i == 0:
            str = f"[{array_numeros[i]}, "
        elif i == TAM - 1:
            str = f"{array_numeros[i]}]"
        else:
            str = f"{array_numeros[i]}, "
        print(str, end="")


def mostrar_menu():
    print("---- MENU ----")
    print("1- Realizar la sumatoria de los valores positivos pares")
    print("2- Realizar el conteo de los valores negativos")
    print("3- Calcular el promedio de todos los valores ingresados")
    print("4- Obtener el menor de todos los números ingresados")
    print("5- Obtener el número que más veces se repite en el vector")
    print(
        "6- Generar un vector destino y copiar (en las mismas posiciones) los valores positivos de las posiciones impares, en el resto copiar el valor 0")
    print("7- Salir del programa")


for i in range(TAM):
    numero = ""
    while not (es_numero_entero(numero) and esta_el_numero_dentro_del_intervalo(numero)):
        numero = leer_numero_entero_valido(f"Ingrese el {i + 1}° número: ")
    numeros[i] = numero

mostrar_numeros(numeros)
print()
opcion = ""


def sumatoria_positivos_pares(array_numeros):
    sum = 0
    for numero in array_numeros:
        if numero > 0 and numero % 2 == 0:
            sum += numero
    return sum


def conteo_negativos(array_numeros):
    cont = 0
    for numero in array_numeros:
        if numero < 0:
            cont += 1
    return cont


def promedio(array_numeros):
    sumatoria = 0
    cont = 0
    for numero in array_numeros:
        sumatoria += numero
        cont += 1
    return sumatoria / cont


def menor(array_numeros):
    menor = None
    for numero in array_numeros:
        if menor is None:
            menor = numero
        elif numero < menor:
            menor = numero
    return menor


def contar_repeticiones(num, array_numeros):
    cont = 0
    for n in array_numeros:
        if n == num:
            cont += 1
    return cont


def mas_repetido(array_numeros):
    num_mas_repetido = None
    cant_repeticiones_del_mas_repetido = 0
    for numero in array_numeros:
        cont = contar_repeticiones(numero, array_numeros)
        if num_mas_repetido is None:
            num_mas_repetido = numero
            cant_repeticiones_del_mas_repetido = cont
        elif cont > cant_repeticiones_del_mas_repetido:
            num_mas_repetido = numero
            cant_repeticiones_del_mas_repetido = cont
    return num_mas_repetido, cant_repeticiones_del_mas_repetido


def opcion6():
    array_copia = arr.array('i', range(TAM))
    for i in range(TAM):
        if i % 2 != 0 and numeros[i] > 0:
            array_copia[i] = numeros[i]
        else:
            array_copia[i] = 0 
    print("Arreglo original:")
    mostrar_numeros(numeros)
    print("\nArreglo copia:")
    mostrar_numeros(array_copia)
    print()


while opcion != '7':
    mostrar_menu()
    opcion = input("Seleccione la opción deseada: ")
    if opcion == '1':
        print(f"La sumatoria de los positivos pares es {sumatoria_positivos_pares(numeros)}")
    elif opcion == '2':
        print(f"El conteo de los negativos es {conteo_negativos(numeros)}")
    elif opcion == '3':
        print(f"El promedio de todos los valores es {promedio(numeros)}")
    elif opcion == '4':
        print(f"El menor de todos los valores es {menor(numeros)}")
    elif opcion == '5':
        print(f"El número que más veces se repite es {mas_repetido(numeros)}")
    elif opcion == '6':
        opcion6()
    elif opcion == '7':
        print("Gracias por utilzar el programa!")
    else:
        print("La opción ingresada no es válida!")