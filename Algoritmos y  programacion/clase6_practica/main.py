import utilities_c
import misclases

def main():
    op = 0
    while op != 4:
        utilities_c.mostrar_menu()
        op = utilities_c.es_entero_mayor_a_cero("Ingrese una opcion: ")
        if op == 1:
            b1 = misclases.Biblioteca()
            misclases.Biblioteca.cargar_libros(b1)
        elif op == 2:
            b1.buscar_libros()
        elif op == 3:
            b1.mostrar_libros()
        elif op == 4:
            print('Gracias por utilizar mi programa')

main()