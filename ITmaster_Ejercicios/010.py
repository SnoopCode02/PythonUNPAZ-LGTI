"""
Ejercicio 010

Escribir un programa para resolver el siguiente problema:
Tres personas invierten dinero para fundar una empresa (no necesariamente en partes
iguales).

Calcular qué porcentaje invirtió cada una.

Como pensarlo:

- 1 Solicitar al usuario que ingrese las cantidades invertidas por cada persona en 
tres variables numéricas. 


- 2 Calcular el total de la inversión sumando las cantidades de las tres personas.  


- 3 Calcular el porcentaje que representa la inversión de cada persona en relación
 al total de la inversión.

- 3 - 1 Dividir la cantidad invertida por cada persona entre el total de la
inversión y multiplicar por 100 para obtener el porcentaje.
Almacenar el resultado en una variable correspondiente a cada persona.
Opcionalmente, se puede redondear el resultado a un número determinado de 
decimales utilizando la función round().

- 4 Mostrar por pantalla el porcentaje de inversión de cada persona.
"""
persona1 = float(input("Ingrese el valor de la inversion de la persona 1: "))
persona2 = float(input("Ingrese el valor de la inversion de la persona 2: "))
persona3 = float(input("Ingrese el valor de la inversion de la persona 3: "))
total_inversion = persona1 + persona2 + persona3
porcen1 = round((persona1 / total_inversion) * 100, 2)
porcen2 = round((persona2 / total_inversion) * 100, 2)
porcen3 = round((persona3 / total_inversion) * 100, 2)
print(f"""El porcentaje de inversion de cada persona es: 
Persona1: {porcen1}%
Persona2: {porcen2}%
Persona3: {porcen3}%""")