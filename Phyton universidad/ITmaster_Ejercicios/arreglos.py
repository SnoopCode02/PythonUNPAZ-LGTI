"""
arreglos de tipo "d" = float  y "i" = int.
"""
import array as arr  #importo el modulo del arreglo 
num_list = [5,4,5,3,2,5]
num_array = arr.array('i', num_list) #defino mi arreglo y le doy valores.

#se puede recorrer el arreglo usando indices
print(num_array[0]) #Primera posicion, siempre comienzan en 0
print(num_array[2]) #tercera posicion 
print(num_array[-1]) #Ultima posicion, se usa el "-" para comenzar desde el otro lado

#se pueden rebanar o cortar los arreglos con este elemento ':'
print(num_array[2:5]) # 3ro to 5t0
print(num_array[:-5]) # comienzo to 4to
print(num_array[5:])  # 6to to end
print(num_array[:])   # beginning to end

#se pueden cambiar y agregar elementos en un arreglo 
#se puede cambiar de una forma parecida a una lista

num_array[0] = 0
print(num_array)  #cambia el primer elemento por un 0

num_array[2:5] = arr.array('i', [4, 5, 6])
print(num_array) #cambia del tercer elemento al 5to

#Se pueden cambiar uno o varios elementos de un arreglo 
#Para agregar un solo elemento se usa el metodo append() "agrega" 
num2_array = arr.array('i', [2, 3, 4])

num2_array.append(5)
print(num2_array)

#Para agregar varios elementos se usa el metodo extend()
# extend() agrega varios elementos iterables al final de un arreglo
num2_array.extend([3, 4, 5])
print(num2_array)

#Tambien se pueden concatenar 2 arreglos con el simbolo "+"
num_juntos = arr.array('i') #se crea un arreglo vacio
num_juntos = num_array + num2_array
print(num_juntos)

#Tambien se puede eliminar elementos de un arreglo con la declaracion de python "del"
del num_juntos[1] #este elimina el segundo elemento del arreglo
print(num_juntos)

del num_juntos #este borra todo el arreglo 
#print(num_juntos)

#se puede eliminar un elemento dado del arreglo con 2 metodos

print(num2_array)
num2_array.remove(3) #Este elimina el primer elemento "3" que encuentra 
print(num2_array)

num2_array.pop(3) #Y este elimina el elemento en la posicion 3
print(num2_array)

#Diferencias entre listas y arreglos
#Diferentes elementos en una lista
a = [1, 2, "hello"]

#si tu creas un arreglo con el modulo 'array' todos los elementos tienen que ser del mismo tipo numerico
#error
a = arr.array('d',[2, 3.5, "hello"])



