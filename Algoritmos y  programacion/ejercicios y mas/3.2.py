'''
2. Dado el siguiente código verificar si está bien escrito resuelva todo lo que se
pueda manualmente y agregue las excepciones necesarias.
'''
def introducir_entero_valido(mensaje):
    while True:
        num = input(mensaje).strip()
        try:    
            num = int(num)
            return int(num)    
        except ValueError:
            print(f"El numero: {num} no es un entero, presione enter para continuar.")
            input()
divisor = 1
acumulador = 0
listado_numeros=[]
while True:
    numero = introducir_entero_valido("Ingrese un numero para calcular y mostrar sus divisores: ")
    if numero >= 0:
        print(f"Los numeros divisores de {numero} son:")
        while divisor <= numero:
            if numero % divisor == 0:
                acumulador += divisor
                listado_numeros.append(divisor)
            divisor +=1
        break
    else:
        print("Debe ingresar un valor numérico entero positivo")
for i in range(len(listado_numeros)):
    print(f"{listado_numeros[i+1]:^30d}")
print(f"La suma de todos los divisores es de {acumulador}")


