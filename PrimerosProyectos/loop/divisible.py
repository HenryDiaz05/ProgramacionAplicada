#definimos un rango de numeros a mostrar
for i in range(100, 301):
    # Cada numero que contenga la variable i sera ingrsada al condicional
    #Se analiza si es divisible por 12 al tener un residuo de 0
    if (i%12) != 0:
        continue
    print(i)