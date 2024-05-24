class Cliente:
    def __init__(self,Nombre,apellido,Telefono,Direccion,IdC):
        self.Nombre=Nombre
        self.Apellido=apellido
        self.Telefono=Telefono
        self.Direccion=Direccion
        self.IdC=IdC
    
    def __str__(self):
        return f"{self.IdC}, {self.Nombre}, {self.Telefono}, {self.Direccion}"

