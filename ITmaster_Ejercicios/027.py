## Ejercicio 027

### Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.
EDAD_MASC = 65
EDAD_FEM = 60 

edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su genero: ").upper()
nombre = input("Ingrese su nombre: ").title()

if genero == "M":
    se_jubila = edad >= EDAD_MASC
else:
    print("Por favor ingrese un genero valido, F para masculino, M para femenino.")
if genero == "F":
    se_jubila = edad >= EDAD_FEM
else:
    print("Por favor ingrese un genero valido, F para masculino, M para femenino.")
    
if se_jubila:
    print(f"{nombre} Genero: {genero} se jubila.")
else: 
    print(f"{nombre} Genero: {genero} no se jubila.")
