## Ejercicio 035

### Existen dos reglas que identifican dos conjuntos de valores:  
### a) El número es de un solo dígito.  
### b) El número es impar.  

### A partir de estas reglas, escribir un programa que permita ingresar un número entero.
### Debe asignar el valor que corresponda a las variables booleanas:  
"""
- esDeUnSoloDigito  
- esImpar  
- estaEnAmbos  
- noEstaEnNinguno  
"""
### el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. }Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.

from random import randint

for i in range(10):
    flag = False
    num1 = randint(0,100)
#    while not flag:
 #       num1 = input(f"ingrese el {i+1}° numero entero: ")
 #       if num1.isdecimal():
  #          num1 = int(num1)
 #           flag = not flag
   #     else:
     #       print("Ingrese un valor numerico!")

    if 0 <= num1 < 10:
        esDeUnSoloDigito = True
    else: esDeUnSoloDigito = False
    if num1 % 2 != 0:
        esImpar = True
    else:
        esImpar = False
    if esImpar == True and esDeUnSoloDigito == True:
        estaEnAmbos = True
        noEstaEnNinguno = False
    else:
        estaEnAmbos = False
    if esImpar == True or esDeUnSoloDigito == True:
        noEstaEnNinguno = False
    elif esImpar == False and esDeUnSoloDigito == False:
        noEstaEnNinguno = True
    print(f"El numero es: {num1}\nEs de un solo digito? ==> {esDeUnSoloDigito}\nEs impar?==> {esImpar}\nEsta en ambos? ==> {estaEnAmbos}\nNo esta en ninguno? ==> {noEstaEnNinguno}")
