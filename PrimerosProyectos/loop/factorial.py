
value = int(input("Ingresar un valor entero positivo: "))
print("Valor: ", value)
a = isinstance(value, int) #develve true si cumple la condicion
if a == True and value > 0:
    fact = 1
    for i in range (1, value + 1):
        fact = fact*i            
    print(f'{value}!= ', fact)
else:
    print("porfavor, ingrese un numero positivo")