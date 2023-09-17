"""hacer un algoritmo que solicite 10 números positivos, calcular y mostrar por 
pantalla cuantos son pares y cuantos impares"""
N = 10
cont_pares = 0
cont_impares = 0
cont_negativos = 0
for i in range(N) :
    num = -1
    while num <0:
        num = int(input(f"ingrese el {i+1}° numero: "))
        if num > 0:
            if num % 3 == 0:
                cont_pares += 1
            else: cont_impares += 1
        else:
            print(f"El numero {num} es negativo, debe ingresar un numero positivo!!")
            cont_negativos += 1

print(f"La cantidad de pares es {cont_pares}")
print(f"La cantidad de impares es {cont_impares}")
print(f"La cantidad de errores al ingresar números fue {cont_negativos}")