'''
6. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo
por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''
h = float(input('Ingrese la cantidad de horas trabajadas: '))
c = float(input('Ingrese el coste por horas trabajadas: '))

print(f'Su sueldo es de: {h * c}$')