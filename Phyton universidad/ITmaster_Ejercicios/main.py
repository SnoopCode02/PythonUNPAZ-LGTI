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
    return LIM_INF <= int(numero) <= LIM_SUP

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


def conteo_negativos(array_numeros):
    cont = 0
    for numero in array_numeros:
        if numero < 0:
            cont += 1
    return cont

def sumatoria_positivos_pares(array_numeros):
    sum = 0
    for numero in array_numeros:
        if numero > 0 and numero % 2 != 0:
            sum += numero
    return sum

def promedio_positivos(array_numeros):
    sumatoria = sumatoria_positivos_pares(array_numeros)
    cont = 0
    for numero in array_numeros:
        if numero > 0:
            
            cont += 1
    
    return sumatoria / cont 

def es_primo(numero):
    es_primo = False
    cant_divisores = 0
    for i in range(numero):
        if numero % (i + 1) == 0:
            cant_divisores += 1

    if cant_divisores == 2:
        es_primo = True
    return es_primo


def menor_de_los_primos(array_numeros):
    menor = None
    for numero in array_numeros:
        if es_primo(numero):
            print("s")
            if menor is None:
                menor = numero
            elif numero < menor:
                menor = numero
    return menor

def negativo_mas_repetido():
    pass

def opcion7():
    pass

def mostrar_menu():
    print("---- MENU ----")
    print("1- Mostrar numeros cargados")
    print("2- Realizar la sumatoria de los valores positivos impares")
    print("3- Realizar el conteo de los valores negativos")
    print("4- Calcular el promedio de todos los valores positivos ingresados")
    print("5- Obtener el menor de todos los primos ingresados. Mostrar aviso en caso que no se hayan ingresados numeros primos")
    print("6- Obtener el número negativo que más veces se repite en el vector. Mostrar aviso en caso de que no se hayan ingresado números negativos")
    print("7- Generar un vector destino y copiar (en las mismas posiciones del arreglo original) los valores positivos que superen el promedio calculado en el punto 4, en el resto de posiciones copiar el valor 0")
    print("8- Salir del programa")
    
for i in range(TAM):
    numero = ""
    while not (es_numero_entero(numero) and esta_el_numero_dentro_del_intervalo(numero)):
        numero = leer_numero_entero_valido(f"Ingrese el {i + 1}° número: ")
    numeros[i] = numero
print()
opcion = ""



while opcion != '8':
    mostrar_menu()
    opcion = input("Seleccione la opción deseada: ")
    if opcion == '1':
        print(f"{mostrar_numeros(numeros)}")
    elif opcion == '2':
        print(f"La sumatoria de los positivos impares es {sumatoria_positivos_pares(numeros)}")
    elif opcion == '3':
        print(f"El conteo de los negativos es {conteo_negativos(numeros)}")
    elif opcion == '4':
        print(f"El promedio de todos los valores positivos es {promedio_positivos(numeros)}")
    elif opcion == '5':
            if menor_de_los_primos(numeros) == None:
                print("No se cargaron numeros primos")
            else:
                print(f"El menor de todos los primos es {menor_de_los_primos(numeros)}")
    elif opcion == '6':
        print(f"El número que más veces se repite es {negativo_mas_repetido(numeros)}")
    elif opcion == '7':
        opcion7()
    elif opcion == '8':
        print("Gracias por utilzar el programa!")
    else:
        print("La opción ingresada no es válida!")