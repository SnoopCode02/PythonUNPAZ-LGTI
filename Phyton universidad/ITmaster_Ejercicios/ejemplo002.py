"""
5 5 5 5 2 2 2 2 2 8 8 8 8 8 3 3 3 3 3 7 4 4 4 0

1 1 1 1 1 1 2 2 2 2 2 3 3 3 3 7 7 7 7 7 9 9 9 9 9 9 0
"""
#corte de control
cant_numeros = 0
numero = int(input("numero: "))
while numero != 0: #FIN DE DATOS
    numero_proceso = numero
    repet = 0
    while numero != 0 and numero_proceso == numero: #fin de datos y el mismo numero
        repet += 1
        #cant_numeros += 1
        numero = int(input("numero: "))
    #FIN NUMERO IGUAL
    print(f"numero: {numero_proceso} rep: {repet}")
    cant_numeros += repet
# FIN DE DATOS
print(f"LOS NUMEROS SE REPITEN: {cant_numeros}")


