class Cliente:
    def __init__(self,Nombre,Telefono,Direccion,IdC,EstadoC):
        self.Nombre=Nombre
        self.Telefono=Telefono
        self.Direccion=Direccion
        self.IdC=IdC
        self.EstadoC=EstadoC

    def ModificarEstadoClientes(self,EstadoC):
        self.EstadoC=EstadoC
    
    def __str__(self):
        return f"Id: {self.IdC} | Nombre: {self.Nombre} | Telefono: {self.Telefono} | Direccion: {self.Direccion} | Estado: {self.EstadoC}"

class Auto:
    def __init__(self,Patente,Marca,Modelo,EstadoA,Chofer):
        self.Marca=Marca
        self.Modelo=Modelo
        self.Patente=Patente
        self.EstadoA=EstadoA
        self.Chofer=Chofer

    def ModificarEstado(self,EstadoA):
        self.EstadoA=EstadoA
    
    def ModificarChofer(self,Chofer):
        self.Chofer=Chofer

    def __str__(self):
        return f"Patente: {self.Patente} | Marca: {self.Marca} | Modelo: {self.Modelo} | Chofer: {self.Chofer} | Disponible: {self.EstadoA}"

class Reserva:
    def __init__(self,IdR,Fecha,Direccion,Destino,Auto,EstadoR,Precio,Cliente):
        self.IdR=IdR
        self.Fecha=Fecha
        self.Direccion=Direccion
        self.Destino=Destino
        self.Precio=Precio
        self.Auto=Auto
        self.EstadoR=EstadoR
        self.Cliente=Cliente

    def ModificarEstadoR(self,EstadoR):
        self.EstadoR=EstadoR
    
    def __str__(self):
        return f"ID Reserva: {self.IdR} | Fecha: {self.Fecha} | Origen: {self.Direccion} | Destino: {self.Destino} | Precio: ${self.Precio} | Auto asignado: {self.Auto} | Estado: {self.EstadoR} | Cliente: {self.Cliente}"