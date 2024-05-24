import utilities
import negocio

def main():
    op = 0
    while op != 7:
        op2 = 0
        op3 = 0
        utilities.mostrar_menu()
        op =  utilities.es_entero('Ingrese una opcion: ')
        if op == 1:
            negocio.carga_empleados()
        elif op == 2:
            negocio.listar_empleados()
        elif op == 3:
            negocio.listar_empleados_inactivos()
        elif op == 4:
            while op2 != 4:
                utilities.mostrar_buscador()
                op2 = utilities.es_entero("Ingrese una opcion: ")
                if op2 == 1:
                    negocio.buscar_por_id()
                elif op2 == 2:
                    negocio.buscar_por_nombre()
                elif op2 == 3:
                    negocio.buscar_por_categoria()
                else:
                    print("Ingrese una opcion valida!")       
        elif op == 5:
            while op3 != 4:
                utilities.mostrar_modificador()
                op3 = utilities.es_entero("Ingrese una opcion: ")
                if op3 == 1:
                    negocio.modif_empleado_nombre()
                elif op3 == 2:
                    negocio.modif_empleado_apellido()
                elif op3 == 3:
                    negocio.modif_empleado_categoria()
                else:
                    print("Ingrese una opcion valida!")    
        elif op == 6:
            negocio.borrar_empleado()
        elif op == 7:
            print("Gracias por utilizar el programa: ")

main()