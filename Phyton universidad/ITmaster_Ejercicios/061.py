numero = int(input("numero: "))

if numero <= 1:
    fact = 1
else: 
    fact = 1
    for n in range (1,numero+1):
        fact *= n
cad = str(fact)        
#print(f"Factorial : {fact}")
print(f"Cantidad de caracteres: {len(cad)}")