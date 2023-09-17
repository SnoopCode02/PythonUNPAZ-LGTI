"""
mostrar la suma de cada sub secuencia
1 2 4 3 5 0 4 7 8 5 6 9 0 1 4 5 7 8 0 -1
"""
mayor_suma_sub = -float('inf')
suma_tot = 0
numero = int(input("numero: "))
while numero != -1:
    suma_sub = 0
    while numero !=0:
        suma_sub += numero
        suma_tot += numero
        numero = int(input("numero: "))
    #Fin del while
    print(f"La suma de la sub sec es: {suma_sub}")
    if suma_sub > mayor_suma_sub:
        mayor_suma_sub = suma_sub
    #otra forma de hacerlo suma_tot += suma_sub
    numero = int(input("numero: "))
#fin del while
print(f"Suma total: {suma_tot}")
print(f"La suma sub mayot es: {mayor_suma_sub}")

