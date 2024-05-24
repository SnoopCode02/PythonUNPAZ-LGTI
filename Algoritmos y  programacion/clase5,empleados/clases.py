class Empleado:
    def __init__(self, Id, nombre, apellido, edad, categoria, sueldo, estado):
        self.Id = Id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad  
        self.categoria = categoria
        self.sueldo = sueldo
        self.estado = estado

    def __str__(self):
        cadena = self.nombre+" "+self.apellido
        return cadena

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtenerSueldoBruto(self):
        return self.sueldo

    def ObtenerSueldoNeto(self):
        return self.sueldo * .83

    def obtenerid(self):
        return self.Id
    
    def obtener_categoria(self):
        return self.categoria