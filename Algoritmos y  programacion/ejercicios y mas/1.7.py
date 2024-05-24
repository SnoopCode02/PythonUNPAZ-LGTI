'''
7. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada
payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
'''
MUÑE = 75
PAYA = 112

vendi_muñe = int(input('Ingrese la cantidad de muñecas vendidos: '))
vendi_paya = int(input('Ingrese la cantidad de payasos vendidos: '))
peso_muñe = vendi_muñe * MUÑE
peso_paya = vendi_paya * PAYA

peso_caja = peso_muñe + peso_paya
print(f"El peso total de la caja es: {peso_caja}" )

