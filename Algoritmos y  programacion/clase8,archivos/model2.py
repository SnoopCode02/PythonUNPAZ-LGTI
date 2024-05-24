class Cliente:
    def __init__(self, codigo, nombre, direccion, saldo):
       self.codigo = codigo
       self.nombre = nombre
       self.direccion = direccion
       self.saldo = saldo

    def __str__(self):
        return f"{self.codigo} {self.nombre} {self.direccion} {self.saldo}"