"""
## Ejercicio 034
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:
- Jubilación: 11%  

- Obra Social: 3%  

- Sindicato: 3%  
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)

Estado Civil: Soltero/Casado
Sueldo básico: $ 999.99
Antigüedad: 99 años

Descuentos:

- Jubilación - 999,99  

- Obra Social - 999,99  

- Sindicato - 999,99  

Sueldo Neto 999,99
"""
sueldo_basico = ""
antiguedad = ""
estado_civil = ""
flag = False
flag2 =False
flag3 =False

AUMEN_SOLTERO = 1.05
AUMEN_CASADO = 1.07
DESC_OBRA_SOCIAL = 0.11
DESC_SINDICATO = 0.03
DESC_JUBILACION =  0.03

while not flag:
    sueldo_basico = input("ingrese su sueldo basico: ")
    if sueldo_basico.isdecimal():
        sueldo_basico = int(sueldo_basico)
        flag = not flag
    else: 
        print("Por favor ingrese un valor numerico!")
        
while not flag2:
    antiguedad = input("ingrese sus años de antiguedad: ")
    if antiguedad.isdecimal():
        antiguedad = int(antiguedad)
        flag2 = not flag2
    else: 
        print("Por favor ingrese un valor numerico!")
        
while not flag3:
    estado_civil = input("ingrese su estado civil: ")
    
    if estado_civil == "S" or estado_civil == "C" or estado_civil == "c" or estado_civil == "s":
        estado_civil = estado_civil.upper()
        flag3 = True
    else: 
        print("Por favor ingrese 'S' para soltero y 'C' para casado!")

aumen_soltero = (sueldo_basico * AUMEN_SOLTERO) - sueldo_basico
aumen_casado = (sueldo_basico * AUMEN_CASADO) - sueldo_basico

if estado_civil == 'S':
    estado_civil = "Soltero"
    sueldo_soltero = (aumen_soltero * antiguedad) + sueldo_basico
    desc_jubilacion = sueldo_soltero * DESC_JUBILACION
    desc_obra_social = (sueldo_soltero * DESC_OBRA_SOCIAL)
    desc_sindicato = (sueldo_soltero * DESC_SINDICATO)
    sueldo_neto = sueldo_soltero - desc_jubilacion - desc_obra_social - desc_sindicato

if estado_civil == 'C':
    estado_civil = "Casado"
    sueldo_casado = (aumen_casado * antiguedad) + sueldo_basico
    desc_jubilacion = aumen_casado * DESC_JUBILACION
    desc_obra_social = (aumen_casado * DESC_OBRA_SOCIAL)
    desc_sindicato = (aumen_casado * DESC_SINDICATO)
    sueldo_neto = sueldo_casado - desc_jubilacion - desc_obra_social - desc_sindicato
desc_jubilacion = round(float(desc_jubilacion),2)
desc_obra_social = round(float(desc_obra_social),2)
desc_sindicato = round(float(desc_sindicato),2)
sueldo_neto = round(float(sueldo_neto),2)
if estado_civil == "Soltero" or estado_civil == "Casado":
    print(f"""
    Eatado civil: {estado_civil}
    Sueldo basico: ${sueldo_basico}
    Antiguedad: {antiguedad}

    Descuentos:

    - Jubilación - ${desc_jubilacion} 

    - Obra Social - ${desc_obra_social} 

    - Sindicato - ${desc_sindicato} 

    Sueldo Neto ${sueldo_neto}""")