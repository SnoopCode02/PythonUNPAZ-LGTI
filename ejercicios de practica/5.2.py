""" 
5.2. Realiza un programa que permita el ingreso de dos cadenas de caracteres llame a
unas funciones programadas por ti que realicen las mismas tareas que la función
len( ) y strcmp( ) (Existentes en lenguaje C.)
len(str) -> myUDFcuentaCaracteres( )
strcmp( ) -> myUDFcomparaCadenas( )
"""
def cuenta_caracteres(string):
    contador = 0
    for i in string:
        contador += 1
    return contador
def compara_cadenas(string1, string2):
    if string1 == string2:
        return True
    else:
        return False
    
    

str1 = input("Ingrese la cadena 1: ")
str2 = input("Ingrese la cadena 2: ")

print(f"Funcion len con la primera cadena: {cuenta_caracteres(str1)}")
print(f"Funcion strcmp con la segunda cadena : {compara_cadenas(str1, str2)}")