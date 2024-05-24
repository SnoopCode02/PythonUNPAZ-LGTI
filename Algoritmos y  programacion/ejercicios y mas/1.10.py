'''
Utilizando un ciclo for, ingresa un lote de 10 números y asegúrate de validar que todos sea
n positivos.
a) Luego, determina cuántos números mayores que 10 se han ingresado. En caso contrario, muestra un mensaje indicando que no se han ingresado números mayores que 10.
b) Además, calcula y comunica el promedio de los números ingresados que sean mayores a 10.

2-
Solicita el ingreso de un lote de 10 números, los cuales pueden ser tanto positivos como negativos.
a) Identifica y muestra el número más grande que ha sido ingresado.

3-
Ingesta un conjunto de 10 números, asegurándote de validar que todos sean positivos.
a) Luego, informa la cantidad de números pares ingresados y calcula su promedio.
b) También, comunica la cantidad de números impares ingresados y determina su promedio
'''

numero = 0
cont = 0
sum = 0
for i in range(10):
    while True:
        numero = int(input(f"ingrese el numero {i+1}: "))
        if numero >= 0:
            break
        else:
            print("Debe ingresar un numero entero!!")
    #if numero > 10:
    cont = cont +1
    

        
    
if cont == 0:
    print('No se ingresaron numero mayores a 10!')
else:
    print("los numeros mayores a 10 son: ",cont)
    
