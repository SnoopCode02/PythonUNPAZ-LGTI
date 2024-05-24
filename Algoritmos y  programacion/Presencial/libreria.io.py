import io

'''datos = open("oto.txt",'w')
#print(type(nombre_obj_archivo))

frase1 = 'Eta linea de texto la escribiremos en nuestro archivo'
datos.write(frase1)

datos.write('\nEsta es otra linea de manera diferente')

datos.close()

datos = open("oto.txt",'r')

contenido = datos.read()

print(contenido)
cont_lista = datos.readlines()

print(cont_lista)
print()
datos.close()

for i in cont_lista:
    print(i.strip('\n'))'''

'''
pisando el archivo
arch = open('otro_archivo.txt', 'w')
arch.write('estoy creando un archivo nuevo')
arch.close()

arch = open('otro_archivo.txt', 'r+')
arch.write('\notro tex...')

arch.seek(0)
print(arch.read())              
arch.close'''

'''imprimir sin pisar, posicionar el puntero
arch = open('otro_archivo.txt', 'w')
arch.write('estoy creando un archivo nuevo')
arch.close()

arch = open('otro_archivo.txt', 'r+')
arch.seek(len(arch.read()))
arch.write('\notro tex...')

arch.seek(0)
print(arch.read())              
arch.close'''

'''arch = open('modif_archivo.txt', 'w')
arch.write('Linea 1 esta es la primera linea')
arch.write('\nLinea 3 esta es la tercera linea')
arch.write('\nLinea 2 esta es la segunda linea')
arch.close()


arch = open('modif_archivo.txt', 'r+')
line = arch.readlines()
line[1] = '\nLinea 2 esta es la segunda linea'
line[2] = '\nLinea 3 esta es la tercera linea'

arch.seek(0)
arch.writelines(line)
print(arch.read())
arch.close()

arch = open('modif_archivo.txt', 'r')
print(arch.read())
arch.close()'''           



