"""
## Ejercicio 033

La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala: 

- Menor de $5500.0 el descuento es del 4.5%  
- Entre $5500.0 y $10000.0 el descuento es del 8%  
- Más de $10000.0 el descuento es del 10.5%  

Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.
"""
importe = ""
flag = False
while not flag:
    importe = input("Ingrese el importe total: ")
    if importe.isdigit():
        importe = float(importe)
        flag = True
    else:
        print("Por favor ingrese un caracter numerico: ")
DESC_MINIMO = (importe * 0.045)
DESC_MEDIO = (importe * 0.08)
DESC_MAXIMO = (importe * 0.105)

if importe < 5500.0:
    print(f"El descuento es de: {DESC_MINIMO}$\nDebe pagar: {importe - DESC_MINIMO}$")
elif 5500 <= importe < 10000:
    print(f"El descuento es de: {DESC_MEDIO}$\nDebe pagar: {importe - DESC_MEDIO}$")
else:
    print(f"El descuento es de: {DESC_MAXIMO}$\nDebe pagar: {importe - DESC_MAXIMO}$")
