"""
Ejercicio 011

Escribir un programa que permita resolver el siguiente problema: 
Tres personas aportan diferente capital a una sociedad y desean saber
el valor total aportado y qué porcentaje aportó cada una 
(indicando nombre y porcentaje). 
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, 
a partir de esto calcular e informar lo requerido previamente.
"""
name1 = input("Ingrese su nombre: ")
capital1 = float(input("Ingrese el valor de su inversion: "))

name2 = input("Ingrese su nombre: ")
capital2 = float(input("Ingrese el valor de su inversion: "))

name3 = input("Ingrese su nombre: ")
capital3 = float(input("Ingrese el valor de su inversion: "))

total_inversion = capital1 + capital2 + capital3

porcen1 = round((capital1 / total_inversion) * 100, 2)
porcen2 = round((capital2 / total_inversion) * 100, 2)
porcen3 = round((capital3 / total_inversion) * 100, 2)

print(f"""Se invirtio un total de {total_inversion}$
Cada persona invirtio 
{name1}: {porcen1}%
{name2}: {porcen2}%
{name3}: {porcen3}%""")