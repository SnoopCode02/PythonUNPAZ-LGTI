import Model,datetime
fecha_actual=datetime.date.today()
CostoKm=300

Autos=[]
Clientes=[]
Reservas=[]

def AgregarAuto():
    Patente=input("Ingrese la Patente del auto: ")
    Marca=input("Ingrese la Marca del auto: ")
    Modelo=input("Ingrese el modelo del auto: ")
    Chofer=input("Ingrese el chofer del auto: ")
    Auto=Model.Auto(Patente,Marca,Modelo,True,Chofer)
    Autos.append(Auto)
    print("Operacion exitosa")

def ModificarEstadoAuto(Patente,Estado):
    count=0
    for i in Autos:
        if Patente == i.Patente:
            i.ModificarEstado(Estado)
            count +=1
            print("Operacion exitosa")
    if count == 0:
        print(f"No existe ningun auto con la patente {Patente}")


def ModificarChoferAuto(Patente,Chofer):
    count=0
    for i in Autos:
        if Patente == i.Patente:
            i.ModificarChofer(Chofer)
            count += 1
            print("Operacion exitosa")
    if count == 0:
        print(f"No existe ningun auto con la patente {Patente}")

def MostrarAutos():
    if len(Autos) == 0:
        print("No existen autos en la base de datos")
    else:
        for i in Autos:
            print(i)

def MostrarDisponibles():
    count=0
    if len(Autos) == 0:
        print("No existen autos en la base de datos")
    else:
        for i in Autos:
            if i.EstadoA == True:
                print(i)
                count +=1
        if count == 0:
            print("Por el momento no hay autos disponibles")

def MostrarEstado(Patente):
    count=0
    if len(Autos) == 0:
        print("No existen autos en la base de datos")
    else:
        for i in Autos:
            if i.Patente == Patente:
                return i
        if count == 0:
            print(f"No existe ningun auto con la patente {Patente}")

        
def AgregarCliente():
    Id=len(Clientes)+1
    Nombre=input("Ingrese el nombre del cliente: ")
    Telefono=input("Ingrese el telefono del cliente: ")
    Direccion=input("Ingrese la direccion del cliente: ")
    cliente=Model.Cliente(Nombre,Telefono,Direccion,Id,True)
    Clientes.append(cliente)
    print("Operacion exitosa")

def HabilitarCliente(Id):
    count=0
    if len(Clientes) == 0:
        print("No existen clientes en la base de datos")
    else:
        for i in Clientes:
            if i.IdC == Id:
                i.ModificarEstadoClientes(True)
                count += 1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ningun cliente con ID {Id}")

def DeshabilitarCliente(Id):
    count=0
    if len(Clientes) == 0:
        print("No existen clientes en la base de datos")
    else:
        for i in Clientes:
            if i.IdC == Id:
                i.ModificarEstadoClientes(False)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ningun cliente con ID {Id}")

def MostrarClientes():
    if len(Clientes) == 0:
        print("No existen clientes en la base de datos")
    else:
        for i in Clientes:
            print(i)

def BuscarClienteId(Id):
    count=0
    if len(Clientes) == 0:
        print("No existen clientes en la base de datos")
    else:
        for i in Clientes:
            if i.IdC == Id:
                print(i)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ningun cliente con ID {Id}")

def BuscarClienteTelefono(Telefono):
    count=0
    if len(Clientes) == 0:
        print("No existen clientes en la base de datos")
    else:
        for i in Clientes:
            if i.Telefono == Telefono:
                print(i)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ningun cliente con Telefono: {Telefono}")


def IngresarReservaAhora():
    IdR= len(Reservas)+1
    Fecha=fecha_actual
    Direccion= input("ingrese la dirección de origen: ")
    Destino= input("Ingrese la direccion de destino: ")
    Auto= input("Ingrese la patente del auto asignado: ")
    Km= int(input("Ingrese la cantidad de KM del viaje: "))
    Precio=Km * CostoKm
    Cliente= int(input("ingrese el ID del cliente: "))
    Reserva=Model.Reserva(IdR,Fecha,Direccion,Destino,Auto,True,Precio,Cliente)
    ModificarEstadoAuto(Auto,False)
    Reservas.append(Reserva)
    print(f"Operación exitosa!, su numero de reserva se registro con el número: {IdR}")

def IngresarReservaConFecha():
    IdR= len(Reservas)+1
    Fecha=input("ingrese la fecha de la reserva (AAAA-MM-DD): ")
    Direccion= input("ingrese la dirección de origen: ")
    Destino= input("Ingrese la direccion de destino: ")
    Auto= input("Ingrese la patente del auto asignado: ")
    Km= int(input("Ingrese la cantidad de KM del viaje: "))
    Precio=Km * CostoKm
    Cliente= int(input("ingrese el ID del cliente: "))
    Reserva=Model.Reserva(IdR,Fecha,Direccion,Destino,Auto,True,Precio,Cliente)
    ModificarEstadoAuto(Auto,False)
    Reservas.append(Reserva)
    print(f"Operación exitosa!, su numero de reserva se registro con el número: {IdR}")

def ConfirmarReserva(Id):
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.IdR == Id:
                i.ModificarEstadoR(True)
                count += 1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ninguna reserva con ID {Id}")

def CancelarReserva(Id):
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.IdR == Id:
                i.ModificarEstadoR(False)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ninguna reserva con ID {Id}")

def MostrarReservasConfirmadas():
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.EstadoR == True:
                print(i)
                count +=1
        if count == 0:
            print("Por el momento no hay reservas confirmadas")

def MostrarReservasCanceladas():
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.EstadoR == False:
                print(i)
                count +=1
        if count == 0:
            print("Por el momento no hay reservas canceladas")

def MostrarReservas():
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            print(i)

def BuscarReservaId(Id):
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.IdR == Id:
                print(i)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ninguna reserva con ID {Id}")

def BuscarReservaPatente(Patente):
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.Auto == Patente:
                print(i)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ninguna reserva asociada a la patente: {Patente}")

def BuscarReservaCliente(id):
    count=0
    if len(Reservas) == 0:
        print("No existen reservas en la base de datos")
    else:
        for i in Reservas:
            if i.Cliente.IdC == id:
                print(i)
                count +=1
                print("Operacion exitosa")
    if count == 0:
        print(f"No existe ninguna reserva asociada a ese ID de cliente: {id}")