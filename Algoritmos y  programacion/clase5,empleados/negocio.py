import clases
import utilities
empleados = []

def carga_empleados():
    flag = False
    while not flag:
        cant = utilities.es_entero("¿Cuantos empleados desea cargar?: ")
        for i in range(cant): 
            iD = len(empleados) + 1
            nombre = input("Ingrese el nombre del empleado: ").upper()
            apellido = input("Ingrese el apellido del empleado: ").upper()
            #edad = utilities.es_entero("Ingrese la edad del empleado: ")
            while True:
                edad = utilities.es_entero("Ingrese la edad del empleado: ")
                if edad >= 18:
                    break
                else: 
                    print("El empleado debe ser mayor de 18 Años")
            while True:
                categoria = input("Ingrese la categoria del empleado, 'T' para temporal o 'P' para planta:  ").upper()
                if categoria == "T" or categoria == "P":
                    break
                else:
                    print("Ingrese una opcion correcta: 'T' o 'P'")
            sueldo = utilities.es_flotante("Ingrese el sueldo bruto del empleado: ")
            while True:
                estado = utilities.es_entero("Ingrese el estado del empleado '1' Para vigente o '0' para inactivo: ")
                if estado == 1 or estado == 0:
                    break
                else:
                    print("Ingrese una opcion correcta: '1' o '0': ")
            p1 = clases.Empleado(iD, nombre, apellido, edad, categoria, sueldo, estado)
            empleados.append(p1)
            print("Empleado cargado correctamente!")
            
        while True:
            op = input("¿Desea seguir ingresando empleados? 'S' para si o 'N' para no: ").upper()
            if   op == "S":
                break
            elif op == "N":
                flag =  not flag
                break
            else:
                print("Ingrese una opcion correcta!!")

def listar_empleados():
    cont = 0
    for e in empleados:
        if e.estado == 1:
            cont += 1
            print(f"""
ID: {e.Id}| Nombre: {e.nombre}| Apellido: {e.apellido}| Edad: {e.edad}| Categoria: {e.categoria}| Sueldo Bruto: {e.sueldo}| Sueldo Neto: {e.ObtenerSueldoNeto()}""")
    if cont == 0:
        print("No se encontraron empleados activos!")
    else: return
    
def listar_empleados_inactivos():
    cont = 0
    for e in empleados:
        if e.estado == 0:
            cont += 1
            print(f"""
ID: {e.Id}| Nombre: {e.nombre}| Apellido: {e.apellido}| Edad: {e.edad}| Categoria: {e.categoria}| Sueldo Bruto: {e.sueldo}| Sueldo Neto: {e.ObtenerSueldoNeto()}""")
    if cont == 0:
        print("No se encontraron empleados activos!")
    else: return

def buscar_por_id():
    loc_id = utilities.es_entero("Ingrese el ID del empleado: ")
    for e in empleados:
        if e.Id == loc_id:
            return print(f"""
ID: {e.Id}| Nombre: {e.nombre}| Apellido: {e.apellido}| Edad: {e.edad}| Categoria: {e.categoria}| Sueldo Bruto: {e.sueldo}| Sueldo Neto: {e.ObtenerSueldoNeto()}""")        
    print("Id incorrecto, por favor intentelelo nuevamente.")

def buscar_por_nombre():
    loc_nombre = input("Ingrese el Nombre del empleado: ").upper()
    loc_apellido = input("Ingrese el Apellido del empleado: ").upper()
    for e in empleados:
        if e.nombre == loc_nombre and e.apellido == loc_apellido:
            return print(f"""
ID: {e.Id}| Nombre: {e.nombre}| Apellido: {e.apellido}| Edad: {e.edad}| Categoria: {e.categoria}| Sueldo Bruto: {e.sueldo}| Sueldo Neto: {e.ObtenerSueldoNeto()}""")
    print("Id Nombre o apellido incorrectos, por favor intentelelo nuevamente.")

def buscar_por_categoria():
    cont = 0
    loc_cat = input("Ingrese La categoria del empleado 'T' o 'P': ").upper()
    for e in empleados:
        if e.categoria == loc_cat:
            print(f"""
ID: {e.Id}| Nombre: {e.nombre}| Apellido: {e.apellido}| Edad: {e.edad}| Categoria: {e.categoria}| Sueldo Bruto: {e.sueldo}| Sueldo Neto: {e.ObtenerSueldoNeto()}""")
            cont += 1
    if cont == 0:
        print("Categoria incorrecta, por favor intentelelo nuevamente.")
    else:
        return
        
def modif_empleado_nombre():
    loc_ID = utilities.es_entero("Ingrese el ID numerico del empleado a modificar su nombre: ")
    for e in empleados:
        if e.Id == loc_ID:
            print(f"Se encontro el empleado de Nombre y Apellido: {e.nombre} {e.apellido} edad: {e.edad}.")
            nom_loc = input("Ingrese el nuevo nombre del empleado: ").upper()
            e.nombre = nom_loc
            print("Nombre cambiado correctamente!!")
            return
    input("Id incorrecto, por favor intentelelo nuevamente.")
            
def modif_empleado_apellido():
    loc_ID = utilities.es_entero("Ingrese el ID numerico del empleado a modificar su apellido: ")
    for e in empleados:
        if e.Id == loc_ID:
            print(f"Se encontro el empleado de Nombre y Apellido: {e.nombre} {e.apellido} edad: {e.edad}.")
            ape_loc = input("Ingrese el nuevo Apellido del empleado: ").upper()
            e.nombre = ape_loc
            print("Apellido cambiado correctamente!!")
            return
    print("Id incorrecto, por favor intentelelo nuevamente.")
                           
def modif_empleado_categoria():
    loc_ID = utilities.es_entero("Ingrese el ID numerico del empleado a modificar: ")
    for e in empleados:
        if e.Id == loc_ID:
            if e.categoria == "T":
                op = input(f"""
Se encontro al empleado: {e.nombre} {e.apellido} de categoria '{e.categoria}': Temporal.
Desea cambiar su categoria?: 'S' para si o 'N' para no: """).upper()
                if op == 'S':
                    e.categoria = 'P'
                    return print("El empleado fue cambiado de categoria!")    
                elif op == 'N':
                    return print("No se efectuaron cambios!")
                        
            elif e.categoria == "P":
                op = input(f"""
Se encontro al empleado: {e.nombre} {e.apellido} de categoria '{e.categoria}': Planta.
Desea cambiar su categoria?: 'S' para si o 'N' para no: """).upper()
                if op == 'S':
                    e.categoria = 'T'
                    return print("El empleado fue cambiado de categoria!")
                elif op == 'N':
                    return print("No se efectuaron cambios.")
    print ("Id incorrecto, por favor intentelelo nuevamente.")
                
        
def borrar_empleado():
    cont = 0
    loc_ID = utilities.es_entero("Ingrese el ID numerico del empleado a eliminar: ")
    for e in empleados:
        if e.Id == loc_ID and e.estado == 1:
            e.estado = 0
            cont += 1
            return print(f"Se borro al empleado: {e.nombre} {e.apellido} con el id numero: {e.Id}")
    if cont == 0:
        print("El ID ingresado es incorrecto o ese empleado ya ah sido borrado.")
    else: return    
