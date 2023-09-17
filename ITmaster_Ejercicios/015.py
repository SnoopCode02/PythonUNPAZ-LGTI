"""
Ejercicio 015

Definición del problema: Una inmobiliaria paga a sus vendedores un salario base,
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas.
Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde
en un determinado mes. 
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó 
y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?
"""
base = int(100000)
nombre = input("Cual es su nombre?: ")
ventas = int(input("Cuantas ventas realizo?: "))
valor_ventas = int(input("¿Cual es el valor total de las ventas?: "))
venta_unitaria = round(valor_ventas/ventas,2)
comision = round((venta_unitaria * 3) / 100,2)
cinco_porcent_ventas = round((valor_ventas * 5) / 100,2)
sueldo__total = (comision * ventas) + cinco_porcent_ventas + base
print(f"""
                Sueldo total
              
{nombre}: {sueldo__total}      
      """)



