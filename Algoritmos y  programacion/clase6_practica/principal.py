import utilities
import matrices

matriz = []

def main():
    op = 0
    while op != 5:
        utilities.mostrar_menu()
        op = utilities.es_entero_mayor_a_cero("Ingrese una opcion: ")
        if op == 1:
            filas = utilities.es_entero_mayor_a_cero("Ingrese la cantidad de filas que tendra su matriz: ")
            columnas = utilities.es_entero_mayor_a_cero("Ingrese la cantidad de columnas que tendra su matriz: ")
            matrices.cargar_matriz(matriz, filas, columnas)
        elif op == 2:
            matrices.mostrar_matriz(matriz)
        elif op == 3:
            matrices.sumar_diagonal(matriz, filas)
        elif op == 4:
            matrices.buscar_el_maximo(matriz, filas, columnas)
        elif op == 5:
            print('Gracias por utilizar mi programa: ')
        else:
            print("Opcion Incorrecta!!")

main()