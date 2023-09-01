a = int(input("Ingrese el rango para saber sus impares: "))
for i in range (1,a):
    residual = i%2
    if residual == 0:
        print(f'{i} es par')
    else:
        print(f'{i} es impar')

#multiplos de 3 en el rango
for i in range (0,a):
    result = i**3
    print(result)


times = input("Enter a number of times: ")
times = float(times)
times = int(times)
print(type(times))# aseguramos el cambio de tipo de variable
print(times)

if times == 0:
    print("no hacer nada")
else:
    for i in range(1,times+1): #mostrar los numeros de 1 a times
        print("i = ", i)
