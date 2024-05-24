import csv
class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Alumnos:
    def __init__(self):
        self.alumnos = []
        
    def agregar_alumnos(self, alumno):
        self.alumnos.append(alumno)
        
    def guardar_alumno(self, archivo):
        whit open(archivo, mode = 'w', newline = '') as arch:
            writer = csv.writer(arch, delimiter = ";")
            writer.writerrow(["Nombre", "Apellido"])
            for alumno in self.alumnos:
                writer.writerrow([alumno.nombre, alumno.apellido])

    def cargar_alumnos(self, archivo):
        try:
            whit open(archivo) as arch:
                reader = csv.reader(arch, delimiter) = ";"
                next(reader)
                print(f"{'NRO':^3}{'Nombre':^25}{'Apellido':^25}")
                for pos, row in enumerate(reader):
                    nombre, apellido = row
                    print(f"{pos:^3}{nombre:^25}{apellido:^25}")
                    self.agregar_alumno(Alumno(nombre,apellido))
            return true
        
        except FileNotFoundError:
            opcion = input(f"El archivo {archivo} no existe,\
Desea crearlo ? Si o No :").upper()
            if opcion == 'S':
                whit open(archivo, mode = 'w', newline = '') as arch:
                    writer = csv.writer(arch, delimiter = ";")
                    writer.writerow(['Nombre', 'Apellido'])
                    return True
            else:
                return False
            