class Autos:
    def __init__(self,patente,marca,modelo,chofer,estadoA):
        self.Patente = patente
        self.Marca = marca
        self.Modelo = modelo
        self.Chofer = chofer
        self.EstadoA = estadoA
        
    def __str__(self):
        return f'Patente: {self.Patente} | Marca: {self.Marca} | Modelo: {self.Modelo} | Chofer: {self.Chofer} | Estado: {self.Estado}'
    
    def cambiar_estadoA(self, estado):
        self.EstadoA = estado
    
class cliente:
    def __init__(self,iDc,nombre,apellido,telefono,direccion,estadoC):
        self.iDc = iDc
        self.Nombre = nombre
        self.Apellido = apellido
        self.Telefono = telefono
        self.Direccion = direccion
        self.EstadoC = estadoC
        
    def __str__(self):
        return f'Nombre: {self.Nombre}, Apellido: {self.Apellido}, Telefono: {self.Telefono}, Direccion: {self.Direccion}'
    
    def cambiar_estadoC(self,estado):
        self.EstadoC = estado
            
class Reserva:
    def __init__(self,Idr,fecha,direccion, destino,estador,cliente, auto, precio):
        self.iDr = Idr
        self.Fecha = fecha
        self.Direccion = direccion
        self.Destino = destino
        self.EstadoR = estador
        self.Cliente = cliente
        self.Auto = auto
        self.Precio = precio
        
    def __str__(self):    
        return f'ID reserva: {self.iDr} | Fecha: {self.Fecha} | Direccion: {self.Direccion} | Destino: {self.Destino} | Estado: {self.EstadoR} | Auto: {self.Auto} | Precio: ${self.Precio}'
    
    def cambiar_estadoR(self, estado):
        self.EstadoR = estado
    
    
    
    
    
    
    
    