## Ejercicio 040

### Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:
#- Suma de los numeros
#- La suma de los numeros entre a y b
#- La suma de los numeros pares entre a y b.  
#- El producto de los numeros impares entre a y b.

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if a > b:
    a,b = b,a
    
sum = 0
sum_pares = 0
prod_imp = 1
for contador in range(a,b+1):
    sum += contador
    if contador % 2 == 0:
        sum_pares += contador
    else: 
        prod_imp *= contador
   
print(f"La suma entre los numeros es: {a + b}")
print(f"La suma de los numeros entre a y b es : {sum}")
print(f"La suma de los numeros pares entre a y b es: {sum_pares}")  
print(f"El producto de los numeros impares entre a y b es: {prod_imp}")




