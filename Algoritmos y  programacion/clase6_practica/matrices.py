import utilities

def cargar_matriz(matriz, filas, columnas):
    matrizloc = matriz
    for f in range(filas):
        matrizloc.append([0]*columnas)
        
    for f in range(filas):
        for c in range(columnas):
            matrizloc[f][c] = utilities.es_entero(f"Ingrese el numero para la posicion: {f}-{c}: ")
            
def mostrar_matriz(matriz):
    for i in matriz:
        print(i)

            
def sumar_diagonal(matriz, filas):
    suma_diagonal = 0
    for i in range(filas):
        suma_diagonal += matriz[i][i]
    if suma_diagonal != 0:
        return print(f"La suma diagonal de su matriz es: {suma_diagonal}.")
    else:
        return print(f"La matriz no fue cargada!!")

def buscar_el_maximo(matriz, filas, columnas):
    maximo = 0
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] > maximo:
                maximo = matriz[f][c]
    return print(f"El numero mayor dentro de su matriz es {maximo}.")