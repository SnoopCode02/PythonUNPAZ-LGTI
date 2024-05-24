import Negocio
import Utils

opcion=0
opcion2=0
opcion3=0
opcion4=0
opcion5=0
opcion6=0
opcion7=0
opcion8=0
opcion9=0

while opcion != 4:
    try:
        Utils.MenuPrincipal()
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            while opcion2 != 6:
                Utils.MenuAutos()
                opcion2=int(input("Ingrese una opcion: "))
                if opcion2 == 1:
                    Negocio.AgregarAuto()
                elif opcion2 == 2:
                    patente=input("Ingresar la patente del auto: ")
                    chofer=input("Ingresar el nombre del nuevo chofer: ")
                    Negocio.ModificarChoferAuto(patente,chofer)
                elif opcion2 == 3:
                    Negocio.MostrarDisponibles()
                elif opcion2 == 4:
                    Negocio.MostrarAutos()
                elif opcion2 == 5:
                    patente=input("Ingresar la patente del auto: ")
                    print(Negocio.MostrarEstado(patente))
                elif opcion2 < 0 or opcion2 > 6:
                    print("ERROR: Ingrese una opcian valida")
            opcion2=0
        elif opcion == 2:
            while opcion3 != 6:
                Utils.MenuClientes()
                opcion3=int(input("Ingrese una opcion: "))
                if opcion3 == 1:
                    Negocio.AgregarCliente()
                elif opcion3 == 2:
                        IdCliente=int(input("Ingrese el ID del cliente a deshabilitar: "))
                        Negocio.DeshabilitarCliente(IdCliente)
                elif opcion3 == 3:
                        IdCliente=int(input("Ingrese el ID del cliente a habilitar: "))
                        Negocio.HabilitarCliente(IdCliente)
                elif opcion3 == 4:
                    Negocio.MostrarClientes()
                elif opcion3 == 5:
                    while opcion5 != 3:
                        Utils.MenuClientesBuscar()
                        opcion5=int(input("Ingrese una opcion: "))
                        if opcion5 == 1:
                            IdCliente=int(input("Ingrese el ID del cliente a buscar: "))
                            Negocio.BuscarClienteId(IdCliente)
                        elif opcion5 == 2:
                            Telefono=input("Ingrese el numero de telefono del cliente a buscar: ")
                            Negocio.BuscarClienteTelefono(Telefono)
                        elif opcion5 < 0 or opcion5 > 4:
                            print("ERROR: Ingrese una opcian valida")
                    opcion5=0
                elif opcion3 < 0 or opcion3 > 7:
                    print("ERROR: Ingrese una opcian valida")
            opcion3=0
        elif opcion == 3:
            while opcion4 != 7:
                Utils.MenuReservas()
                opcion4=int(input("Ingrese una opcion: "))
                if opcion4 == 1:
                    while opcion7 != 4:
                        Utils.SubMenuReservas()
                        opcion7=int(input("Ingrese una opcion: "))
                        if opcion7 == 1:
                            Negocio.MostrarDisponibles()
                        elif opcion7 == 2:
                            Negocio.IngresarReservaAhora()
                        elif opcion7 == 3:
                            Negocio.IngresarReservaConFecha()
                        elif opcion7 < 0 or opcion7 > 4:
                            print("ERROR: Ingrese una opcian valida")
                    opcion7=0
                elif opcion4 == 2:
                    while opcion8 != 3:
                        Utils.MenurReservaEstado()
                        opcion8=int(input("Ingrese una opcion: "))
                        if opcion8 == 1:
                            IdReserva=int(input("Ingrese el ID correspondiente a la reserva: "))
                            Negocio.ConfirmarReserva(IdReserva)
                        elif opcion8 == 2:
                            IdReserva=int(input("Ingrese el ID correspondiente a la reserva: "))
                            Negocio.CancelarReserva(IdReserva)
                        elif opcion8 < 0 or opcion8 > 3:
                            print("ERROR: Ingrese una opcian valida")
                    opcion8=0
                elif opcion4 == 3:
                    Negocio.MostrarReservasConfirmadas()
                elif opcion4 == 4:
                    Negocio.MostrarReservasCanceladas()
                elif opcion4 == 5:
                    Negocio.MostrarReservas()
                elif opcion4 == 6:
                    while opcion9 != 4:
                        Utils.MenuReservasBuscar()
                        opcion9=int(input("Ingrese una opción: "))
                        if opcion9 == 1:
                            IdReserva=int(input("Ingrese el ID correspondiente a la reserva: "))
                            Negocio.BuscarReservaId(IdReserva)
                        elif opcion9 == 2:
                            patente=input("Ingrese una patente: ")
                            Negocio.BuscarReservaPatente(patente)
                        elif opcion9 == 3:
                            IdCliente=int(input("Ingrese el ID del cliente: "))
                            Negocio.BuscarReservaCliente(IdCliente)
                        elif opcion9 < 0 or opcion9 > 4:
                            print("ERROR: Ingrese una opcian valida")
                    opcion9=0
                elif opcion4 < 0 or opcion4 > 7:
                    print("ERROR: Ingrese una opcian valida")
            opcion4=0
        elif opcion < 0 or opcion > 4:
            print("ERROR: Ingrese una opcian valida")
    except:
        print("ERROR: ingrese un caracter válido")
print("Programa finalizado")