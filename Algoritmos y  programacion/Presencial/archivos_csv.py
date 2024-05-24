import csv
alumnos = [
    ("Manuel", "Aprobo",4,7),
    ("Lorena", "Desaprobo",3,0),
    ("Javier", "Desaprovo",7,7),
    ("Marta", "Aprobo",8,8) ]
whit open("alumnos.csv", "w", newline="\n") as arch_csv:
    writer = csv.writer(arch_csv, delimiter = ";")
    encabezado = ["Nombre", "TP", "N_P1", "N_P2"]
    writer.writerow(encabezado)
    for alumn in alumnos:
        writer.writerow(alum)
whit open("alumnos.csv", "w", newline="\n") as arch_csv:
    registros = csv.reader(arch_csv, delimiter = ";")
    for registro in registros:
        print(registro)

whit open("alumnos.csv", "w", newline="\n") as arch_csv:
    registros = csv.reader(arch_csv, delimiter = ";")