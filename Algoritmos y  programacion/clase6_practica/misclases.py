import utilities_c

libros = []
class Libros():
    
    def __init__(self, titulop, autorp, generop, num_de_pagp):
        self.titulo = titulop
        self.autor = autorp
        self.genero = generop
        self.num_de_pag = num_de_pagp
        
    def to_string(self):
        return print(f"""
    Informacion del libro
    Titulo: {self.titulo}| Autor: {self.autor}| Genero: {self.genero}| Numero de paginas: {self.num_de_pag}
    """)
    
class Biblioteca():
    
    def __init__(self):
        self.libros = libros
        
    def ingresar_libros(self, l1):
        self.libros.append(l1)

    def cargar_libros(b1):
        cant = 0
        flag = False
        while not flag:
            cant = utilities_c.es_entero_mayor_a_cero("¿Cuantos libros desea ingresar?: ")
            for i in range(cant):
                titulo = input('Ingrese el titulo del libro: ').upper()
                autor = input('Ingrese el nombre del autor: ').upper()
                genero = input('Ingrese El genero del libro: ').upper()
                num_pag = utilities_c.es_entero_mayor_a_cero('Ingrese el numero de paginas del libro: ')
                l1 = Libros(titulo, autor, genero, num_pag)
                b1.ingresar_libros(l1)
                print('Libro cargado correctamente!!')
            op = input("¿Desea ingresar mas libros? 'S' para si o enter para no: ").upper()
            if op == 'S':
                continue
            else:
                flag = not flag
    
    def buscar_libros(self):
        cont = 0
        titulo_aux = input('Ingrese el titulo del libro que quiera buscar: ').upper()
        for l in self.libros:
            if l.titulo == titulo_aux:
                l.to_string()
                cont += 1
        if cont == 0:
            print('Su titulo es incorrecto o el libro no existe en nuestra biblioteca!')
        else:
            return


    def mostrar_libros(self):
        cont = 0
        autor_aux = input('Ingrese el autor de los libros que quiera buscar: ').upper()
        for l in self.libros:
            if l.autor == autor_aux:
                l.to_string()
                cont += 1
        if cont == 0:
            print('El autor es incorrecto o no tenemos libros de ese autor en nuestra biblioteca!')
        else:
            return
